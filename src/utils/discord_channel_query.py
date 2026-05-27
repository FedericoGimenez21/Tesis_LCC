#!/usr/bin/env python3
"""
Consulta mensajes y adjuntos de un canal de Discord para recuperar material de la tesis.

Importante:
- Un webhook de Discord SOLO permite publicar mensajes en un canal.
- Para leer/consultar mensajes históricos del canal se necesita un BOT TOKEN con permisos
  para ver el canal y leer el historial de mensajes.

Variables de entorno soportadas:
- DISCORD_BOT_TOKEN: token del bot para leer mensajes.
- DISCORD_CHANNEL_ID: ID del canal a consultar.
- DISCORD_WEBHOOK_URL: webhook para publicar una pregunta/mensaje en el canal.

Ejemplos:
  # Buscar mensajes que contengan "scenario1" en los últimos 500 mensajes
  DISCORD_BOT_TOKEN="..." DISCORD_CHANNEL_ID="..." \
    python src/utils/discord_channel_query.py --contains scenario1 --max-messages 500

  # Descargar imágenes/adjuntos de mensajes que mencionen "feature-based"
  python src/utils/discord_channel_query.py \
    --contains feature-based --save-attachments outputs/discord_attachments

  # Publicar una pregunta usando webhook
  DISCORD_WEBHOOK_URL="..." \
    python src/utils/discord_channel_query.py --ask "¿Dónde están los resultados finales de scenario1?"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

DISCORD_API_BASE = "https://discord.com/api/v10"
DEFAULT_CHANNEL_ID = "1364959110444875827"


def load_dotenv() -> None:
    """Carga variables desde .env si existe, sin depender de python-dotenv."""
    candidates = [
        Path.cwd() / ".env",
        Path(__file__).resolve().parents[2] / ".env",  # raíz de Tesis_LCC
    ]
    for env_path in candidates:
        if not env_path.exists():
            continue
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


def http_json(
    url: str,
    *,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    payload: Optional[Dict[str, Any]] = None,
) -> Any:
    data = None
    final_headers = {
        "User-Agent": "TesisDiscordQueryBot/1.0 (+https://discord.com/developers/docs)",
        "Accept": "application/json",
        **dict(headers or {}),
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        final_headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=data, headers=final_headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Error HTTP {exc.code} en {url}: {body}") from exc


def fetch_messages(channel_id: str, bot_token: str, max_messages: int) -> List[Dict[str, Any]]:
    """Trae hasta max_messages mensajes recientes del canal, paginando de a 100."""
    headers = {"Authorization": f"Bot {bot_token}"}
    messages: List[Dict[str, Any]] = []
    before: Optional[str] = None

    while len(messages) < max_messages:
        limit = min(100, max_messages - len(messages))
        params = {"limit": str(limit)}
        if before:
            params["before"] = before
        url = f"{DISCORD_API_BASE}/channels/{channel_id}/messages?{urllib.parse.urlencode(params)}"
        batch = http_json(url, headers=headers)
        if not batch:
            break
        messages.extend(batch)
        before = batch[-1]["id"]
        time.sleep(0.35)  # ser amable con rate limits

    return messages


def message_matches(message: Dict[str, Any], text: Optional[str], author: Optional[str]) -> bool:
    if text:
        haystack_parts = [message.get("content", "")]
        for attachment in message.get("attachments", []):
            haystack_parts.append(attachment.get("filename", ""))
            haystack_parts.append(attachment.get("description", "") or "")
        for embed in message.get("embeds", []):
            haystack_parts.append(embed.get("title", "") or "")
            haystack_parts.append(embed.get("description", "") or "")
        haystack = "\n".join(haystack_parts).lower()
        if text.lower() not in haystack:
            return False

    if author:
        author_data = message.get("author", {})
        author_haystack = " ".join(
            str(author_data.get(k, "")) for k in ("username", "global_name", "id")
        ).lower()
        if author.lower() not in author_haystack:
            return False

    return True


def summarize_message(message: Dict[str, Any]) -> Dict[str, Any]:
    attachments = message.get("attachments", [])
    return {
        "id": message.get("id"),
        "timestamp": message.get("timestamp"),
        "author": message.get("author", {}).get("global_name")
        or message.get("author", {}).get("username"),
        "content": message.get("content", ""),
        "attachments": [
            {
                "filename": a.get("filename"),
                "url": a.get("url"),
                "content_type": a.get("content_type"),
                "size": a.get("size"),
            }
            for a in attachments
        ],
    }


def print_messages(messages: Iterable[Dict[str, Any]]) -> None:
    for msg in messages:
        item = summarize_message(msg)
        print("-" * 80)
        print(f"ID: {item['id']}")
        print(f"Fecha: {item['timestamp']}")
        print(f"Autor: {item['author']}")
        content = item["content"].strip() or "(sin texto)"
        print(f"Mensaje: {content}")
        if item["attachments"]:
            print("Adjuntos:")
            for att in item["attachments"]:
                print(f"  - {att['filename']} ({att['content_type']}, {att['size']} bytes)")
                print(f"    {att['url']}")


def safe_filename(name: str) -> str:
    return "".join(c if c.isalnum() or c in ".-_" else "_" for c in name)


def download_file(url: str, path: Path) -> None:
    with urllib.request.urlopen(url, timeout=60) as response:
        path.write_bytes(response.read())


def save_attachments(messages: Iterable[Dict[str, Any]], output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for msg in messages:
        msg_id = msg.get("id", "mensaje")
        for attachment in msg.get("attachments", []):
            url = attachment.get("url")
            filename = attachment.get("filename") or f"attachment_{count}"
            if not url:
                continue
            target = output_dir / f"{msg_id}_{safe_filename(filename)}"
            download_file(url, target)
            count += 1
            print(f"Descargado: {target}")
    return count


def post_webhook(webhook_url: str, content: str) -> None:
    payload = {"content": content}
    http_json(webhook_url, method="POST", payload=payload)


def parse_args() -> argparse.Namespace:
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Consulta mensajes/adjuntos de Discord relacionados con la tesis."
    )
    parser.add_argument(
        "--channel-id",
        default=os.getenv("DISCORD_CHANNEL_ID", DEFAULT_CHANNEL_ID),
        help="ID del canal; por defecto usa el canal de la tesis",
    )
    parser.add_argument("--bot-token", default=os.getenv("DISCORD_BOT_TOKEN"), help="Token del bot")
    parser.add_argument("--webhook-url", default=os.getenv("DISCORD_WEBHOOK_URL"), help="Webhook para publicar mensajes")
    parser.add_argument("--max-messages", type=int, default=300, help="Cantidad máxima de mensajes recientes a consultar")
    parser.add_argument("--contains", help="Filtrar mensajes que contengan este texto")
    parser.add_argument("--author", help="Filtrar por username/global_name/id del autor")
    parser.add_argument("--save-attachments", type=Path, help="Directorio donde descargar adjuntos de los mensajes filtrados")
    parser.add_argument("--json", action="store_true", help="Imprimir salida en JSON")
    parser.add_argument("--ask", help="Publicar esta pregunta/mensaje en el canal usando webhook")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.ask:
        if not args.webhook_url:
            print("Error: --ask requiere --webhook-url o DISCORD_WEBHOOK_URL.", file=sys.stderr)
            return 2
        post_webhook(args.webhook_url, args.ask)
        print("Mensaje enviado al canal mediante webhook.")

    needs_read = args.contains or args.author or args.save_attachments or not args.ask
    if not needs_read:
        return 0

    if not args.channel_id:
        print("Error: falta --channel-id o DISCORD_CHANNEL_ID.", file=sys.stderr)
        return 2
    if not args.bot_token:
        print(
            "Error: para leer mensajes históricos se necesita --bot-token o DISCORD_BOT_TOKEN. "
            "Un webhook solo sirve para publicar mensajes, no para consultar el canal.",
            file=sys.stderr,
        )
        return 2

    messages = fetch_messages(args.channel_id, args.bot_token, args.max_messages)
    filtered = [m for m in messages if message_matches(m, args.contains, args.author)]

    if args.json:
        print(json.dumps([summarize_message(m) for m in filtered], ensure_ascii=False, indent=2))
    else:
        print(f"Mensajes leídos: {len(messages)} | Mensajes filtrados: {len(filtered)}")
        print_messages(filtered)

    if args.save_attachments:
        total = save_attachments(filtered, args.save_attachments)
        print(f"Adjuntos descargados: {total}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
