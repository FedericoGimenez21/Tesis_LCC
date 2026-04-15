# Diseño y desarrollo del trabajo.

Esta sección presenta la metodología general seguida para el diseño y la ejecución del trabajo experimental sobre NetSecGame. En primer lugar, se justifica la elección de un enfoque de aprendizaje por refuerzo con representación basada en características (*feature-based*), seleccionado por su capacidad de generalización y por reducir la dimensionalidad del espacio de estados frente a representaciones tabulares puras. En segundo término, se describe el flujo de preprocesamiento de datos. La interpretación de resultados se centra en el *win rate* como métrica principal de desempeño, entendido como la proporción de episodios en los que el agente alcanza el objetivo definido en el entorno bajo un presupuesto de pasos dado. Finalmente, se detallan las tecnologías y librerías utilizadas para implementar, automatizar y monitorear los experimentos.


# Representación de estados basada en características (Feature Based) para agente Q-Learning

En esta sección se presenta la modificación aplicada al algoritmo Q-Learning mediante la implementación de una representación de estados basada en características (*feature-based*) para mejorar el desempeño del agente en NetSecGame. La propuesta aborda las limitaciones del mapeo directo estado-identificador, introduciendo una abstracción que permite la generalización entre estados similares y reduce la complejidad del espacio de estados. 

Se postula que la implementación de una representación basada en características permitirá al agente Q-Learning:
- Generalizar el conocimiento adquirido entre estados funcionalmente equivalentes
- Reducir el tiempo de convergencia del algoritmo
- Mantener o mejorar la calidad de las políticas aprendidas

La transición hacia una representación basada en características no solo obedece a la necesidad de comprimir el espacio de estados, sino que constituye un prerrequisito estructural ineludible para posibilitar la aplicación integral de algoritmos genéticos en el aprendizaje y evolución de políticas. Bajo la representación directa original, la explosión combinatoria del espacio de estados tornaba computacionalmente prohibitivo que un individuo genético (cromosoma) lograra codificar una matriz estado-acción robusta y susceptible de ser entrenada.

Una vez establecida una representación adecuada y dimensionalmente controlable, el propósito recae en la aplicación de la metodología **ReLIEF** [29, 30]. Este es un enfoque metodológico propuesto recientemente para inicializar de forma informada la tabla Q (lo que previamente se definió como un enfoque de *warm-start*), apalancándose en las propiedades exploratorias de la computación y algoritmos evolutivos [31, 32, 33]. Este marco ha sido validado y adaptado exitosamente a problemas heurísticos complejos como los desafíos de autoescalado [34, 35, 36].

En este contexto, la idea central del trabajo adopta el marco ReLIEF para aplicar técnicas de computación evolutiva que exploren y evalúen políticas iniciales en el entorno simulado de ciberseguridad NetSecGame. Como resultado, se obtiene una tabla Q preentrenada que reduce la exploración inicial no informada y acelera el aprendizaje secuencial del agente atacante en NetSecGame.

## Arquitectura propuesta

La solución implementada consta de dos componentes principales:

- **Extractor de características (FeatureExtractor)**: módulo que toma el estado provisto por NetSecGame (originalmente expresado como una representación textual/estructurada del entorno) y lo transforma en un vector numérico de dimensión fija. Este vector resume, en forma de conteos agregados, la información relevante para la toma de decisiones (por ejemplo, para el caso de 4 subredes descubiertas, 10 hosts conocidos, 4 hosts controlados, 10 servicios observados y 3 datos encontrados, el vector resultante es [4, 10, 4, 10, 3]). 
    
    El vector de características definido captura cinco dimensiones fundamentales del estado del entorno:

    $$\mathbf{f}(s) = [n_{redes}, n_{hosts\_conocidos}, n_{hosts\_controlados}, n_{servicios}, n_{datos}]$$

    Donde:
    - $n_{redes}$: Cantidad de subredes descubiertas
    - $n_{hosts\_conocidos}$: Total de hosts identificados en el entorno  
    - $n_{hosts\_controlados}$: Número de hosts bajo control del atacante
    - $n_{servicios}$: Suma de servicios detectados en todos los hosts
    - $n_{datos}$: Total de elementos de datos encontrados

- **Agente Q-Learning modificado**: componente de aprendizaje que reemplaza el identificador de estado “literal” por el vector de características. En cada paso del episodio, el agente (i) obtiene el estado del entorno, (ii) calcula su representación feature-based, (iii) utiliza ese vector como clave de estado en la Q-table y (iv) selecciona y ejecuta una acción según su política, actualizando luego $Q(s,a)$ en función de la recompensa y el siguiente estado.

En términos operativos, el flujo puede resumirse como: 

**NetSecGame → estado → FeatureExtractor → vector de características → Q-table/política → acción → NetSecGame**. 

Esta separación permite desacoplar la lógica de representación del estado de la lógica de aprendizaje, y habilita el uso de estrategias de *warm-start* (como ReLIEF) para inicializar la Q-table de manera informada antes del entrenamiento en línea.

---

## Preprocesamiento de datos

Tras la integración de la representación basada en características (feature-based), la fase de preprocesamiento se centró en la preparación de los componentes fundamentales para la construcción de las tablas Q que serían sometidas a optimización. El objetivo principal de esta etapa es definir con precisión las dimensiones de la matriz (el conjunto de estados y acciones) para que el framework de optimización —orquestado mediante la integración de SMAC y pymoo— pueda generar, poblar y evolucionar las políticas candidatas de manera estructurada.

La conformación de este espacio de búsqueda se dividió en dos procesos de extracción diferenciados:

- Extracción del Espacio de Estados: La recopilación de los estados factibles se llevó a cabo mediante un módulo de desarrollo propio. Este componente analiza y extrae los estados empíricamente visitados a partir de una tabla Q de referencia, la cual fue generada previamente mediante ejecuciones estándar del algoritmo Q-Learning. Este enfoque garantiza que el optimizador trabaje exclusivamente sobre estados relevantes y alcanzables dentro del entorno.

- Mapeo del Espacio de Acciones: Para definir el conjunto de acciones disponibles, se integró el componente WhiteBoxNSGCoordinator. Esta extensión del entorno NetSecGame opera bajo un enfoque de caja blanca, proporcionando visibilidad total sobre las mecánicas subyacentes y permitiendo extraer un listado exhaustivo de todas las acciones legales y posibles para cada agente registrado en la simulación.


## Herramientas y tecnologías utilizadas 

En esta sección se detallan las herramientas de software adoptadas para el desarrollo experimental. La selección tecnológica se fundamentó en la necesidad de garantizar la interoperabilidad con el framework principal, NetSecGame, y asegurar una implementación eficiente. Se adoptó Python como lenguaje de programación central debido a su robusta compatibilidad con el entorno de simulación y su extenso ecosistema orientado a la optimización computacional.

1. Entorno de Desarrollo y Gestión de Proyecto

- Visual Studio Code: Empleado como entorno de desarrollo integrado (IDE) principal para la codificación, estructuración y depuración del proyecto.

- Git y GitHub: Implementados como sistema de control de versiones y repositorio remoto, respectivamente, garantizando la trazabilidad y el resguardo de la evolución del código fuente.

- Conda: Utilizado para la creación y administración de entornos virtuales, asegurando el aislamiento de las dependencias y la reproducibilidad del entorno de ejecución.

2. Lenguaje Base y Librerías del Sistema

El proyecto fue desarrollado utilizando Python (versión 3.12.0). Para la gestión a nivel de sistema e interacción con el intérprete se integraron las siguientes librerías estándar:

- sys y subprocess: Utilizados para el control de la ejecución del proceso, manejo de interrupciones y la invocación de comandos del sistema operativo subyacente.

- argparse: Implementado para la gestión e ingesta dinámica de argumentos mediante línea de comandos.

- time: Empleado para la medición precisa de los tiempos de ejecución de los algoritmos.

- pickle: Encargado de la serialización y deserialización de estructuras de datos persistentes, fundamentalmente para guardar y cargar las Q-tables resultantes de los entrenamientos.

3. Computación Científica y Lógica de Aprendizaje

- numpy: Principal motor para la ejecución eficiente de cálculos matriciales, numéricos y estadísticos.
- random: Utilizado para la generación de números pseudoaleatorios, una pieza fundamental en la implementación de la política de exploración $\epsilon$-greedy.

4. Frameworks de Optimización

- SMAC y ConfigSpace: Integrados en conjunto para llevar a cabo la optimización bayesiana de los hiperparámetros del modelo.

- pymoo: Utilizado como framework de optimización heurística para la ejecución de un algoritmo genético enfocado en la mejora de las políticas (Q-tables).

5. Monitorización y Visualización de Resultados

- logging: Configurado para generar un registro detallado de los eventos de ejecución y depuración.

- mlflow: Implementado para la monitorización avanzada, permitiendo el registro, seguimiento y comparación de métricas y parámetros a lo largo de los distintos experimentos.

- matplotlib: Herramienta encargada de la generación de gráficas 2D para el análisis visual de los resultados obtenidos.
---


## Recursos de Hardware

La ejecución de las fases de entrenamiento, optimización de hiperparámetros y validación fue posible gracias a la infraestructura de cómputo de alto rendimiento provista por el Laboratorio de Sistemas Inteligentes (LABSIN https://labsin.org/es.html). El uso de estos recursos especializados garantizó la continuidad operativa de las pruebas, permitiendo mantener ejecuciones prolongadas y estables bajo cargas de procesamiento intensivas. Las especificaciones técnicas del nodo de cómputo utilizado se detallan en la Tabla N.

| Componente | Descripción | 
|----------|----------|
| Procesador | Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz |
| Sistema Operativo | Ubuntu 20.04.6 LTS |
| GPU | NVIDIA GeForce GTX 1080 Ti |
| Memoria RAM | 64GB |


