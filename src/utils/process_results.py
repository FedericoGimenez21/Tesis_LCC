import re
import pandas as pd
from pathlib import Path
from datetime import datetime
import argparse
import sys

"""
PROCESADOR DE RESULTADOS DE EXPERIMENTOS Q-LEARNING

Este script procesa archivos de resultados en formato Markdown generados por experimentos
de Q-learning en NetSecGame y los convierte a formato CSV estructurado para análisis.
"""

def parse_results_md(file_path):
    """
    Parsea el archivo de resultados en formato markdown y extrae los datos estructurados
    """
    # Verificar que el archivo existe
    if not file_path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Patrón simplificado para extraer los datos de cada experimento
    # Buscar bloques que contienen "Final model performance"
    blocks = re.split(r'(?=Final model performance)', content)
    
    data = []
    for i, block in enumerate(blocks):
        if 'Final model performance' not in block:
            continue
        # Extraer cada métrica individualmente para mayor robustez
        try:
            # Episodios
            episodes_match = re.search(r'after (\d+) episodes', block)
            episodes = int(episodes_match.group(1)) if episodes_match else None
            
            # Wins
            wins_match = re.search(r'Wins=(\d+)', block)
            wins = int(wins_match.group(1)) if wins_match else None
            
            # Winrate
            winrate_match = re.search(r'winrate=([\d.]+)%', block)
            winrate = float(winrate_match.group(1)) if winrate_match else None
            
            # Average returns - modificado para capturar valores negativos también
            returns_match = re.search(r'average_returns=([-\d.]+) \+- ([\d.]+)', block)
            avg_returns = float(returns_match.group(1)) if returns_match else None
            std_returns = float(returns_match.group(2)) if returns_match else None
            
            # Episode steps
            episode_steps_match = re.search(r'average_episode_steps=([\d.]+) \+- ([\d.]+)', block)
            avg_episode_steps = float(episode_steps_match.group(1)) if episode_steps_match else None
            std_episode_steps = float(episode_steps_match.group(2)) if episode_steps_match else None
            
            # Win steps
            win_steps_match = re.search(r'average_win_steps=([\d.]+) \+- ([\d.]+)', block)
            avg_win_steps = float(win_steps_match.group(1)) if win_steps_match else None
            std_win_steps = float(win_steps_match.group(2)) if win_steps_match else None
            
            # Epsilon
            epsilon_match = re.search(r'epsilon=([\d.]+)', block)
            epsilon_val = float(epsilon_match.group(1)) if epsilon_match else None
            
            # Limpiar epsilon a valores estándar
            if epsilon_val:
                if abs(epsilon_val - 0.30) < 0.01:
                    epsilon_clean = 0.30
                elif abs(epsilon_val - 0.35) < 0.01:
                    epsilon_clean = 0.35
                else:
                    epsilon_clean = round(epsilon_val, 2)
            else:
                epsilon_clean = None
            
            # Solo agregar si tenemos datos mínimos - modificado para incluir avg_returns negativos
            if wins is not None and winrate is not None and epsilon_clean is not None:
                data.append({
                    'experiment_id': f'exp_{len(data)+1:03d}',
                    'model_name': f'Model_{len(data)+1}',
                    'episodes': episodes,
                    'wins': wins,
                    'winrate': winrate,
                    'avg_returns': avg_returns,  # Ahora incluye valores negativos
                    'std_returns': std_returns,
                    'avg_episode_steps': avg_episode_steps,
                    'std_episode_steps': std_episode_steps,
                    'avg_win_steps': avg_win_steps,
                    'std_win_steps': std_win_steps,
                    'final_epsilon': epsilon_clean,
                    'epsilon_start': 0.5,  # Asumido del nombre del experimento
                    'scenario': 'tiny',    # Asumido del nombre del archivo
                    'algorithm': 'q_learning',
                    'timestamp': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                })
                
        except Exception as e:
            print(f"Error procesando bloque {i}: {e}")
            continue
    
    if not data:
        raise ValueError("No se encontraron datos válidos en el archivo")
    
    return pd.DataFrame(data)

def generate_output_filename(input_file_path, base_output_dir=None):
    """
    Genera el nombre del archivo de salida basado en el archivo de entrada
    Formato: INPUT_FILE_epsilon_start_NUMBER_processed.csv
    """
    input_path = Path(input_file_path)
    
    # Extraer nombre base del archivo (sin extensión)
    input_name = input_path.stem
    
    
    # Generar nombre de salida
    output_name = f"{input_name}-processed.csv"
    
    # Determinar directorio de salida
    if base_output_dir:
        output_dir = Path(base_output_dir)
    else:
        # Usar estructura de proyecto estándar
        project_root = Path(__file__).parent.parent.parent
        output_dir = project_root / "data" / "processed"
    
    # Crear directorio si no existe
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return output_dir / output_name

def main(input_file_path=None, output_dir=None):
    """
    Función principal que procesa el archivo de resultados
    
    Args:
        input_file_path: Ruta al archivo de entrada (opcional)
        output_dir: Directorio de salida (opcional)
    """
    
    # Si no se proporciona input_file_path, buscar en ubicaciones predeterminadas
    if input_file_path is None:
        print("🔍 No se especificó archivo de entrada. Buscando en ubicaciones predeterminadas...")
        
        base_path = Path(__file__).parent.parent.parent  # Subir 3 niveles desde src/utils/
        
        possible_paths = [
            base_path / "data" / "raw" / "netsecgame-experiments" / "epsilon-start-05" / "results-tiny.md",
            base_path / "data" / "raw" / "netsecgame-experiments" / "epsilon-start-09" / "results-tiny.md",
            base_path / "data" / "raw" / "results-tiny.md",
            base_path / "results-tiny.md",
            Path("results-tiny.md"),  # En directorio actual
        ]
        
        input_file = None
        for path in possible_paths:
            if path.exists():
                input_file = path
                break
        
        if input_file is None:
            print("No se encontró el archivo de resultados en las siguientes ubicaciones:")
            for path in possible_paths:
                print(f"   • {path}")
            print("\nSugerencias:")
            print("   1. Especifica la ruta del archivo: python process_results.py --input /ruta/al/archivo.md")
            print("   2. Copia el archivo a una de las ubicaciones esperadas")
            return None
    else:
        input_file = Path(input_file_path)
        if not input_file.exists():
            print(f"Archivo no encontrado: {input_file}")
            return None
    
    # Generar nombre del archivo de salida
    output_file = generate_output_filename(input_file, output_dir)
    
    try:
        # Procesar datos
        print(f"Procesando archivo: {input_file}")
        print(f"Archivo de salida: {output_file}")
        
        df = parse_results_md(input_file)
        
        # Guardar CSV procesado
        df.to_csv(output_file, index=False)        
        return df
        
    except Exception as e:
        print(f"Error procesando el archivo: {e}")
        print(f"Archivo fuente: {input_file}")
        return None

def parse_args():
    """
    Parsea argumentos de línea de comandos
    """
    parser = argparse.ArgumentParser(
        description="Procesa archivos de resultados de experimentos Q-learning",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python process_results.py --input results-tiny-epsilon-start-05.md
  python process_results.py --input data/raw/results.md --output data/processed/
  python process_results.py  # Busca automáticamente el archivo
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        type=str,
        help='Ruta al archivo de resultados (.md) a procesar'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Directorio donde guardar el archivo CSV procesado (opcional)'
    )
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    # Mostrar información de uso
    print("Procesador de Resultados Q-Learning")
    print("="*50)
    
    df = main(args.input, args.output)
    
    if df is not None:
        print(f"\nProcesamiento completado exitosamente")
    else:
        print(f"\nEl procesamiento falló.")
        sys.exit(1)