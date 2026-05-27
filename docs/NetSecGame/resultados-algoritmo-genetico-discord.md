# Resumen de resultados del algoritmo genético relevados desde Discord

## Fuente

Este documento resume mensajes recuperados desde el canal de Discord de la tesis mediante `Tesis_LCC/src/utils/discord_channel_query.py`, buscando términos como `genet`, `genético`, `SMAC`, `hiper`, `win_rate` y `Q-table`.

## Objetivo de los experimentos

El objetivo del algoritmo genético fue generar o mejorar una Q-table inicial para el agente de Q-learning en NetSecGame. La idea general fue usar una política/Q-table evolucionada como punto de partida informado, intentando mejorar el desempeño frente a una inicialización aleatoria o no informada.

La métrica principal utilizada fue el `win_rate` del agente.

## Primera prueba funcional del algoritmo genético

En diciembre de 2025 se reportó la primera prueba funcional del algoritmo genético sobre `scenario_small`.

Configuración usada:

- Crossover: *Simulated Binary Crossover*.
  - `crossover_prob = 0.8`
  - `eta = 15`
- Mutación: *Polynomial Mutation*.
  - `mutation_prob = 0.0005`
  - `eta = 20`
- Población: 20 individuos.
- Generaciones: 10.
- Evaluación de cada individuo: 250 episodios en modo testing, sin entrenamiento adicional.
- Métrica optimizada: `win_rate`.
- Tiempo de ejecución aproximado: 9 horas.

Se observó que el algoritmo era funcional, pero los `win_rate` obtenidos eran bajos. Desde esta primera prueba se planteó que era necesario optimizar los hiperparámetros del genético.

## Problema de escala de la Q-table

Se mencionó que la representación evaluada involucraba aproximadamente:

- 860 estados.
- 1600 acciones.
- Alrededor de 1,3 millones de valores en la Q-table.

Esto hizo que la elección de la probabilidad de mutación fuera delicada. Una recomendación estándar de `1/L` daría una probabilidad aproximada de `0.00000072`, considerada demasiado baja para el experimento. Por eso se usó una mutación mayor (`0.0005`), aunque cuidando no destruir la estructura de la Q-table.

## Optimización de hiperparámetros con SMAC3

Durante enero/febrero de 2026 se discutió la optimización de hiperparámetros. Se descartó el análisis de sensibilidad con Sobol/Saltelli por su alto costo computacional y se decidió usar **SMAC3** como optimizador del algoritmo evolutivo.

La arquitectura experimental quedó planteada en dos niveles:

1. **SMAC3** propone configuraciones de hiperparámetros del algoritmo genético.
2. El **algoritmo genético** evoluciona Q-tables bajo esa configuración.
3. Cada Q-table se evalúa en NetSecGame.
4. El `win_rate` obtenido se devuelve a SMAC3 como función objetivo.

Se aclaró que un `trial` corresponde a una ejecución completa del genético con una configuración dada de hiperparámetros.

## Pruebas cortas de SMAC/genético

En febrero de 2026 se reportó una prueba con:

- `population_size` entre `[2, 10]`.
- `n_generations` entre `[2, 6]`.
- `test_episodes = 25`.
- 13 trials.
- Un solo proceso.

Tiempo aproximado: 2 horas y 20 minutos.

Esto confirmó que incluso búsquedas reducidas eran costosas. También se mencionó que se planeaba implementar multiprocesamiento para acelerar las evaluaciones.

## Ejecución larga de SMAC

Posteriormente se ejecutó SMAC con:

- Timeout por trial: 1 día.
- Timeout total: 7 días.

Durante la ejecución se detectó un problema: aunque había individuos con `win_rate` mayor a 20%, el sistema no registraba correctamente mejores valores y el mejor `win_rate` figuraba como 0%. Se sospechó un error asociado a timeouts o configuración, y se planteó la necesidad de debuggear y volver a ejecutar.

Luego se reportaron resultados tras aproximadamente 10 días de ejecución:

- Solo 3 trials se completaron correctamente.
- Los demás no se completaron por timeout.
- Los hiperparámetros no variaron demasiado, probablemente porque hubo muy pocos trials válidos.

Esto limitó fuertemente la capacidad de SMAC para encontrar una configuración adecuada.

## Prueba con host controlado inicial fijo

En mayo de 2026 se probó una modificación en la configuración inicial del entorno: usar un host controlado inicial fijo en lugar de `random`.

La hipótesis era que esta configuración podía mejorar el rendimiento del genético.

Resultados reportados:

- Configuración anterior: aproximadamente 11,2% de `win_rate`.
- Configuración con host inicial fijo: aproximadamente 10,4% de `win_rate`.

La modificación no produjo una mejora. Luego se tomó la mejor Q-table y se evaluó en testing durante 6.000 y 15.000 episodios, obteniendo nuevamente valores cercanos al 5%, similares a random.

## Verificación posterior con entrenamiento adicional

Para comprobar si el problema era la Q-table o el agente, se tomó la mejor Q-table generada por el genético y se la entrenó con la configuración random durante 15.000 episodios.

Resultado:

- 100% de `win_rate` en training.
- 100% de `win_rate` en testing durante 15.000 episodios.

Esto sugiere que la Q-table/representación y el agente pueden alcanzar muy buen desempeño si reciben entrenamiento suficiente. Por lo tanto, los resultados bajos del genético no parecen deberse a una imposibilidad estructural del agente, sino a la configuración y presupuesto de la búsqueda evolutiva.

## Interpretación general

Los resultados muestran que el algoritmo genético fue implementado correctamente y que el enfoque tiene potencial, pero las ejecuciones realizadas no lograron mejorar de forma robusta al agente random o al Q-learning base sin entrenamiento adicional.

Las causas probables son:

1. **Presupuesto insuficiente por individuo**: muchas búsquedas se realizaron con pocos episodios por individuo, por ejemplo 25 episodios, debido al costo computacional.
2. **Pocos trials efectivos**: en la ejecución larga solo 3 trials terminaron correctamente.
3. **Timeouts frecuentes**: varios trials quedaron truncados por límites de tiempo.
4. **Hiperparámetros no suficientemente explorados**: SMAC tuvo poca evidencia útil para aprender buenas configuraciones.
5. **Alta variabilidad del entorno/evaluación**: se observó que evaluaciones cortas pueden no representar correctamente el desempeño real de una Q-table.
6. **Costo computacional elevado**: evaluar muchas Q-tables en NetSecGame es caro, especialmente con poblaciones, generaciones y episodios suficientes.

## Conclusión

El algoritmo genético no produjo, en los experimentos reportados, una mejora clara sobre el desempeño random o Q-learning base cuando se usó directamente la mejor Q-table evolucionada. Sin embargo, al entrenar posteriormente la mejor Q-table durante 15.000 episodios, se alcanzó 100% de `win_rate` tanto en training como en testing.

Por lo tanto, la conclusión más razonable es que el enfoque evolutivo no queda descartado conceptualmente. Los resultados negativos se explican principalmente por limitaciones de presupuesto computacional, pocos trials válidos y una optimización de hiperparámetros insuficiente. Para evaluar adecuadamente el potencial del método sería necesario repetir la búsqueda con más individuos, más generaciones, más episodios por individuo, mejor manejo de timeouts y posiblemente paralelización.
