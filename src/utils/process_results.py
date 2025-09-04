import re
import pandas as pd
from pathlib import Path
from datetime import datetime
import argparse
import sys
import numpy as np

"""
PROCESADOR DE RESULTADOS DE EXPERIMENTOS Q-LEARNING

Este script procesa archivos de resultados en formato Markdown generados por experimentos
de Q-learning en NetSecGame y los convierte a formato CSV estructurado para análisis.
"""

def parse_results_md(file_path):
    """
    Parsea el archivo de resultados en formato markdown y extrae los datos estructurados.
    Maneja tanto datos de prueba cada N episodios como resultados finales.
    Permite bloques de test con solo las líneas mínimas.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = []

    # Patrón para bloques de test (mínimo: encabezado, Wins, epsilon)
    test_block_pattern = r'Tested for (\d+) episodes after (\d+) training episode\.(.*?)(?=Tested for |\Z|Final model performance)'
    test_blocks = re.findall(test_block_pattern, content, re.DOTALL)

    for test_episodes, training_episodes, block in test_blocks:
        # Extraer valores presentes
        wins = re.search(r'Wins=(\d+)', block)
        epsilon = re.search(r'epsilon=([\d.]+)', block)
        detections = re.search(r'Detections=(\d+)', block)
        winrate = re.search(r'winrate=([\d.]+)%', block)
        detection_rate = re.search(r'detection_rate=([\d.]+)%', block)
        avg_returns = re.search(r'average_returns=([-\d.]+) \+- ([\d.]+)', block)
        avg_episode_steps = re.search(r'average_episode_steps=([\d.]+) \+- ([\d.]+)', block)
        avg_win_steps = re.search(r'average_win_steps=([\d.]+) \+- ([\d.]+)', block)
        avg_detected_steps = re.search(r'average_detected_steps=([\d.nan]+) \+- ([\d.nan]+)', block)
        avg_max_steps_steps = re.search(r'average_max_steps_steps=([\d.]+) \+- ([\d.]+)', block)

        # Asignar valores, usando np.nan o None si no están presentes
        data.append({
            'experiment_id': f'test_{int(training_episodes):05d}',
            'model_name': f'Model_test_{training_episodes}',
            'test_episodes': int(test_episodes),
            'training_episodes': int(training_episodes),
            'wins': int(wins.group(1)) if wins else np.nan,
            'detections': int(detections.group(1)) if detections else np.nan,
            'winrate': float(winrate.group(1)) if winrate else np.nan,
            'detection_rate': float(detection_rate.group(1)) if detection_rate else np.nan,
            'avg_returns': float(avg_returns.group(1)) if avg_returns else np.nan,
            'std_returns': float(avg_returns.group(2)) if avg_returns else np.nan,
            'avg_episode_steps': float(avg_episode_steps.group(1)) if avg_episode_steps else np.nan,
            'std_episode_steps': float(avg_episode_steps.group(2)) if avg_episode_steps else np.nan,
            'avg_win_steps': float(avg_win_steps.group(1)) if avg_win_steps else np.nan,
            'std_win_steps': float(avg_win_steps.group(2)) if avg_win_steps else np.nan,
            'avg_detected_steps': np.nan if not avg_detected_steps else (np.nan if avg_detected_steps.group(1) == 'nan' else float(avg_detected_steps.group(1))),
            'std_detected_steps': np.nan if not avg_detected_steps else (np.nan if avg_detected_steps.group(2) == 'nan' else float(avg_detected_steps.group(2))),
            'avg_max_steps_steps': float(avg_max_steps_steps.group(1)) if avg_max_steps_steps else np.nan,
            'std_max_steps_steps': float(avg_max_steps_steps.group(2)) if avg_max_steps_steps else np.nan,
            'current_epsilon': float(epsilon.group(1)) if epsilon else np.nan,
            'data_type': 'test_checkpoint',
            'scenario': extract_scenario_from_filename(file_path),
            'algorithm': 'q_learning',
            'timestamp': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        })

    # Patrón para resultado final (igual que antes)
    final_pattern = r'Final model performance after (\d+) episodes\.(.*?)(?=Tested for |\Z)'
    final_blocks = re.findall(final_pattern, content, re.DOTALL)
    for final_episodes, block in final_blocks:
        wins = re.search(r'Wins=(\d+)', block)
        epsilon = re.search(r'epsilon=([\d.]+)', block)
        detections = re.search(r'Detections=(\d+)', block)
        winrate = re.search(r'winrate=([\d.]+)%', block)
        detection_rate = re.search(r'detection_rate=([\d.]+)%', block)
        avg_returns = re.search(r'average_returns=([-\d.]+) \+- ([\d.]+)', block)
        avg_episode_steps = re.search(r'average_episode_steps=([\d.]+) \+- ([\d.]+)', block)
        avg_win_steps = re.search(r'average_win_steps=([\d.]+) \+- ([\d.]+)', block)
        avg_detected_steps = re.search(r'average_detected_steps=([\d.nan]+) \+- ([\d.nan]+)', block)
        avg_max_steps_steps = re.search(r'average_max_steps_steps=([\d.]+) \+- ([\d.]+)', block)

        data.append({
            'experiment_id': f'final_{int(final_episodes):05d}',
            'model_name': f'Model_final_{final_episodes}',
            'test_episodes': None,
            'training_episodes': int(final_episodes),
            'wins': int(wins.group(1)) if wins else np.nan,
            'detections': int(detections.group(1)) if detections else np.nan,
            'winrate': float(winrate.group(1)) if winrate else np.nan,
            'detection_rate': float(detection_rate.group(1)) if detection_rate else np.nan,
            'avg_returns': float(avg_returns.group(1)) if avg_returns else np.nan,
            'std_returns': float(avg_returns.group(2)) if avg_returns else np.nan,
            'avg_episode_steps': float(avg_episode_steps.group(1)) if avg_episode_steps else np.nan,
            'std_episode_steps': float(avg_episode_steps.group(2)) if avg_episode_steps else np.nan,
            'avg_win_steps': float(avg_win_steps.group(1)) if avg_win_steps else np.nan,
            'std_win_steps': float(avg_win_steps.group(2)) if avg_win_steps else np.nan,
            'avg_detected_steps': np.nan if not avg_detected_steps else (np.nan if avg_detected_steps.group(1) == 'nan' else float(avg_detected_steps.group(1))),
            'std_detected_steps': np.nan if not avg_detected_steps else (np.nan if avg_detected_steps.group(2) == 'nan' else float(avg_detected_steps.group(2))),
            'avg_max_steps_steps': float(avg_max_steps_steps.group(1)) if avg_max_steps_steps else np.nan,
            'std_max_steps_steps': float(avg_max_steps_steps.group(2)) if avg_max_steps_steps else np.nan,
            'current_epsilon': float(epsilon.group(1)) if epsilon else np.nan,
            'data_type': 'final_result',
            'scenario': extract_scenario_from_filename(file_path),
            'algorithm': 'q_learning',
            'timestamp': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        })

    if not data:
        raise ValueError("No se encontraron datos válidos en el archivo")

    return pd.DataFrame(data)

def extract_scenario_from_filename(file_path):
    """
    Extrae el nombre del escenario del nombre del archivo
    """
    filename = Path(file_path).stem.lower()
    
    if 'tiny' in filename:
        return 'tiny'
    elif 'small' in filename:
        return 'small'
    elif 'three' in filename or '3net' in filename:
        return 'three_net'
    else:
        return 'unknown'

def generate_output_filename(input_file_path, base_output_dir=None):
    """
    Genera el nombre del archivo de salida basado en el archivo de entrada
    Formato: INPUT_FILE_processed.csv
    """
    input_path = Path(input_file_path)
    
    # Extraer nombre base del archivo (sin extensión)
    input_name = input_path.stem
    
    # Generar nombre de salida
    output_name = f"{input_name}_processed.csv"
    
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
            base_path / "data" / "raw" / "netsecgame-experiments" / "results-tiny.md",
            base_path / "data" / "raw" / "netsecgame-experiments" / "results-small.md",
            base_path / "data" / "raw" / "netsecgame-experiments" / "results-three-net.md",
            base_path / "data" / "raw" / "results-tiny.md",
            base_path / "data" / "raw" / "results-small.md",
            base_path / "data" / "raw" / "results-three-net.md",
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
        
        # Mostrar resumen de datos procesados
        print(f"\n Resumen de datos procesados:")
        print(f"   • Total de registros: {len(df)}")
        print(f"   • Checkpoints de prueba: {len(df[df['data_type'] == 'test_checkpoint'])}")
        print(f"   • Resultados finales: {len(df[df['data_type'] == 'final_result'])}")
        print(f"   • Escenario detectado: {df['scenario'].iloc[0] if len(df) > 0 else 'N/A'}")
        
        if len(df[df['data_type'] == 'test_checkpoint']) > 0:
            test_data = df[df['data_type'] == 'test_checkpoint']
            print(f"   • Rango de episodios de entrenamiento: {test_data['training_episodes'].min()} - {test_data['training_episodes'].max()}")
            print(f"   • Mejor winrate en checkpoints: {test_data['winrate'].max():.2f}% (episodio {test_data.loc[test_data['winrate'].idxmax(), 'training_episodes']})")
        
        # Guardar CSV procesado
        df.to_csv(output_file, index=False)
        
        print(f"\n Procesamiento completado exitosamente")
        print(f"   Archivo guardado: {output_file}")
        
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
        description="Procesa archivos de resultados de experimentos Q-learning con checkpoints cada 1000 episodios",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python process_results.py --input results-tiny.md
  python process_results.py --input data/raw/results-small.md --output data/processed/
  python process_results.py  # Busca automáticamente el archivo

El script procesa tanto los checkpoints de prueba cada 1000 episodios como el resultado final.
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
    print("Soporta formato con checkpoints cada 1000 episodios")
    print()
    
    df = main(args.input, args.output)
    
    if df is not None:
        print(f"\nProcesamiento completado exitosamente")
    else:
        print(f"\nEl procesamiento falló.")
        sys.exit(1)