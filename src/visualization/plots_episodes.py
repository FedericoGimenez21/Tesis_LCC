import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import argparse

def load_and_process_data(csv_file_path):
    """
    Carga y procesa los datos para análisis de winrate
    """
    try:
        df = pd.read_csv(csv_file_path)
        print(f"Datos cargados: {len(df)} registros")
        
        # Filtrar solo test checkpoints
        df_checkpoints = df[df['data_type'] == 'test_checkpoint'].copy()
        print(f"Checkpoints de prueba: {len(df_checkpoints)} registros")
        
        return df_checkpoints
    except Exception as e:
        print(f"Error cargando datos: {e}")
        return None

def calculate_winrate_statistics(df):
    """
    Calcula estadísticas de winrate por grupos de episodios
    """
    # Agrupar por training_episodes y calcular estadísticas
    stats = df.groupby('training_episodes')['winrate'].agg([
        'count',
        'mean',
        'std',
        'min',
        'max',
        'median'
    ]).round(3)
    
    stats.columns = ['Num_Runs', 'Mean_Winrate', 'Std_Winrate', 'Min_Winrate', 'Max_Winrate', 'Median_Winrate']
    
    print("\n ESTADÍSTICAS DE WINRATE POR EPISODIOS DE ENTRENAMIENTO")
    print("=" * 70)
    print(stats)
    
    # Encontrar el mejor resultado
    best_episode = stats['Mean_Winrate'].idxmax()
    best_winrate = stats.loc[best_episode, 'Mean_Winrate']
    
    print(f"\n MEJOR RENDIMIENTO:")
    print(f"   Episodios: {best_episode}")
    print(f"   Winrate promedio: {best_winrate:.2f}%")
    print(f"   Desviación estándar: {stats.loc[best_episode, 'Std_Winrate']:.2f}%")
    print(f"   Rango: [{stats.loc[best_episode, 'Min_Winrate']:.1f}% - {stats.loc[best_episode, 'Max_Winrate']:.1f}%]")
    
    return stats

def create_winrate_plots(df, save_images=False, output_dir=None):
    """
    Crea gráficos de análisis de winrate
    """
    # Configurar estilo
    plt.style.use('seaborn-v0_8')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    
    # Colores
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#7209B7', '#0C7C59', '#8B5A2B', '#6A0136']
    
    # 1. GRÁFICO DE BARRAS - Winrate promedio por episodios
    plt.figure(figsize=(14, 8))
    
    # Calcular promedios y errores estándar
    grouped = df.groupby('training_episodes')['winrate'].agg(['mean', 'std', 'count']).reset_index()
    grouped['se'] = grouped['std'] / np.sqrt(grouped['count'])  # Error estándar
    
    # Crear gráfico de barras (corregido)
    bars = plt.bar(range(len(grouped)), grouped['mean'], 
                   color=colors[:len(grouped)], alpha=0.8, 
                   edgecolor='black', linewidth=1.5)
    
    # Añadir barras de error manualmente
    plt.errorbar(range(len(grouped)), grouped['mean'], 
                yerr=grouped['se'], fmt='none', capsize=8, capthick=2, 
                ecolor='black', elinewidth=2)
    
    # Personalizar gráfico
    plt.title('Winrate promedio por episodios de entrenamiento\n(barras de error muestran error estándar)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Winrate promedio (%)', fontsize=14, fontweight='bold')
    plt.xlabel('Episodios de entrenamiento', fontsize=14, fontweight='bold')
    
    # Configurar etiquetas del eje X
    plt.xticks(range(len(grouped)), grouped['training_episodes'], rotation=45)
    
    # Añadir valores en las barras
    for i, (bar, value, std, count) in enumerate(zip(bars, grouped['mean'], grouped['std'], grouped['count'])):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + grouped.iloc[i]['se'] + 0.1,
                f'{value:.1f}%\n(n={count})', 
                ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    if save_images and output_dir:
        plt.savefig(output_dir / "winrate_01_bars_by_episodes.png", dpi=300, bbox_inches='tight')
        print("Guardado: winrate_01_bars_by_episodes.png")
    
    plt.show(block=False)
    
    # 2. GRÁFICO DE CAJAS (BOXPLOT) - Distribución de winrate por episodios
    plt.figure(figsize=(14, 8))
    
    # Crear boxplot
    episodes_list = sorted(df['training_episodes'].unique())
    data_for_boxplot = [df[df['training_episodes'] == ep]['winrate'].values for ep in episodes_list]
    
    box_plot = plt.boxplot(data_for_boxplot, labels=episodes_list, patch_artist=True,
                          boxprops=dict(linewidth=2), whiskerprops=dict(linewidth=2),
                          capprops=dict(linewidth=2), medianprops=dict(linewidth=3, color='red'))
    
    # Colorear las cajas
    for patch, color in zip(box_plot['boxes'], colors[:len(episodes_list)]):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Personalizar gráfico
    plt.title('Distribución de Winrate por episodios de entrenamiento', 
              fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Winrate (%)', fontsize=14, fontweight='bold')
    plt.xlabel('Episodios de entrenamiento', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Añadir información estadística
    for i, ep in enumerate(episodes_list):
        ep_data = df[df['training_episodes'] == ep]['winrate']
        median_val = ep_data.median()
        plt.text(i+1, median_val + 0.3, f'Med: {median_val:.1f}%', 
                ha='center', va='bottom', fontweight='bold', fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    
    if save_images and output_dir:
        plt.savefig(output_dir / "winrate_02_boxplot_by_episodes.png", dpi=300, bbox_inches='tight')
        print("Guardado: winrate_02_boxplot_by_episodes.png")
    
    plt.show(block=False)
    
    # 3. TABLA RESUMEN con visualización
    plt.figure(figsize=(12, 6))
    plt.axis('tight')
    plt.axis('off')
    
    # Preparar datos para la tabla
    table_data = []
    for ep in sorted(df['training_episodes'].unique()):
        ep_data = df[df['training_episodes'] == ep]['winrate']
        table_data.append([
            f"{ep:,}",
            f"{len(ep_data)}",
            f"{ep_data.mean():.2f}",
            f"{ep_data.std():.2f}",
            f"{ep_data.min():.1f}",
            f"{ep_data.max():.1f}",
            f"{ep_data.median():.1f}"
        ])
    
    table = plt.table(cellText=table_data,
                     colLabels=['Episodios', 'Runs', 'Media (%)', 'Std (%)', 'Min (%)', 'Max (%)', 'Mediana (%)'],
                     cellLoc='center', loc='center')
    
    # Estilizar tabla
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 2)
    
    # Colorear header
    for i in range(len(table_data[0])):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Colorear filas alternadamente
    for i in range(1, len(table_data) + 1):
        for j in range(len(table_data[0])):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#F0F0F0')
    
    plt.title('Resumen estadístico de Winrate por episodios de entrenamiento', 
              fontsize=14, fontweight='bold', pad=30)
    
    if save_images and output_dir:
        plt.savefig(output_dir / "winrate_03_summary_table.png", dpi=300, bbox_inches='tight')
        print("Guardado: winrate_03_summary_table.png")
    
    plt.show(block=False)

def main():
    """
    Función principal para análisis de winrate
    """
    parser = argparse.ArgumentParser(description="Análisis de Winrate por Episodios de Entrenamiento")
    parser.add_argument('--input', '-i', required=True, help='Archivo CSV con datos procesados')
    parser.add_argument('--save', '-s', action='store_true', help='Guardar imágenes')
    parser.add_argument('--output_dir', '-o', help='Directorio de salida para imágenes')
    
    args = parser.parse_args()
    
    print("ANÁLISIS DE WINRATE - Q-LEARNING")
    print("=" * 50)
    
    # Cargar datos
    df = load_and_process_data(args.input)
    if df is None:
        return
    
    # Calcular estadísticas
    stats = calculate_winrate_statistics(df)
    
    # Configurar directorio de salida
    output_dir = None
    if args.save:
        if args.output_dir:
            output_dir = Path(args.output_dir)
        else:
            base_path = Path(__file__).parent.parent.parent
            output_dir = base_path / "outputs" / "figures" / "winrate_analysis"
        
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"\nDirectorio de salida: {output_dir}")
    
    # Crear gráficos
    print(f"\n GENERANDO VISUALIZACIONES...")
    create_winrate_plots(df, args.save, output_dir)
    
    if args.save:
        print(f"\n Imágenes guardadas en: {output_dir}")
    
    # Mantener gráficos abiertos
    input("\nPresiona Enter para cerrar los gráficos...")
    plt.close('all')

if __name__ == "__main__":
    main()