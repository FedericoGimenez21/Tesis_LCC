# Material recuperado de Workflowy sobre la tesis de Fede

## Fuente

Este documento resume los ítems encontrados en Workflowy relacionados con la tesis de Fede, a partir de calendario, journal y tareas consultadas manualmente con las herramientas `workflowy_list`, `workflowy_get` y `workflowy_list_calendar`.

> Nota: Workflowy no expone una búsqueda global directa en las herramientas disponibles; por eso el relevamiento se hizo revisando targets, nodos principales, calendario y entradas plausiblemente relacionadas.

## Ítems encontrados

### 2026-02-23 — meet with Fede

Nodo Workflowy:

- `meet with Fede`
- ID: `3d03d116-133a-8576-6119-6f9c935ac816`

Hijos encontrados:

- `update:`
  - ID: `00b63d6b-86e9-1892-c990-2a8b89080da2`

Dentro de `update:`:

- `Saltelli was discarded too much time`
  - ID: `1dca1b6c-d471-86ff-a791-c78826ba3644`
- `hyperparemeter`
  - ID: `47848828-4d2e-2758-2b31-2a4e6b4d2bd9`
- ítem vacío
  - ID: `cdba569e-3715-8329-c596-eebca2329f36`
- `about 1 hour`
  - ID: `dd7b605f-c88b-fd6e-05f8-850dd9500714`

Interpretación:

- En esta reunión se discutió la optimización de hiperparámetros.
- Se descartó el análisis de sensibilidad con Saltelli/Sobol por costo temporal excesivo.
- Se registró una estimación temporal de aproximadamente una hora, posiblemente asociada a una ejecución o evaluación puntual.

### 2026-02-23 — issue para NetSecGame

Nodo Workflowy:

- `create an issue for netsecgame. Server-side calculation of agent's performance metrics`
- ID: `80402f0c-66df-6f1f-e9f4-2b7fc990fecc`
- Enlace: `https://github.com/stratosphereips/NetSecGame/issues/445`

Interpretación:

- Se identificó la necesidad de calcular métricas de performance del agente del lado del servidor de NetSecGame.
- Esto es relevante para la tesis porque los experimentos dependen fuertemente de métricas como `win_rate`, detecciones, retornos y cantidad de pasos.
- También está relacionado con los problemas observados en Discord, donde algunas ejecuciones largas no registraban correctamente el mejor `win_rate`.

### 2026-05-04 — syncup with Fede and Luciano

Nodo Workflowy:

- `syncup with fede and luciano`
- ID: `6b293c81-1a4a-775b-5943-a5efd13f8d52`

Hijos:

- `Fede results image`
  - ID: `c5dbc6dd-b50d-e403-9403-89bedb2cabe4`
  - Enlace: `https://www.dropbox.com/scl/fi/z80y90v825x3yihg5en49/Copia_de_training.drawio.webp?rlkey=gd3hphdnfsyuxxt8nkxrwckro&st=8jdmef21&dl=1`
- `there is a problem with the actions. Since the game starts every episode with different known and controlled hosts. We can have actions in the table for the same state in feature-based format that lead to incorrect actions`
  - ID: `b6311ebf-4fe3-3e11-f148-daf746c24fb7`

Interpretación:

- Se discutieron resultados de Fede y se registró una imagen asociada.
- Se identificó un problema importante en la representación feature-based: si cada episodio empieza con distintos `known_hosts` y `controlled_hosts`, una misma representación de estado basada en características puede mapear a acciones que son válidas en un episodio pero inválidas en otro.
- Esto puede explicar parte de la variabilidad o degradación del desempeño, especialmente cuando la Q-table abstrae estados y acciones de forma demasiado compacta.

### 2026-05-21 — meet with Fede and Luciano

Nodo Workflowy:

- `meeti wht fede and luciano`
- ID: `d8a25817-15d7-a6e6-4089-8a54664d0a6d`

Hijos:

- `ask Marisa`
  - ID: `9953eba4-7df2-cf7d-4ff8-05570968e502`
- `create an overleaf with the index of the thesis`
  - ID: `7ffa2d15-7cf6-e199-27a5-e5986f49bb5e`
- `calculate space size`
  - ID: `d687203b-005b-9b5b-3bee-201e3a440103`
- `run new a new experiment with 140 generations (it will take 15 days)`
  - ID: `41efd28b-7195-cb71-e23e-970368f4c67d`

Interpretación:

- Se definieron tareas concretas para avanzar en la tesis:
  - consultar a Marisa;
  - crear un Overleaf con el índice de la tesis;
  - calcular el tamaño del espacio de estados/acciones;
  - ejecutar un nuevo experimento con 140 generaciones, estimado en 15 días.
- Este último punto conecta directamente con el diagnóstico de Discord: el algoritmo genético necesita más generaciones/presupuesto para evaluar si realmente puede mejorar la inicialización de la Q-table.

## Conexión con el análisis de Discord

El material de Workflowy refuerza lo observado en Discord:

1. **Costo computacional alto**: se descartó Saltelli por tiempo y se planificó un experimento de 140 generaciones con duración estimada de 15 días.
2. **Optimización de hiperparámetros crítica**: aparece explícitamente como tema de reunión.
3. **Problemas de medición/registro**: la necesidad de calcular métricas del lado del servidor de NetSecGame coincide con problemas de logging/registro de `win_rate` observados en ejecuciones SMAC.
4. **Problemas de representación feature-based**: el mismo estado abstracto puede llevar a acciones inválidas si cambia la configuración inicial de hosts conocidos/controlados.
5. **Necesidad de formalizar la tesis**: se registró la creación de Overleaf y el índice del documento.

## Ítems accionables derivados

- Revisar el issue de NetSecGame sobre métricas server-side.
- Incorporar en la tesis la limitación de la representación feature-based respecto a acciones válidas/inválidas bajo distintas condiciones iniciales.
- Documentar que Saltelli/Sobol fue descartado por costo y que se eligió SMAC3 como alternativa práctica.
- Documentar que una evaluación robusta del genético requiere ejecuciones largas, por ejemplo 140 generaciones y alrededor de 15 días.
- Conectar el experimento genético de 140 generaciones con los resultados preliminares de Discord.
