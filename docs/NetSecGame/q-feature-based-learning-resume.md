# Resumen: Q-Learning basado en características para NetSecGame

Este trabajo presenta una modificación al algoritmo Q-Learning tradicional mediante la implementación de una representación de estados basada en características (feature-based) para mejorar el desempeño del agente en el entorno NetSecGame. La propuesta busca abordar las limitaciones del mapeo directo estado-identificador, introduciendo una abstracción que permita la generalización entre estados similares y reduzca la complejidad del espacio de estados.

La metodología implementada consta de dos componentes principales: un `FeatureExtractor` que transforma la representación textual compleja del estado del entorno en un vector de características numéricas de dimensión fija, y un agente `Q-Learning-feature-based` que utiliza este vector como identificador de estado. El vector de características captura cinco dimensiones fundamentales: número de redes descubiertas, hosts conocidos, hosts controlados, servicios detectados y elementos de datos encontrados, representado matemáticamente como 

$$\mathbf{f}(s) = [n_{redes}, n_{hosts\_conocidos}, n_{hosts\_controlados}, n_{servicios}, n_{datos}]$$

Donde:
- $n_{redes}$: Cantidad de subredes descubiertas
- $n_{hosts\_conocidos}$: Total de hosts identificados en el entorno  
- $n_{hosts\_controlados}$: Número de hosts bajo control del atacante
- $n_{servicios}$: Suma de servicios detectados en todos los hosts
- $n_{datos}$: Total de elementos de datos encontrados

Los experimentos se realizaron utilizando un modelo de agente entrenado durante 15,000 episodios sobre el `scenario1`, el cual alcanzó un rendimiento de 100% de `winrate` en 6000 episodios. El mismo modelo entrenado fue evaluado en dos configuraciones diferentes de testing para analizar su capacidad de generalización.

En el **Experimento de testing 1** con mismo entorno estático (direcciones IP y topología fijas), el modelo alcanzó un rendimiento perfecto con 100% de winrate, completando todos los episodios en exactamente 5 pasos con reward de 1000.

El **Experimento de testing 2** utilizó un entorno dinámico con direcciones IP modificadas aleatoriamente al inicio de cada episodio con el mismo modelo entrenado. Los resultados mostraron una dramática caída en el rendimiento: solo 5.427% de winrate (814 victorias de 15,000 episodios), con un reward promedio de -40.307 y episodios de 98.426 pasos en promedio. Esta diferencia abismal entre ambos experimentos evidencia una limitación fundamental en el enfoque propuesto.

La interpretación de los resultados revela dos problemas críticos: sobreespecificación del vector de características que mantiene un nivel de granularidad que impide la generalización efectiva, y memorización versus aprendizaje, donde el agente memoriza configuraciones específicas en lugar de aprender patrones generalizables. El desempeño perfecto en el entorno estático contrastado con el bajo desempeño en el entorno dinámico confirma esta hipótesis.
