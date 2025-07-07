import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import argparse
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def load_processed_data(data_dir=None):
    """
    Carga todos los archivos CSV procesados del directorio especificado
    """
    if data_dir is None:
        # Buscar automáticamente en ubicaciones predeterminadas
        base_path = Path(__file__).parent.parent.parent
        data_dir = base_path / "data" / "processed"
    
    data_dir = Path(data_dir)
    
    if not data_dir.exists():
        print(f"Directorio no encontrado: {data_dir}")
        return None
    
    # Buscar todos los archivos CSV procesados
    csv_files = list(data_dir.glob("*processed*.csv"))
    
    if not csv_files:
        print(f"No se encontraron archivos CSV procesados en: {data_dir}")
        return None
    
    print(f"Encontrados {len(csv_files)} archivos CSV:")
    for file in csv_files:
        print(f"  - {file.name}")
    
    # Cargar y combinar todos los archivos
    all_data = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            df['source_file'] = file.stem  # Agregar información del archivo fuente
            all_data.append(df)
            print(f"Cargado: {file.name} ({len(df)} registros)")
        except Exception as e:
            print(f"Error cargando {file.name}: {e}")
    
    if not all_data:
        print("No se pudieron cargar datos")
        return None
    
    # Combinar todos los datasets
    combined_df = pd.concat(all_data, ignore_index=True)
    print(f"\nTotal de registros combinados: {len(combined_df)}")
    
    return combined_df

def prepare_data_for_analysis(df):
    """
    Prepara los datos para análisis agrupado
    """
    if df is None:
        return None
    
    # Asegurar que las columnas necesarias existen
    required_columns = ['episodes', 'winrate', 'avg_returns', 'avg_episode_steps', 'avg_win_steps']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"Columnas faltantes: {missing_columns}")
        return None
    
    # Convertir tipos de datos
    df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
    df['winrate'] = pd.to_numeric(df['winrate'], errors='coerce')
    df['avg_returns'] = pd.to_numeric(df['avg_returns'], errors='coerce')
    df['avg_episode_steps'] = pd.to_numeric(df['avg_episode_steps'], errors='coerce')
    df['avg_win_steps'] = pd.to_numeric(df['avg_win_steps'], errors='coerce')
    
    # Agregar columna de epsilon si existe final_epsilon
    if 'final_epsilon' in df.columns:
        df['epsilon_group'] = df['final_epsilon'].round(2)
    
    # Limpiar datos
    df = df.dropna(subset=required_columns)
    
    print(f"Datos preparados: {len(df)} registros válidos")
    print(f"Grupos de episodios únicos: {sorted(df['episodes'].unique())}")
    
    if 'epsilon_group' in df.columns:
        print(f"Grupos de epsilon únicos: {sorted(df['epsilon_group'].unique())}")
    
    return df

def calculate_group_statistics(df, group_by='episodes'):
    """
    Calcula estadísticas agrupadas (media y desviación estándar)
    """
    metrics = ['winrate', 'avg_returns', 'avg_episode_steps', 'avg_win_steps']
    
    # Agrupar y calcular estadísticas
    grouped_stats = df.groupby(group_by)[metrics].agg(['mean', 'std', 'count']).round(3)
    
    # Aplanar nombres de columnas
    grouped_stats.columns = [f"{metric}_{stat}" for metric, stat in grouped_stats.columns]
    
    print(f"\nEstadísticas agrupadas por {group_by}:")
    print("=" * 80)
    print(grouped_stats)
    
    return grouped_stats

def setup_output_directory(save_images=False):
    """
    Configura directorio de salida para gráficos
    """
    if not save_images:
        return None
    
    base_path = Path(__file__).parent.parent.parent
    output_dir = base_path / "outputs" / "figures" / f"comparison_analysis"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Directorio de salida: {output_dir}")
    return output_dir

def save_figure(output_dir, filename, dpi=300):
    """
    Guarda la figura actual
    """
    if output_dir is None:
        return
    
    filepath = output_dir / f"{filename}.png"
    plt.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"Guardado: {filename}.png")

def plot_bar_charts_with_error(df, group_by='episodes', save_images=False, output_dir=None):
    """
    Genera gráficos de barras con barras de error (media ± std)
    """
    metrics = {
        'winrate': {'title': 'Evolución de win_rate según la cantidad de episodios de entrenamiento', 'ylabel': 'Winrate (%)', 'color': '#2E86AB'},
        'avg_returns': {'title': 'Average Returns por Grupo', 'ylabel': 'Average Returns', 'color': '#A23B72'},
        'avg_episode_steps': {'title': 'Average Episode Steps por Grupo', 'ylabel': 'Steps', 'color': '#F18F01'},
        'avg_win_steps': {'title': 'Average Win Steps por Grupo', 'ylabel': 'Win Steps', 'color': '#C73E1D'}
    }
    
    # Calcular estadísticas
    stats = calculate_group_statistics(df, group_by)
    
    for metric, config in metrics.items():
        plt.figure(figsize=(10, 6))
        
        # Extraer datos para el gráfico
        groups = stats.index
        means = stats[f'{metric}_mean']
        stds = stats[f'{metric}_std']
        counts = stats[f'{metric}_count']
        
        # Crear gráfico de barras con barras de error
        bars = plt.bar(range(len(groups)), means, yerr=stds, 
                      capsize=8, color=config['color'], alpha=0.8, 
                      edgecolor='black', linewidth=0.5,
                      error_kw={'elinewidth': 2, 'capthick': 2})
        
        # Personalización
        plt.title(config['title'], fontsize=16, fontweight='bold', pad=20)
        plt.ylabel(config['ylabel'], fontsize=14)
        plt.xlabel(group_by.replace('_', ' ').title(), fontsize=14)
        plt.xticks(range(len(groups)), [str(g) for g in groups])
        plt.grid(axis='y', alpha=0.3)
        
        # Añadir valores en las barras
        for i, (mean, std, count) in enumerate(zip(means, stds, counts)):
            plt.text(i, mean + std + (max(means) * 0.01), 
                    f'{mean:.1f}±{std:.1f}\n(n={count})', 
                    ha='center', va='bottom', fontweight='bold', fontsize=10)
        
        plt.tight_layout()
        save_figure(output_dir, f"bar_chart_{metric}_{group_by}")
        plt.show(block=False)

def plot_trend_lines(df, x_metric='episodes', save_images=False, output_dir=None):
    """
    Genera gráficos de líneas de tendencia
    """
    y_metrics = ['winrate', 'avg_returns', 'avg_episode_steps', 'avg_win_steps']
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
    
    # Gráfico combinado
    plt.figure(figsize=(12, 8))
    
    for i, (metric, color) in enumerate(zip(y_metrics, colors)):
        plt.subplot(2, 2, i+1)
        
        # Agrupar y calcular medias
        grouped = df.groupby(x_metric)[metric].agg(['mean', 'std']).reset_index()
        
        # Gráfico de línea con área de error
        plt.plot(grouped[x_metric], grouped['mean'], 'o-', color=color, linewidth=2, markersize=8)
        plt.fill_between(grouped[x_metric], 
                        grouped['mean'] - grouped['std'], 
                        grouped['mean'] + grouped['std'], 
                        alpha=0.3, color=color)
        
        plt.title(f'{metric.replace("_", " ").title()} vs {x_metric.title()}', 
                 fontsize=12, fontweight='bold')
        plt.xlabel(x_metric.replace('_', ' ').title(), fontsize=10)
        plt.ylabel(metric.replace('_', ' ').title(), fontsize=10)
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(output_dir, f"trend_lines_{x_metric}")
    plt.show(block=False)

def plot_boxplots(df, group_by='episodes', save_images=False, output_dir=None):
    """
    Genera boxplots para visualizar distribuciones completas
    """
    metrics = {
        'winrate': {'title': 'Distribución de Winrate', 'ylabel': 'Winrate (%)', 'color': '#2E86AB'},
        'avg_returns': {'title': 'Distribución de Average Returns', 'ylabel': 'Average Returns', 'color': '#A23B72'},
        'avg_episode_steps': {'title': 'Distribución de Episode Steps', 'ylabel': 'Steps', 'color': '#F18F01'},
        'avg_win_steps': {'title': 'Distribución de Win Steps', 'ylabel': 'Win Steps', 'color': '#C73E1D'}
    }
    
    for metric, config in metrics.items():
        plt.figure(figsize=(10, 6))
        
        # Crear boxplot
        box_plot = sns.boxplot(data=df, x=group_by, y=metric, 
                              color=config['color'], linewidth=2, fliersize=8)
        
        # Añadir puntos individuales
        #sns.stripplot(data=df, x=group_by, y=metric,  color='black', size=4, alpha=0.6)
        
        plt.title(config['title'], fontsize=16, fontweight='bold', pad=20)
        plt.ylabel(config['ylabel'], fontsize=14)
        plt.xlabel(group_by.replace('_', ' ').title(), fontsize=14)
        plt.grid(axis='y', alpha=0.3)
        
        # Añadir estadísticas en el gráfico
        for i, group in enumerate(df[group_by].unique()):
            group_data = df[df[group_by] == group][metric]
            median = group_data.median()
            plt.text(i, median, f'Med: {median:.1f}', ha='center', va='bottom', 
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        save_figure(output_dir, f"boxplot_{metric}_{group_by}")
        plt.show(block=False)


def plot_epsilon_comparison(df, save_images=False, output_dir=None):
    """
    Genera comparación específica por grupos de epsilon si está disponible
    """
    if 'epsilon_group' not in df.columns:
        print("No hay datos de epsilon para comparar")
        return
    
    epsilon_groups = sorted(df['epsilon_group'].unique())
    if len(epsilon_groups) < 2:
        print("Necesitas al menos 2 grupos de epsilon para comparar")
        return
    
    metrics = ['winrate', 'avg_returns']
    colors = ['#2E86AB', '#A23B72']
    
    plt.figure(figsize=(12, 5))
    
    for i, (metric, color) in enumerate(zip(metrics, colors)):
        plt.subplot(1, 2, i+1)
        
        # Preparar datos para gráfico de barras agrupadas
        epsilon_stats = df.groupby('epsilon_group')[metric].agg(['mean', 'std'])
        
        x = np.arange(len(epsilon_stats))
        
        bars = plt.bar(x, epsilon_stats['mean'], yerr=epsilon_stats['std'],
                      capsize=8, color=color, alpha=0.8, edgecolor='black',
                      error_kw={'elinewidth': 2, 'capthick': 2})
        
        plt.title(f'{metric.replace("_", " ").title()} por Epsilon', 
                 fontsize=14, fontweight='bold')
        plt.ylabel(metric.replace('_', ' ').title(), fontsize=12)
        plt.xlabel('Epsilon Final', fontsize=12)
        plt.xticks(x, [f'ε = {eps}' for eps in epsilon_stats.index])
        plt.grid(axis='y', alpha=0.3)
        
        # Añadir valores en las barras
        for j, (mean, std) in enumerate(zip(epsilon_stats['mean'], epsilon_stats['std'])):
            plt.text(j, mean + std + (max(epsilon_stats['mean']) * 0.01), 
                    f'{mean:.1f}±{std:.1f}', ha='center', va='bottom', 
                    fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    save_figure(output_dir, "epsilon_comparison")
    plt.show(block=False)


def main():
    """
    Función principal
    """
    parser = argparse.ArgumentParser(
        description="Análisis comparativo de resultados de Q-learning",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python compare_results.py
  python compare_results.py --data_dir data/processed --save_images
  python compare_results.py --group_by epsilon_group --save_images
        """
    )
    
    parser.add_argument(
        '--data_dir', 
        type=str, 
        default=None,
        help='Directorio con archivos CSV procesados'
    )
    
    parser.add_argument(
        '--group_by', 
        type=str, 
        default='episodes',
        choices=['episodes', 'epsilon_group', 'final_epsilon'],
        help='Variable para agrupar análisis'
    )
    
    parser.add_argument(
        '--save_images', 
        action='store_true',
        help='Guardar gráficos como imágenes PNG'
    )
    
    args = parser.parse_args()
    
    print("ANÁLISIS COMPARATIVO DE RESULTADOS Q-LEARNING")
    print("=" * 50)
    
    # Cargar datos
    print("\n1. Cargando datos...")
    df = load_processed_data(args.data_dir)
    if df is None:
        return False
    
    # Preparar datos
    print("\n2. Preparando datos para análisis...")
    df = prepare_data_for_analysis(df)
    if df is None:
        return False
    
    # Configurar salida
    print("\n3. Configurando directorio de salida...")
    output_dir = setup_output_directory(args.save_images)
    
    # Configurar estilo de matplotlib
    plt.style.use('seaborn-v0_8')
    plt.rcParams['figure.dpi'] = 100
    
    # Generar análisis
    print("\n4. Generando gráficos comparativos...")
    
    # Gráficos de barras con error
    print("   - Gráficos de barras con barras de error...")
    plot_bar_charts_with_error(df, args.group_by, args.save_images, output_dir)
    
    # Gráficos de tendencia
    print("   - Gráficos de líneas de tendencia...")
    if args.group_by == 'episodes':
        plot_trend_lines(df, 'episodes', args.save_images, output_dir)
    
    # Boxplots
    print("   - Boxplots de distribuciones...")
    plot_boxplots(df, args.group_by, args.save_images, output_dir)
    
    
    # Comparación por epsilon si está disponible
    print("   - Comparación por epsilon...")
    plot_epsilon_comparison(df, args.save_images, output_dir)
    
    if args.save_images:
        print(f"\nTodos los gráficos guardados en: {output_dir}")
    
    # Mantener gráficos abiertos
    print("\nGráficos generados. Presiona Enter para cerrar...")
    input()
    plt.close('all')
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)
    print("Análisis completado exitosamente!")