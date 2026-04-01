# Índice

- [Inteligencia Artificial](#inteligencia-artificial)
  - [Algoritmos Genéticos](#algoritmos-genéticos)
    - [Fundamentos y definición](#fundamentos-y-definición)
    - [Ciclo evolutivo](#ciclo-evolutivo)
    - [Teorema del esquema y convergencia](#teorema-del-esquema-y-convergencia)
    - [Representación y codificación](#representación-y-codificación)
    - [Ventajas y limitaciones](#ventajas-y-limitaciones)
    - [Complementariedad entre Algoritmos Genéticos y Aprendizaje por Refuerzo](#complementariedad-entre-algoritmos-genéticos-y-aprendizaje-por-refuerzo)
- [Q-learning](#q-learning)
  - [Ecuacion de actualizacion de Q-learning](#ecuacion-de-actualizacion-de-q-learning)
  - [Técnicas principales de inicialización de Q-tables](#técnicas-principales-de-inicialización-de-q-tables)
    - [Inicialización a ceros](#inicialización-a-ceros)
    - [Inicialización con valores aleatorios](#inicialización-con-valores-aleatorios)
    - [Inicialización optimista](#inicialización-optimista)
    - [Inicialización mediante evolución de políticas](#inicialización-mediante-evolución-de-políticas)
- [Optimización de Hiperparámetros y Optimización Bayesiana en Algoritmos Genéticos](#optimización-de-hiperparámetros-y-optimización-bayesiana-en-algoritmos-genéticos)
  - [Introducción a la Meta-Optimización y Algoritmos Genéticos](#1-introducción-a-la-meta-optimización-y-algoritmos-genéticos)
  - [El Problema de la Optimización de Hiperparámetros](#2-el-problema-de-la-optimización-de-hiperparámetros)
    - [Definición formal](#21-definición-formal)
    - [Hiperparámetros vs. parámetros](#22-hiperparámetros-vs-parámetros)
  - [Hiperparámetros Críticos de los Algoritmos Genéticos](#3-hiperparámetros-críticos-de-los-algoritmos-genéticos)
    - [Tamaño de la población ($N$)](#31-tamaño-de-la-población-n)
    - [Tasa de cruce ($p_c$)](#32-tasa-de-cruce-p_c)
    - [Tasa de mutación ($p_m$)](#33-tasa-de-mutación-p_m)
    - [Número de generaciones](#34-número-de-generaciones-g)
    - [Método y presión de selección](#35-método-y-presión-de-selección)
    - [Interdependencia de hiperparámetros](#36-interdependencia-de-hiperparámetros)
  - [4. Métodos Clásicos de Optimización de Hiperparámetros](#4-métodos-clásicos-de-optimización-de-hiperparámetros)
    - [Búsqueda manual y ensayo-error](#41-búsqueda-manual-y-ensayo-error)
    - [4.2 Búsqueda por cuadrícula (Grid Search)](#42-búsqueda-por-cuadrícula-grid-search)
    - [4.3 Búsqueda aleatoria (Random Search)](#43-búsqueda-aleatoria-random-search)
  - [5. Optimización Bayesiana](#5-optimización-bayesiana)
    - [5.1 Fundamento conceptual](#51-fundamento-conceptual)
    - [5.2 Formulación del marco SMBO](#52-formulación-del-marco-smbo)
    - [5.3 Modelos sustitutos (*Surrogate Models*)](#53-modelos-sustitutos-surrogate-models)
    - [5.4 Funciones de adquisición](#54-funciones-de-adquisición)
  - [6. Optimización Bayesiana Aplicada a Algoritmos Genéticos](#6-optimización-bayesiana-aplicada-a-algoritmos-genéticos)
    - [6.1 Motivación específica](#61-motivación-específica)
    - [6.2 Formulación del problema de meta-optimización](#62-formulación-del-problema-de-meta-optimización)
    - [6.3 Flujo de trabajo propuesto](#63-flujo-de-trabajo-propuesto)
- [Análisis de Sensibilidad Global: Métodos de Sobol y Saltelli](#análisis-de-sensibilidad-global-métodos-de-sobol-y-saltelli)
  - [1. Introducción al Análisis de Sensibilidad Global](#1-introducción-al-análisis-de-sensibilidad-global)
    - [1.1 Definición Formal](#11-definición-formal)
  - [2. Método de Sobol (Índices de Sensibilidad Basados en Varianza)](#2-método-de-sobol-índices-de-sensibilidad-basados-en-varianza)
    - [2.1 Fundamento Teórico](#21-fundamento-teórico)
    - [2.2 Descomposición de la Varianza](#22-descomposición-de-la-varianza)
    - [2.3 Índices de Sobol de Primer Orden ($S_i$)](#23-índices-de-sobol-de-primer-orden-s_i)
    - [2.4 Índices de Sobol Totales ($S_{Ti}$)](#24-índices-de-sobol-totales-s_ti)
    - [2.5 Índices de Segundo Orden ($S_{ij}$)](#25-índices-de-segundo-orden-s_ij)
  - [3. Método de Muestreo de Saltelli](#3-método-de-muestreo-de-saltelli)
    - [3.1 El Problema del Costo Computacional](#31-el-problema-del-costo-computacional)
- [NetSecGame: Caracterización del entorno y fundamentos de su selección para esta tesis](#netsecgame-caracterización-del-entorno-y-fundamentos-de-su-selección-para-esta-tesis)
  - [Características](#características)
    - [Objetivo del simulador](#objetivo-del-simulador)
    - [Características principales](#características-principales)
  - [¿Cómo funciona?](#cómo-funciona)
    - [Arquitectura general](#arquitectura-general)
    - [Modo de uso](#modo-de-uso)
  - [¿Por qué fue creado?](#por-qué-fue-creado)
    - [Problemas que busca resolver](#problemas-que-busca-resolver)
    - [Ventajas distintivas de NetSecGame](#ventajas-distintivas-de-netsecgame)
    - [Fundamentación en la literatura reciente](#fundamentación-en-la-literatura-reciente)
    - [Usos principales](#usos-principales)
  - [Justificación de su elección para esta tesis](#justificación-de-su-elección-para-esta-tesis)
  - [Arquitectura](#arquitectura)
    - [Componentes del juego](#componentes-del-juego)
  - [Estructura del estado](#estructura-del-estado)
  - [Dinámica de actualización](#dinámica-de-actualización)
  - [Complejidad del espacio de estados](#complejidad-del-espacio-de-estados)
  - [Sistema de recompensas](#sistema-de-recompensas)
  - [Selección y especificación de scenario1-full](#selección-y-especificación-de-scenario1-full)
- [Anexos](#anexos)
    - [Anexo A: netsecenv_conf.yaml](#anexo-a-netsecenv_confyaml)
    - [Anexo B: netsecenv_conf_dynamic.yaml](#anexo-b-netsecenv_conf_dynamicyaml)
- [Referencias Bibliográficas](#referencias-bibliográficas)

# Inteligencia Artificial

De acuerdo con Stuart Russell y Peter Norvig [1], la Inteligencia Artificial se define formalmente como la disciplina de la ciencia de la computación que estudia el diseño, la implementación y la evaluación de agentes racionales.

En este contexto, un agente se define como un sistema computacional que:

- **Percibe** su entorno a través de sensores.

- **Ejecuta** acciones sobre dicho entorno mediante actuadores.

- Opera de forma **autónoma** para cumplir un objetivo designado.

La contribución central de este enfoque no es la simple imitación del pensamiento o comportamiento humano (un estándar difícil de medir y no siempre óptimo), sino la racionalidad. Un agente es considerado racional si, para cualquier secuencia de percepciones dada, selecciona la acción que se espera maximice su medida de rendimiento (o función de utilidad). Esta decisión se fundamenta en la evidencia provista por la secuencia de percepciones y en cualquier conocimiento previo que el agente posea.

Este enfoque en la "racionalidad de la acción" proporciona el fundamento teórico directo para el Aprendizaje por Refuerzo (reinforcement learning).

Como muestra la Figura 1, el Aprendizaje Automático (Machine Learning) es un subcampo de la IA que estudia la capacidad de mejorar el rendimiento basándose en la experiencia. Según la definición canónica de Tom M. Mitchell [2], el Aprendizaje Automático se define de la siguiente manera: "Se dice que un programa de computadora aprende de la experiencia E con respecto a alguna clase de tareas T y una medida de rendimiento P, si su rendimiento en las tareas T, medido por P, mejora con la experiencia E". El Aprendizaje por Refuerzo es un subcampo del Aprendizaje Automático que aborda precisamente el problema de cómo un agente debe actuar en un entorno para maximizar una noción de recompensa acumulativa, constituyendo así una implementación concreta del paradigma del agente racional en entornos secuenciales de decisión. De acuerdo con Sutton y Barto [3], el Aprendizaje por Refuerzo (RL) es un enfoque computacional para el aprendizaje basado en la interacción. 

![ai_hierarchy](../images/q-learning.drawio.png)
*Figura 1: Jerarquía de inteligencia artificial, aprendizaje automático, aprendizaje por refuerzo y q-learning.*

A diferencia de otros paradigmas de aprendizaje automático, un agente de RL no recibe instrucciones sobre qué acciones tomar, sino que debe descubrir mediante prueba y error qué acciones producen la mayor recompensa, aprendiendo a mapear situaciones en acciones para maximizar una señal de recompensa numérica.


Para formalizar matemáticamente el problema de la toma de decisiones secuencial que el Aprendizaje por Refuerzo aborda, se utiliza el marco de los Procesos de Decisión de Markov (Markov Decision Problems, MDPs).

Un MDP es un modelo estocástico de control en tiempo discreto que formaliza la interacción entre el agente y el entorno. Prácticamente todos los problemas de RL pueden ser enmarcados como un MDP [3].

Un MDP se define formalmente como una 5-tupla $(S, A, P, R, \gamma)$:
- $S$ (Estados): Un conjunto finito de estados que el agente puede percibir.
- $A$ (Acciones): Un conjunto finito de acciones que el agente puede ejecutar.
- $P$ (Función de Transición): La dinámica del entorno, o el "modelo" (previamente mencionado). Define la probabilidad de transitar al estado $s'$ después de tomar la acción $a$ en el estado $s$. Se expresa como:$$P(s' | s, a) = \Pr(S_{t+1} = s' | S_t = s, A_t = a)$$
- $R$ (Función de Recompensa): Especifica la recompensa $R_t$ que el agente recibe. Formalmente, es el valor esperado de la recompensa al transitar al estado $s'$ desde el estado $s$ tomando la acción $a$.
- $\gamma$ (Factor de Descuento): Un escalar $0 \le \gamma \le 1$ que pondera la importancia de las recompensas futuras frente a las inmediatas.

La característica que define este marco es la Propiedad de Markov. Un entorno posee esta propiedad si las transiciones y recompensas futuras dependen únicamente del estado actual $S_t$ y la acción $A_t$, y no de la secuencia de eventos pasados que condujeron a ese estado. En un MDP, el estado $S_t$ es una representación suficiente de toda la historia del agente.

Según Sutton y Barto, casi todos los problemas de RL pueden formalizarse utilizando cuatro componentes esenciales que interactúan entre sí:

1. **Política** (Policy): Define el comportamiento del agente en un momento dado. Es una correspondencia (o mapeo) entre los estados percibidos del entorno y las acciones a tomar en dichos estados.
2. **Señal de recompensa** (Reward Signal): Es la base del objetivo del agente. En cada paso de tiempo, el entorno envía al agente un número escalar $R_t$ (la recompensa). El objetivo único del agente es maximizar la recompensa acumulativa total a largo plazo. La señal de recompensa define qué eventos son "buenos" y "malos" para el agente de manera inmediata.
3. **Función de valor** (Value Function): Mientras que la recompensa indica lo que es bueno en el sentido inmediato, la función de valor especifica lo que es bueno a largo plazo. El valor de un estado, es la recompensa total acumulada que el agente espera recibir en el futuro, comenzando desde ese estado. Las funciones de valor son predicciones de recompensas futuras y son cruciales para tomar decisiones, ya que gestionan la disyuntiva entre la ganancia a corto y largo plazo. 
4. **Modelo** (Model, opcional): Es una representación interna que el agente tiene del entorno. Un modelo simula el comportamiento del entorno, permitiendo al agente predecir el próximo estado y la próxima recompensa basándose en el estado actual y la acción tomada. El algoritmo Q-learning, pilar de esta investigación, pertenece precisamente a esta categoría, operando como un método libre de modelo diseñado para estimar la función de valor óptima.

---

## Algoritmos Genéticos

### Fundamentos y definición

Los Algoritmos Genéticos (GA, *Genetic Algorithms*) constituyen una familia de metaheurísticas de optimización inspiradas en los principios de la selección natural y la genética darwiniana. Fueron formalizados por John Holland en 1975 [4] y posteriormente popularizados por David Goldberg [5]. De acuerdo con Holland, un GA es un procedimiento de búsqueda adaptativa que mantiene una población de estructuras candidatas (individuos) y las somete iterativamente a operadores genéticos probabilísticos —selección, cruce y mutación— con el fin de evolucionar soluciones progresivamente mejores a un problema de optimización dado.

Formalmente, un Algoritmo Genético opera sobre una población $\mathcal{P}_t = \{x_1, x_2, ..., x_N\}$ de $N$ individuos en la generación $t$, donde cada individuo $x_i$ es una representación codificada (cromosoma) de una solución candidata en el espacio de búsqueda $\Omega$. El algoritmo busca maximizar (o minimizar) una función de aptitud (*fitness*) $f: \Omega \rightarrow \mathbb{R}$ que mide la calidad de cada solución [4, 5].

### Ciclo evolutivo

El proceso evolutivo de un GA sigue un ciclo iterativo compuesto por las siguientes fases [5, 6]:

1. **Inicialización**: Se genera una población inicial $\mathcal{P}_0$ de $N$ individuos, típicamente de forma aleatoria dentro del espacio de búsqueda $\Omega$.

2. **Evaluación**: Se calcula el valor de aptitud $f(x_i)$ para cada individuo $x_i \in \mathcal{P}_t$.

3. **Selección**: Se eligen individuos de la población actual para actuar como progenitores de la siguiente generación. La probabilidad de selección de un individuo es proporcional a su aptitud relativa, implementando así el principio de "supervivencia del más apto". Entre los mecanismos más utilizados se encuentran:
   - **Selección por torneo**: Se seleccionan aleatoriamente $k$ individuos y el de mayor aptitud se elige como progenitor. El parámetro $k$ controla la presión selectiva [6].
   - **Selección por ruleta** (*roulette wheel*): La probabilidad de selección del individuo $x_i$ es $p_i = f(x_i) / \sum_{j=1}^{N} f(x_j)$.
   - **Selección por ranking**: Los individuos se ordenan por aptitud y la probabilidad de selección se asigna según su posición en el ranking, no por su valor absoluto de fitness.

4. **Cruce** (*Crossover*): Dos individuos progenitores intercambian segmentos de su material genético con probabilidad $p_c$ para producir descendientes. Este operador es el principal mecanismo de exploración del espacio de búsqueda, ya que combina esquemas (*building blocks*) de soluciones existentes para generar nuevas configuraciones [4]. Las variantes más comunes incluyen:
   - **Cruce de un punto**: Se selecciona aleatoriamente un punto de corte y se intercambian los segmentos posteriores entre los dos progenitores.
   - **Cruce de dos puntos**: Se seleccionan dos puntos de corte y se intercambia el segmento intermedio.
   - **Cruce uniforme**: Cada gen se hereda de uno u otro progenitor con probabilidad $0.5$.

5. **Mutación**: Cada gen de un descendiente se altera aleatoriamente con probabilidad $p_m$. La mutación introduce variabilidad genética en la población y previene la convergencia prematura a óptimos locales, actuando como mecanismo de diversificación [5, 6].

6. **Reemplazo**: La nueva generación $\mathcal{P}_{t+1}$ se forma a partir de los descendientes generados, posiblemente incorporando estrategias de elitismo (preservar los mejores individuos de $\mathcal{P}_t$ sin modificación) para garantizar que la aptitud máxima no disminuya entre generaciones.

7. **Criterio de parada**: El ciclo se repite hasta que se cumple una condición de terminación: alcanzar un número máximo de generaciones $G$, converger (la diversidad de la población cae bajo un umbral), o encontrar una solución con aptitud satisfactoria.

### Teorema del esquema y convergencia

El fundamento teórico de los GA se sustenta en el **Teorema del Esquema** (*Schema Theorem*) de Holland [4]. Un esquema es un patrón o plantilla que describe un subconjunto de cromosomas. Holland demostró que los esquemas cortos, de bajo orden y con aptitud superior al promedio reciben un número exponencialmente creciente de representantes en generaciones sucesivas. En términos formales, si $H$ es un esquema con aptitud promedio $\bar{f}(H)$ en la generación $t$, el número esperado de representantes de $H$ en la generación $t+1$ satisface:

$$E[m(H, t+1)] \geq m(H, t) \cdot \frac{\bar{f}(H)}{\bar{f}} \cdot \left[1 - p_c \frac{\delta(H)}{l-1}\right] \cdot (1 - p_m)^{o(H)}$$

donde $m(H, t)$ es el número de representantes del esquema $H$ en la generación $t$, $\bar{f}$ es la aptitud promedio de la población, $\delta(H)$ es la longitud definitoria del esquema, $l$ es la longitud del cromosoma, y $o(H)$ es el orden del esquema (número de posiciones fijas). Este resultado, conocido como la **Hipótesis de los Bloques Constructivos** (*Building Block Hypothesis*), sugiere que los GA funcionan recombinando componentes parciales de buenas soluciones para construir soluciones cada vez mejores [4, 5].

### Representación y codificación

La elección de la representación genética es una decisión de diseño crítica que impacta directamente en la eficacia del algoritmo [5, 7]. Las representaciones más comunes incluyen:

- **Codificación binaria**: Cada individuo se representa como una cadena de bits. Es la representación clásica propuesta por Holland [4], adecuada para problemas de optimización combinatoria.
- **Codificación de valores reales**: Los genes toman valores en $\mathbb{R}$, lo que resulta natural para problemas de optimización continua. Esta representación elimina la necesidad de codificar y decodificar entre espacios binarios y reales [7].
- **Codificación por permutaciones**: Utilizada para problemas de ordenamiento (como el problema del viajante), donde cada individuo es una permutación de un conjunto de elementos.
- **Codificación específica del dominio**: Representaciones diseñadas para capturar la estructura particular del problema, como árboles para programación genética o grafos para diseño de redes.

En el contexto de esta tesis, donde los GA evolucionan políticas para entornos de ciberseguridad, cada individuo codifica un mapeo determinístico de estados a acciones $\pi: S \rightarrow A$, donde el cromosoma es un vector de $|S|$ genes, cada uno tomando valores en el conjunto de acciones $A$.

### Ventajas y limitaciones

Los GA presentan características que los distinguen de otros métodos de optimización [6, 7]:

**Ventajas**:
- **Globalidad**: Al mantener una población diversa de soluciones, los GA exploran múltiples regiones del espacio de búsqueda simultáneamente, reduciendo la probabilidad de quedar atrapados en óptimos locales.
- **Flexibilidad de representación**: Pueden aplicarse a problemas con espacios de búsqueda discretos, continuos, mixtos o estructurados, sin requerir propiedades matemáticas específicas de la función objetivo (como derivabilidad o convexidad).
- **Robustez ante ruido**: Al operar sobre poblaciones y utilizar operadores probabilísticos, los GA toleran funciones de aptitud ruidosas o estocásticas.

**Limitaciones**:
- **Sensibilidad a hiperparámetros**: El rendimiento depende críticamente de la configuración de hiperparámetros ($N$, $p_c$, $p_m$, $G$, y mecanismos de selección), cuya optimización constituye un problema de meta-optimización no trivial (desarrollado en la sección de Optimización Bayesiana).
- **Convergencia prematura**: Si la presión selectiva es excesiva o la diversidad genética se agota rápidamente, el algoritmo puede converger a un óptimo local antes de explorar suficientemente el espacio de búsqueda [6].
- **Costo computacional**: Cada generación requiere evaluar la función de aptitud de $N$ individuos, lo que puede ser prohibitivo cuando las evaluaciones son costosas (como simulaciones en entornos complejos de ciberseguridad).

### Complementariedad entre Algoritmos Genéticos y Aprendizaje por Refuerzo

La intersección entre los Algoritmos Genéticos y el Aprendizaje por Refuerzo constituye un área activa de investigación con una  historia que se remonta a los trabajos pioneros de Grefenstette et al. [8]. Ambos paradigmas buscan optimizar el comportamiento de un agente en un entorno, pero desde perspectivas complementarias:

| Dimensión | Aprendizaje por Refuerzo (Q-Learning) | Algoritmos Genéticos |
|-----------|---------------------------------------|---------------------|
| Unidad de aprendizaje | Un agente individual | Una población de soluciones |
| Mecanismo de mejora | Actualización incremental de valores Q | Evolución generacional por selección y recombinación |
| Uso de la señal de recompensa | Paso a paso (TD error) | Episódica (fitness acumulado) |
| Exploración | Epsilon-greedy, UCB, etc. | Mutación y cruce |
| Representación del conocimiento | Q-table o aproximador de funciones | Cromosoma (política codificada) |

Esta complementariedad sugiere que combinar ambos enfoques —utilizando la evolución para generar políticas iniciales informadas que luego se refinan mediante Q-Learning— puede superar las limitaciones individuales de cada paradigma. En particular, los GA pueden proporcionar una exploración global eficiente del espacio de políticas, mientras que el Q-Learning ofrece un refinamiento local preciso basado en experiencia secuencial [8].

# Q-learning

Q-Learning es un algoritmo central en el aprendizaje por refuerzo sin modelo, ampliamente utilizado para resolver problemas de toma de decisiones secuenciales en entornos inciertos. Su objetivo principal es permitir que un agente aprenda una política óptima —es decir, una estrategia de acciones que maximice la recompensa acumulada— dentro de un Proceso de Decisión de Markov (MDP). Para lograrlo, el algoritmo mantiene una Q-Table, una estructura de datos que almacena los valores Q, los cuales representan la recompensa esperada al ejecutar una acción específica en un determinado estado y seguir una política óptima a futuro. Estos valores se actualizan iterativamente utilizando la ecuación de Bellman, lo que permite que el agente mejore progresivamente su comportamiento mediante prueba y error, sin necesidad de conocer previamente el modelo del entorno [18]. 

Un aspecto crítico del proceso es la inicialización de la Q-Table, ya que los valores asignados inicialmente determinan la estrategia de exploración temprana del agente y, en consecuencia, afectan la velocidad de convergencia y la eficacia del aprendizaje. Entre las técnicas más comunes se encuentran la inicialización con ceros, con valores aleatorios pequeños o con valores optimistas. Cada una de estas estrategias influye directamente en el equilibrio entre exploración y explotación, así como en la dinámica general del proceso de aprendizaje.


## Ecuacion de actualizacion de Q-learning

El aprendizaje en Q-Learning es una de las implementaciones más influyentes del Aprendizaje por Diferencias Temporales (Temporal-Difference o TD Learning), como lo definen Sutton y Barto [3]. A diferencia de los métodos de Monte Carlo que esperan hasta el final de un episodio para actualizar el valor, el aprendizaje TD actualiza sus estimaciones en cada paso (un proceso llamado *bootstrapping*). Es un algoritmo off-policy, lo que significa que aprende el valor de la política óptima independientemente de la política que el agente esté siguiendo para explorar [1, 2]. Después de que el agente ejecuta una acción `a` en un estado `s`, observa la recompensa inmediata `r` y el nuevo estado `s'`, el valor `Q(s, a)` se actualiza utilizando una regla derivada de la ecuación de Bellman:

![BellmanEquation](../images/Q-learning-bellman.jpg)
*Figura 1: Desglose de la Ecuación de Actualización de Q-Learning. La imagen ilustra los componentes de la regla de actualización de Q-Learning, incluyendo el Error de Diferencia Temporal (TD Error). Adaptado de "Deep Reinforcement Learning Course: Part 2", por T. Simonini, 2022, Hugging Face (https://huggingface.co/blog/deep-rl-q-part2).*

Un desglose detallado de sus componentes revela su lógica:

- $Q(s, a)$: Es la estimación actual del valor Q para el par estado-acción $(s, a)$.

- $\alpha$: La tasa de aprendizaje (learning rate), es un factor que determina el tamaño del paso para actualizar el valor Q. Un valor alto (cercano a 1) significa que el agente depende en gran medida de la experiencia más reciente, lo que podría resultar en un aprendizaje más rápido, pero menos estable. Un valor bajo (cercano a 0) significa que el agente actualiza los valores Q más lentamente, con un paso más pequeño según la nueva información, lo que puede resultar en un aprendizaje más estable, pero podría ser más lento en converger. 

- $r + \gamma \max_{a'} Q(s', a')$: Este término se conoce como el TD Target (Objetivo de Diferencia Temporal). Es una nueva estimación, más informada, del valor de $Q(s, a)$. Se compone de la recompensa real e inmediata $r$ y la estimación descontada del valor óptimo futuro, $\gamma \max_{a'} Q(s', a')$. El término $\max_{a'} Q(s', a')$ es la estimación del agente de la máxima recompensa acumulada que puede obtener desde el nuevo estado $s'$. Es este término de maximización el que hace que el algoritmo sea off-policy, ya que evalúa la optimalidad desde $s'$ sin importar qué acción se tomará realmente en el siguiente paso.

- $[r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$: Esta diferencia es el TD Error (Error de Diferencia Temporal). Mide la discrepancia entre la nueva estimación (el TD Target) y la estimación antigua ($Q(s, a)$). El algoritmo actualiza el valor Q en una fracción $\alpha$ de este error, moviendo la estimación antigua hacia el objetivo.

En su forma más simple, conocida como Q-learning tabular, el algoritmo almacena todos los valores Q en una tabla o matriz de dimensiones $|S| \times |A|$, llamada Q-table.  Cada celda de la tabla, $Q(s, a)$, contiene la estimación actual de la calidad de tomar la acción $a$ en el estado $s$. El proceso algorítmico de Q-Learning presentado en la Figura 2, se puede resumir en el siguiente bucle de entrenamiento:

- Inicializar la Q-Table: Crear la tabla Q(S, A) para todos los pares estado-acción. (Aquí se aplican las técnicas de inicialización a cero, aleatoria, u optimista descritas en la siguiente sección).

- Elegir una acción: Para el estado actual S, seleccionar una acción A usando una política (ej. Epsilon-Greedy) que balancee exploración y explotación.

- Realizar la acción: Ejecutar A, observar la recompensa R y el nuevo estado S'.

- Actualizar: Aplicar la regla de actualización de Q-Learning para el par Q(S, A).

![Q-learning-Algorithm](../images/q-learning-algorithm.png)
*Figura 2: Pseudocódigo del algoritmo Q-Learning, detallando el bucle de interacción agente-entorno y la regla de actualización. Adaptado de Sutton y Barto [3].*

Para complementar el pseudocódigo, la Figura 3 representa de forma esquemática el ciclo de interacción agente-entorno y cómo este ciclo alimenta la actualización iterativa de la Q-Table.

![Agent-Environment-QTable](../images/agent-environment.jpg)
*Figura 3: Esquema del ciclo de interacción en Q-Learning. El agente observa el estado actual, selecciona una acción basada en Q(s,a), recibe la recompensa y el nuevo estado del entorno, y actualiza la Q-Table en cada iteración.*

Ambas figuras ilustran las dos dimensiones fundamentales del algoritmo Q-Learning: su matemática aplicada y su flujo lógico de información. En la Figura 3, el motor principal del progreso es la transición cíclica del entorno, que provee la tupla de experiencia empírica 
(S,A,R,S′). La Figura 2 demuestra exactamente cómo el algoritmo asimila esta tupla: la recepción de R R y S′ por parte del agente dispara el cálculo del Error de Diferencia Temporal (TD Error), lo que permite actualizar de forma iterativa y off-policy el valor almacenado en la abstracción de memoria del agente, es decir, la Q-Table.

La interdependencia de este ciclo visibiliza uno de los principales cuellos de botella del Aprendizaje por Refuerzo clásico en espacios de estados masivos: la dependencia absoluta de la repetición del bucle para poblar la Q-Table. Tal como se refleja en el pseudocódigo, la política de selección de acciones depende intrínsecamente de los valores Q existentes. Si la Q-Table carece de conocimientos previos útiles, los primeros miles de ciclos de interacción ilustrados en la Figura 3 se reducen a paseos aleatorios ineficientes, dilatando el tiempo de convergencia.

En consecuencia, la Q-Table actúa como el único nexo de memoria entre episodios consecutivos. Como la ecuación de actualización modela una convergencia asintótica orientada al futuro, la calidad de los valores iniciales poblados en esta tabla define críticamente la trayectoria exploratoria del agente. Esta dependencia justifica la necesidad crítica de aplicar técnicas de inicialización informada (como la inyección de políticas evolucionadas mediante Algoritmos Genéticos) en entornos donde la interacción de prueba y error es altamente penalizada o escasa en recompensas


## Técnicas principales de inicialización de Q-tables

La inicialización de las funciones de valor, específicamente las Q-Tables, es un aspecto crucial que influye significativamente en la eficiencia y la rapidez de convergencia del aprendizaje [3]. La estrategia de inicialización determina la postura inicial del agente frente a la incertidumbre, impactando directamente su estrategia de exploración temprana. Se han establecido varias metodologías canónicas, que van desde enfoques neutrales (como la inicialización a ceros) hasta estrategias que fomentan activamente la exploración (como la inicialización optimista). Este apartado analiza las técnicas fundamentales y culmina con enfoques híbridos avanzados que buscan optimizar este punto de partida.

### Inicialización a ceros

Esta es la técnica de inicialización más directa y, por ende, la más común en la práctica del Q-Learning. Consiste en establecer todas las entradas de la Q-Table en un valor de cero [3]. La justificación de esta práctica radica en que, al inicio del proceso de aprendizaje, el agente carece de cualquier información o conocimiento sobre las recompensas esperadas de las acciones en los diferentes estados. Por lo tanto, un valor neutral de cero sirve como un punto de partida imparcial. 

Cuando todos los valores Q son cero, el agente no tiene una preferencia intrínseca por ninguna acción en un estado dado. En ausencia de otros mecanismos de exploración, esto puede llevar a que el agente elija acciones de manera puramente aleatoria. Esta aleatoriedad inicial es a menudo gestionada por políticas de exploración como la estrategia epsilon-greedy, donde el agente elige una acción aleatoria con una probabilidad ε.

Este sesgo, aunque no impide la convergencia a largo plazo en espacios de estados discretos si se garantiza suficiente exploración , puede afectar la eficiencia del aprendizaje inicial. Podría ralentizar el descubrimiento de rutas óptimas si la acción preferida por defecto no es la mejor, o si se necesitan múltiples exploraciones para corregir este sesgo inicial

### Inicialización con valores aleatorios

Una alternativa a la inicialización a ceros es establecer los valores Q iniciales como números aleatorios dentro de un rango limitado (por ejemplo, entre [-k, k] o [0, k], siendo k un valor real pequeño típicamente ≤ 0.5). Esta práctica se alinea con las recomendaciones de Sutton y Barto [3] donde señalan que:  

><em>“Initialize Q(s,a) arbitrarily…”</em>
- Donde "arbitrariamente" incluye explícitamente valores aleatorios pequeños 

Sus principales ventajas son romper la simetría inicial y prevenir preferencias prematuras hacia acciones específicas, fomentando exploración diversificada en etapas tempranas del aprendizaje. Al asignar valores ligeramente distintos a cada par estado-acción, se eliminan empates iniciales que ocurren con la inicialización a cero. Esto evita que el agente seleccione siempre la misma acción por defecto (ej: la primera en el orden de procesamiento) cuando múltiples acciones tienen valores idénticos.

### Inicialización optimista

La inicialización optimista es una técnica utilizada en el aprendizaje por refuerzo, específicamente en algoritmos de aprendizaje de valores como Q-learning. Consiste en asignar valores iniciales elevados a la función de valor acción-estado, Q(s,a), antes de que el agente comience a interactuar con el entorno. En otras palabras, se le da al agente una expectativa "optimista" sobre las recompensas futuras de todas las acciones en cualquier estado. Esto significa que el agente, al principio, creerá que cualquier acción que tome en un estado dado le reportará una recompensa muy alta.


La principal ventaja de este enfoque es que fomenta una exploración exhaustiva inicial. Incluso si el agente utiliza una política puramente codiciosa (greedy), que normalmente lo llevaría a explotar rápidamente las acciones que parecen más prometedoras, la inicialización optimista lo impulsa a probar todas las acciones suficientes veces. Esto ocurre porque todas las estimaciones iniciales de Q(s,a) son muy altas. Para que el agente "confíe" en que una acción es realmente peor que otra, debe explorar y experimentar recompensas reales que disminuyan su valor Q(s,a) estimado. Este comportamiento es fundamental para garantizar que no se pasen por alto acciones potencialmente óptimas, un concepto bien documentado por Sutton y Barto [3]. 

Sin embargo, la inicialización optimista introduce un hiperparámetro adicional: el nivel de optimismo, es decir, cuán alto se deben inicializar los valores de Q(s,a) [2,6]. Elegir el valor óptimo es crucial y depende del problema específico. Si el valor inicial es demasiado alto, el agente podría dedicar un tiempo excesivo a explorar acciones subóptimas, lo que ralentizaría la convergencia. Por el contrario, si es demasiado bajo, no se logrará una exploración inicial suficiente, y el agente podría converger prematuramente a una política subóptima. Una heurística común es inicializar Q(s,a) con un valor cercano al máximo teórico posible de la recompensa acumulada.

En entornos no estacionarios, donde las recompensas o las transiciones del entorno cambian con el tiempo, la inicialización optimista puede ser menos efectiva. El sesgo inicial puede persistir y dificultar la adaptación del agente a los cambios dinámicos del entorno. Si bien al inicio el agente puede experimentar recompensas subóptimas debido a la exploración excesiva de acciones aparentemente malas, este es un compromiso (trade-off) necesario para asegurar que no se ignoren acciones potencialmente buenas que, de otra manera, podrían haber sido pasadas por alto.

A diferencia de la inicialización a cero (donde todos los Q(s,a) se inicializan en 0) o la inicialización aleatoria, el sesgo optimista es deliberado y temporal. Se corrige a medida que el agente explora el entorno y actualiza sus estimaciones de Q(s,a). La inicialización aleatoria, por su parte, no garantiza una exploración uniforme, ya que algunas acciones podrían tener valores iniciales más altos por pura casualidad, lo que llevaría al agente a favorecerlas sin una exploración sistemática.

### Inicialización mediante evolución de políticas    

Una estrategia prometedora para acelerar el aprendizaje por refuerzo en entornos discretos consiste en inicializar las Q-tables a partir de políticas preentrenadas mediante algoritmos evolutivos. Este enfoque parte del supuesto de que, si se dispone de una política eficaz —obtenida mediante optimización evolutiva—, es posible utilizar su comportamiento como base para estimar valores iniciales Q(s, a), mejorando la calidad de la exploración en las primeras etapas de entrenamiento.

Este tipo de técnica se fundamenta en la complementariedad entre aprendizaje por refuerzo y algoritmos evolutivos, ampliamente discutida por Grefenstette et al. [19] y analizada en detalle en revisiones recientes como las de Bai et al. [20] y Li et al. [21]. En este contexto, la evolución de políticas actúa como una forma de preentrenamiento, proporcionando una estructura inicial informada que evita la necesidad de exploración totalmente aleatoria o de inicialización a cero, como ocurre en el Q-learning básico descrito por Sutton y Barto [3].


En este enfoque, cada individuo de la población representa una política candidata (por ejemplo, un mapeo entre estados y acciones). Estas políticas son evaluadas según la recompensa acumulada que generan en el entorno, lo cual define su fitness. A través de operadores evolutivos —como selección, cruce (crossover) y mutación— se genera una población de políticas sucesivamente mejoradas. Las mejores políticas se traducen luego en estimaciones iniciales de valores Q(s, a), ya sea por registro directo de interacciones o mediante aproximaciones inferidas, lo que da lugar a una Q-table parcialmente informada antes de aplicar el algoritmo de aprendizaje por refuerzo.

Este mecanismo puede entenderse como una forma especializada de inicialización optimista, en el sentido de que los valores Q iniciales no solo se fijan deliberadamente por encima de lo observado, sino que se basan en experiencia empírica adquirida a través del proceso evolutivo. Tal como se argumenta en Neustroev & de Weerdt [22], la inicialización optimista puede incentivar la exploración incluso bajo políticas greedy, y en el caso de las políticas evolucionadas, esta exploración se vuelve estratégicamente guiada.

Las principales ventajas de este enfoque incluyen:

- Reducción significativa del tiempo de convergencia del aprendizaje, ya que el agente comienza desde una política con cierto nivel de rendimiento demostrado.

- Exploración inicial más eficiente, debido a que las políticas evolucionadas tienden a cubrir regiones relevantes del espacio de estados-acciones, reduciendo el riesgo de quedar atrapado en mínimos locales.

No obstante, esta técnica también presenta varios desafíos importantes:

-  Costo computacional elevado, ya que los algoritmos evolutivos requieren evaluar muchas políticas en múltiples episodios.

-  Diseño de la función de aptitud, que debe balancear adecuadamente recompensa acumulada, diversidad y exploración.

-  Problemas de discretización, en caso de que las políticas evolucionadas se generen en espacios continuos y deban traducirse a representaciones tabulares para entornos discretos.

Estas técnicas han demostrado especial utilidad en entornos donde el acceso a datos es limitado o costoso, como es el caso del aprendizaje por refuerzo offline [7,8]. En este tipo de escenarios, donde no es posible explorar activamente el entorno, contar con una Q-table informada por políticas previamente evaluadas representa una ventaja significativa. Además, los estudios de Bai et al. [20] y Li et al. [21] resaltan que las políticas evolucionadas no solo actúan como buenas inicializaciones, sino también como mecanismos de exploración estratégicamente guiada, facilitando una cobertura más robusta del espacio de búsqueda y reduciendo la probabilidad de converger a soluciones subóptimas.



# Optimización de Hiperparámetros y Optimización Bayesiana en Algoritmos Genéticos

## 1. Introducción a la Meta-Optimización y Algoritmos Genéticos

En el ámbito de la investigación de operaciones y las ciencias de la computación, los Algoritmos Genéticos (GA, por sus siglas en inglés) se han consolidado como una de las metaheurísticas más poderosas y versátiles para resolver problemas de optimización combinatoria complejos y NP-duros (como problemas de enrutamiento de vehículos, diseño de antenas y optimización de topologías). Inspirados en los procesos biológicos de la selección natural y la evolución, los GA exploran el espacio de soluciones mediante operadores probabilísticos de selección, cruce (crossover) y mutación.

Sin embargo, el rendimiento, la capacidad de convergencia global y la eficiencia computacional de un Algoritmo Genético dependen de manera intrínseca de la correcta configuración de sus parámetros de control o "hiperparámetros". El proceso de encontrar el conjunto óptimo de estos parámetros para un algoritmo de optimización se conoce formalmente como meta-optimización o ajuste de parámetros (parameter tuning).

Tradicionalmente, la configuración de un GA dependía de la intuición humana, metodologías de ensayo y error empíricas, o reglas generales heurísticas. Una selección inadecuada de hiperparámetros puede inducir a una convergencia prematura en óptimos locales (si hay poca diversidad) o a un comportamiento asintótico puramente aleatorio e ineficiente (si la presión de selección es insuficiente o la mutación es excesiva). Los hiperparámetros influyen significativamente en la capacidad de generalización, velocidad de convergencia y rendimiento final del modelo. Por ello, la selección adecuada de hiperparámetros es una etapa crítica del desarrollo de modelos de aprendizaje automático. [9]

Dado que evaluar el rendimiento de un GA en problemas del mundo real es computacionalmente costoso y su naturaleza es inherentemente estocástica, la optimización de sus hiperparámetros representa un desafío de optimización de "caja negra" (black-box). Frente a esto, la Optimización Bayesiana (BO) destaca por su extrema eficiencia muestral para aproximar la topología del rendimiento del GA con una cantidad muy reducida de evaluaciones costosas.

---

## 2. El Problema de la Optimización de Hiperparámetros

### 2.1 Definición formal

El problema de optimización de hiperparámetros (HPO, por sus siglas en inglés) puede formularse como un problema de optimización de caja negra. Dado un algoritmo $\mathcal{A}$ con un vector de hiperparámetros $\boldsymbol{\lambda} \in \Lambda$, donde $\Lambda$ es el espacio de configuraciones admisibles, el objetivo es encontrar la configuración óptima $\boldsymbol{\lambda}^*$ que minimice (o maximice) una función objetivo $f$ [10]:

$$\boldsymbol{\lambda}^* = \arg\min_{\boldsymbol{\lambda} \in \Lambda} f(\boldsymbol{\lambda})$$

donde $f(\boldsymbol{\lambda})$ representa una métrica de rendimiento del algoritmo $\mathcal{A}$ configurado con $\boldsymbol{\lambda}$, evaluada sobre un conjunto de datos o un entorno específico. En el contexto de esta tesis, $\mathcal{A}$ corresponde a un Algoritmo Genético cuya función objetivo $f$ mide la calidad de las políticas evolucionadas para inicializar Q-tables en entornos de ciberseguridad.

La dificultad fundamental de este problema radica en que la función $f$ es típicamente:
- **No derivable**: no existe una expresión analítica cerrada de $f$ respecto a $\boldsymbol{\lambda}$.
- **Costosa de evaluar**: cada evaluación requiere ejecutar el algoritmo completo, posiblemente durante múltiples episodios o generaciones.
- **Ruidosa**: debido a la naturaleza estocástica de los GA, evaluaciones repetidas con la misma configuración $\boldsymbol{\lambda}$ producen resultados distintos.
- **Con espacio de búsqueda mixto**: los hiperparámetros pueden ser continuos, discretos o categóricos [1, 3].

### 2.2 Hiperparámetros vs. parámetros

Es fundamental distinguir entre parámetros e hiperparámetros de un modelo. Los **parámetros** son variables internas que el algoritmo ajusta durante su ejecución (por ejemplo, los pesos de una red neuronal, o los valores Q en una Q-table). Los **hiperparámetros**, en cambio, son variables de configuración establecidas antes de la ejecución del algoritmo y que controlan su comportamiento de aprendizaje [10]. En el contexto de un Algoritmo Genético, los parámetros son los valores de aptitud (*fitness*) de los individuos de la población, mientras que los hiperparámetros incluyen la tasa de mutación, la tasa de cruce, el tamaño de la población, entre otros.

Formalmente, si $\theta$ representa los parámetros del modelo y $\boldsymbol{\lambda}$ los hiperparámetros, el proceso de aprendizaje puede verse como una optimización de dos niveles (*bilevel optimization*) [10]:

$$\boldsymbol{\lambda}^* = \arg\min_{\boldsymbol{\lambda} \in \Lambda} f(\theta^*(\boldsymbol{\lambda}), \boldsymbol{\lambda})$$

$$\text{donde} \quad \theta^*(\boldsymbol{\lambda}) = \arg\min_{\theta} \mathcal{L}(\theta, \boldsymbol{\lambda})$$

En el nivel inferior, el algoritmo optimiza sus parámetros $\theta$ dado un conjunto fijo de hiperparámetros $\boldsymbol{\lambda}$. En el nivel superior, se busca la configuración $\boldsymbol{\lambda}^*$ que produce el mejor rendimiento global.

---

## 3. Hiperparámetros Críticos de los Algoritmos Genéticos

Los Algoritmos Genéticos poseen un conjunto de hiperparámetros cuya interacción determina el balance entre exploración (búsqueda global del espacio de soluciones) y explotación (refinamiento de las mejores soluciones encontradas). A continuación, se describen los hiperparámetros más relevantes.

### 3.1 Tamaño de la población ($N$)

El tamaño de la población determina el número de individuos (soluciones candidatas) que coexisten en cada generación. Una población grande incrementa la diversidad genética y reduce el riesgo de convergencia prematura, pero aumenta proporcionalmente el costo computacional por generación. Una población demasiado pequeña puede llevar a una pérdida rápida de diversidad y al estancamiento en óptimos locales [11].

### 3.2 Tasa de cruce ($p_c$)

La tasa de cruce (o crossover rate) es la probabilidad de que dos individuos padres intercambien material genético para producir nuevos descendientes. Valores típicos se encuentran en el rango $p_c \in [0.6, 0.9]$. Una tasa alta favorece la combinación de bloques constructivos (*building blocks*) de buenas soluciones, mientras que una tasa baja preserva más individuos intactos de una generación a la siguiente.

### 3.3 Tasa de mutación ($p_m$)

La tasa de mutación es la probabilidad de que un gen individual sea alterado de forma aleatoria. Actúa como el principal mecanismo para mantener la diversidad genética y prevenir la convergencia prematura. Valores típicos son pequeños, en el rango $p_m \in [0.001, 0.1]$. Una mutación excesiva degrada la búsqueda a un paseo aleatorio, mientras que una mutación insuficiente puede llevar al estancamiento [11].

### 3.4 Número de generaciones ($G$)

Determina cuántos ciclos evolutivos se ejecutan. Un número insuficiente de generaciones puede truncar el proceso antes de alcanzar una convergencia adecuada, mientras que un exceso resulta en costo computacional innecesario sin mejora significativa del fitness.

### 3.5 Método y presión de selección

El método de selección (torneo, ruleta, ranking, etc.) y sus parámetros asociados (como el tamaño de torneo $k$) controlan la presión selectiva: la intensidad con la que se favorecen los individuos más aptos. Una presión excesiva acelera la convergencia pero reduce la diversidad; una presión insuficiente produce una búsqueda poco dirigida.

### 3.6 Interdependencia de hiperparámetros

Un aspecto crucial, señalado extensamente en la literatura [1, 3], es que los hiperparámetros de un GA no actúan de forma independiente. Existe una compleja red de interacciones:

- Una población grande puede compensar una tasa de mutación baja al mantener diversidad por sí misma.
- Una presión de selección alta requiere mecanismos de diversidad más fuertes (mayor mutación o cruce) para evitar convergencia prematura.
- El número óptimo de generaciones depende del tamaño de la población y de la velocidad de convergencia inducida por los operadores genéticos.

Esta interdependencia convierte al espacio de hiperparámetros en un paisaje de optimización complejo y no separable, donde métodos de búsqueda unidimensionales (como variar un parámetro a la vez) son insuficientes para encontrar configuraciones óptimas.

---

## 4. Métodos Clásicos de Optimización de Hiperparámetros

### Búsqueda manual y ensayo-error

El enfoque más elemental consiste en que un experto humano ajuste los hiperparámetros iterativamente basándose en su intuición y experiencia. Aunque puede ser efectivo cuando el practicante tiene conocimiento profundo del dominio, este método es inherentemente subjetivo, no reproducible y no escala a espacios de alta dimensionalidad [10].

### 4.2 Búsqueda por cuadrícula (Grid Search)

La búsqueda por cuadrícula discretiza cada dimensión del espacio de hiperparámetros en un conjunto finito de valores y evalúa todas las combinaciones posibles. Para $d$ hiperparámetros, cada uno con $k$ valores candidatos, se requieren $k^d$ evaluaciones. Su principal limitación es que sufre de la *maldición de la dimensionalidad*: el número de evaluaciones crece exponencialmente con el número de hiperparámetros, lo que la hace impracticable para espacios de más de 3-4 dimensiones [10].

### 4.3 Búsqueda aleatoria (Random Search)

Propuesta por Bergstra y Bengio [16], la búsqueda aleatoria muestrea configuraciones uniformemente al azar del espacio de hiperparámetros. Bergstra y Bengio demostraron teórica y empíricamente que, cuando solo un subconjunto de hiperparámetros tiene influencia significativa en el rendimiento (lo cual es frecuente en la práctica), la búsqueda aleatoria es más eficiente que la búsqueda por cuadrícula, ya que explora más valores únicos de cada hiperparámetro relevante con el mismo presupuesto de evaluaciones [2, 3].

Sin embargo, tanto Grid Search como Random Search tratan cada evaluación como independiente, sin utilizar información de evaluaciones previas para guiar la búsqueda. Esto las convierte en estrategias pasivas que no aprenden del historial de evaluaciones.

---

## 5. Optimización Bayesiana

### 5.1 Fundamento conceptual

La optimización bayesiana es un método para optimizar funciones objetivo que requieren mucho tiempo (minutos u horas) para su evaluación. Es especialmente adecuada para la optimización en dominios continuos de menos de 20 dimensiones y tolera el ruido estocástico en las evaluaciones de la función. Construye una función sustituta para la función objetivo y cuantifica la incertidumbre en dicha sustituta mediante una técnica de aprendizaje automático bayesiano, la regresión de procesos gaussianos. Posteriormente, utiliza una función de adquisición definida a partir de esta sustituta para decidir dónde tomar muestras [12].

La idea fundamental es construir un modelo sustituto probabilístico (*surrogate model*) de la función objetivo $f(\boldsymbol{\lambda})$ y utilizar este modelo para decidir de manera informada dónde evaluar a continuación, maximizando la información obtenida por cada evaluación costosa.

A diferencia de Grid Search o Random Search, la Optimización Bayesiana es una estrategia **activa** que utiliza toda la información recopilada en evaluaciones previas para construir y actualizar un modelo estadístico de $f$, guiando la búsqueda de manera inteligente hacia regiones prometedoras del espacio de configuraciones [12].



### 5.2 Formulación del marco SMBO

El proceso iterativo de la Optimización Bayesiana se describe mediante el siguiente ciclo [12]:

1. **Inicialización**: Se evalúa $f$ en un conjunto inicial pequeño de configuraciones $\mathcal{D}_0 = \{(\boldsymbol{\lambda}_1, y_1), ..., (\boldsymbol{\lambda}_n, y_n)\}$, donde $y_i = f(\boldsymbol{\lambda}_i) + \epsilon$ y $\epsilon$ captura el ruido de evaluación.

2. **Construcción del modelo sustituto**: Con los datos $\mathcal{D}_t$ disponibles en la iteración $t$, se ajusta un modelo probabilístico $\mathcal{M}_t$ que proporciona, para cada punto $\boldsymbol{\lambda}$ del espacio, una distribución predictiva $p(y | \boldsymbol{\lambda}, \mathcal{D}_t)$ con media $\mu(\boldsymbol{\lambda})$ y varianza $\sigma^2(\boldsymbol{\lambda})$.

3. **Maximización de la función de adquisición**: Se selecciona el siguiente punto a evaluar como $\boldsymbol{\lambda}_{t+1} = \arg\max_{\boldsymbol{\lambda} \in \Lambda} \alpha(\boldsymbol{\lambda} | \mathcal{M}_t)$, donde $\alpha$ es una función de adquisición que cuantifica la utilidad esperada de evaluar en $\boldsymbol{\lambda}$.

4. **Evaluación y actualización**: Se evalúa $y_{t+1} = f(\boldsymbol{\lambda}_{t+1})$, se actualiza el conjunto de datos $\mathcal{D}_{t+1} = \mathcal{D}_t \cup \{(\boldsymbol{\lambda}_{t+1}, y_{t+1})\}$, y se reconstruye el modelo sustituto.

5. **Criterio de parada**: Se repite el ciclo hasta agotar el presupuesto de evaluaciones o alcanzar un criterio de convergencia.

### 5.3 Modelos sustitutos (*Surrogate Models*)

#### 5.3.1 Procesos Gaussianos (GP)

El modelo sustituto más utilizado en la Optimización Bayesiana clásica es el **Proceso Gaussiano** (*Gaussian Process*, GP) [12]. Un GP define una distribución sobre funciones, de forma que cualquier conjunto finito de puntos sigue una distribución normal multivariante:

$$f(\boldsymbol{\lambda}) \sim \mathcal{GP}(m(\boldsymbol{\lambda}), k(\boldsymbol{\lambda}, \boldsymbol{\lambda}'))$$

donde:
- $m(\boldsymbol{\lambda})$ es la función de media (frecuentemente se asume $m(\boldsymbol{\lambda}) = 0$).
- $k(\boldsymbol{\lambda}, \boldsymbol{\lambda}')$ es la función de covarianza o *kernel* que codifica supuestos sobre la suavidad y estructura de $f$.

Dado el conjunto de observaciones $\mathcal{D}_t = \{(\boldsymbol{\lambda}_i, y_i)\}_{i=1}^{t}$, la distribución predictiva posterior en un punto nuevo $\boldsymbol{\lambda}_*$ es analíticamente tratable:

$$\mu(\boldsymbol{\lambda}_*) = \mathbf{k}_*^T (\mathbf{K} + \sigma_n^2 \mathbf{I})^{-1} \mathbf{y}$$

$$\sigma^2(\boldsymbol{\lambda}_*) = k(\boldsymbol{\lambda}_*, \boldsymbol{\lambda}_*) - \mathbf{k}_*^T (\mathbf{K} + \sigma_n^2 \mathbf{I})^{-1} \mathbf{k}_*$$

donde $\mathbf{K}$ es la matriz de covarianza entre las observaciones, $\mathbf{k}_*$ es el vector de covarianzas entre $\boldsymbol{\lambda}_*$ y las observaciones, y $\sigma_n^2$ es la varianza del ruido.

Los GP ofrecen estimaciones calibradas de incertidumbre, lo que los hace ideales para guiar la exploración. Su principal limitación es la complejidad computacional $\mathcal{O}(n^3)$ para la inversión de la matriz de covarianza, lo que los hace menos adecuados cuando el número de evaluaciones es muy grande [12].

#### 5.3.2 Tree-structured Parzen Estimator (TPE)

Una alternativa popular a los GP es el **Tree-structured Parzen Estimator** (TPE), propuesto por Bergstra et al. (2011) [17] e implementado en la librería Hyperopt. En lugar de modelar $p(y | \boldsymbol{\lambda})$ directamente, el TPE modela las densidades condicionales $\ell(\boldsymbol{\lambda}) = p(\boldsymbol{\lambda} | y < y^*)$ y $g(\boldsymbol{\lambda}) = p(\boldsymbol{\lambda} | y \geq y^*)$, donde $y^*$ es un umbral que separa evaluaciones "buenas" de "malas" [10]. La función de adquisición EI se maximiza al maximizar la razón $\ell(\boldsymbol{\lambda}) / g(\boldsymbol{\lambda})$, lo que favorece regiones donde la densidad de buenas configuraciones es alta respecto a las malas.

El TPE maneja naturalmente espacios condicionales y jerárquicos, lo que lo hace particularmente adecuado para hiperparámetros con dependencias estructurales (como elegir *tipo de selección* y luego *tamaño de torneo* solo si el tipo es torneo).

#### 5.3.3 Random Forests (SMAC)

El framework **SMAC3** (*Sequential Model-based Algorithm Configuration*) [14] utiliza, por defecto, un Random Forest [38] como modelo sustituto para aproximar la función objetivo de la optimización de hiperparámetros.

En este contexto, el Random Forest no se emplea como modelo predictivo final del problema, sino como un metamodelo que estima el rendimiento esperado de cada configuración de hiperparámetros y su incertidumbre asociada. Esta elección es especialmente adecuada para espacios de búsqueda mixtos (continuos, discretos y categóricos) y condicionales, frecuentes en la configuración de algoritmos.

El bosque se construye mediante bagging y selección aleatoria de características, lo que reduce la correlación entre árboles y mejora la robustez frente al ruido. A partir del conjunto de árboles, SMAC3 obtiene una predicción de desempeño y una medida de incertidumbre (derivada de la variabilidad entre predicciones individuales), que se utiliza en la función de adquisición para balancear exploración y explotación.

Además, SMAC3 integra un mecanismo de intensificación que compara configuraciones candidatas bajo distintos presupuestos de evaluación, asignando más recursos a las prometedoras y descartando tempranamente las de bajo rendimiento. Esta combinación entre modelo sustituto e intensificación permite una búsqueda eficiente cuando las evaluaciones son costosas y estocásticas.

En el caso de esta tesis, donde cada evaluación del Algoritmo Genético puede ser costosa y ruidosa, SMAC3 resulta apropiado dado que prioriza configuraciones prometedoras con menor número de ejecuciones totales.


### 5.4 Funciones de adquisición

Las funciones de adquisición formalizan el compromiso entre exploración (evaluar en regiones de alta incertidumbre) y explotación (evaluar cerca de las mejores soluciones conocidas). Las más utilizadas son [12]:

#### 5.4.1 Expected Improvement (EI)

La **Mejora Esperada** (*Expected Improvement*) es la función de adquisición más ampliamente utilizada. Dado el mejor valor observado $f^* = \min_{i \leq t} y_i$, el EI cuantifica la mejora esperada sobre $f^*$:

$$\text{EI}(\boldsymbol{\lambda}) = \mathbb{E}[\max(f^* - f(\boldsymbol{\lambda}), 0)] = (f^* - \mu(\boldsymbol{\lambda})) \Phi(Z) + \sigma(\boldsymbol{\lambda}) \phi(Z)$$

donde $Z = \frac{f^* - \mu(\boldsymbol{\lambda})}{\sigma(\boldsymbol{\lambda})}$, $\Phi$ es la CDF normal estándar y $\phi$ es la PDF normal estándar.

El primer término $(f^* - \mu(\boldsymbol{\lambda})) \Phi(Z)$ favorece la **explotación** (puntos con media baja), mientras que el segundo término $\sigma(\boldsymbol{\lambda}) \phi(Z)$ favorece la **exploración** (puntos con alta incertidumbre).

#### 5.4.2 Probability of Improvement (PI)

La **Probabilidad de Mejora** calcula la probabilidad de obtener un valor mejor que $f^*$:

$$\text{PI}(\boldsymbol{\lambda}) = P(f(\boldsymbol{\lambda}) < f^*) = \Phi\left(\frac{f^* - \mu(\boldsymbol{\lambda})}{\sigma(\boldsymbol{\lambda})}\right)$$

PI tiende a ser más explotadora que EI, ya que no considera la magnitud de la mejora, solo su probabilidad.

#### 5.4.3 Upper Confidence Bound (UCB)

El **Límite de Confianza Superior** (o Lower Confidence Bound para minimización) ofrece un balance explícito entre media y varianza:

$$\text{UCB}(\boldsymbol{\lambda}) = \mu(\boldsymbol{\lambda}) - \kappa \cdot \sigma(\boldsymbol{\lambda})$$

donde $\kappa > 0$ es un parámetro que controla el nivel de exploración. Valores altos de $\kappa$ favorecen la exploración, mientras que valores bajos favorecen la explotación.


---

## 6. Optimización Bayesiana Aplicada a Algoritmos Genéticos

### 6.1 Motivación específica

La aplicación de Optimización Bayesiana a la configuración de Algoritmos Genéticos es particularmente relevante por las siguientes razones:

1. **Evaluaciones costosas**: Cada evaluación de una configuración de hiperparámetros de un GA requiere ejecutar el algoritmo completo durante múltiples generaciones, lo cual puede tardar minutos u horas. La eficiencia muestral de la BO es crítica en este contexto [12].

2. **Estocasticidad inherente**: Los GA son algoritmos inherentemente estocásticos, por lo que la función objetivo $f(\boldsymbol{\lambda})$ es ruidosa. Los modelos probabilísticos de la BO (especialmente los GP) manejan naturalmente esta incertidumbre.

3. **Interacciones complejas**: Como se discutió en la Sección 3.6, los hiperparámetros de un GA interactúan de formas no triviales. La BO captura estas interacciones a través de su modelo sustituto, a diferencia de métodos que asumen independencia entre dimensiones.

4. **Espacio de búsqueda mixto**: Los GA poseen hiperparámetros de naturaleza diversa (continuos como $p_m$, discretos como $N$, categóricos como el tipo de selección), un escenario que los modelos sustitutos como TPE y SMAC manejan de forma nativa [10].

### 6.2 Formulación del problema de meta-optimización

En el contexto de esta tesis, el problema de meta-optimización del GA se formula como:

$$\boldsymbol{\lambda}^*_{GA} = \arg\max_{\boldsymbol{\lambda} \in \Lambda_{GA}} \mathbb{E}\left[\text{fitness}_{GA}(\boldsymbol{\lambda})\right]$$

donde $\boldsymbol{\lambda} = (N, p_c, p_m, G, \text{selección}, ...)$ y $\text{fitness}_{GA}(\boldsymbol{\lambda})$ representa la calidad de la mejor política evolucionada por el GA configurado con $\boldsymbol{\lambda}$, medida como la recompensa acumulada promedio en el entorno NetSecGame.

Debido al ruido, cada configuración $\boldsymbol{\lambda}$ puede evaluarse múltiples veces, y el modelo sustituto de la BO captura tanto la tendencia central como la variabilidad del rendimiento.

### 6.3 Flujo de trabajo propuesto

El flujo de meta-optimización combina la BO en el nivel superior con el GA en el nivel inferior:

1. La BO propone una configuración de hiperparámetros $\boldsymbol{\lambda}_t$.
2. El GA se ejecuta con $\boldsymbol{\lambda}_t$ durante $G$ generaciones, evolucionando una población de políticas.
3. La mejor política resultante se evalúa (directamente o como semilla para inicializar una Q-table).
4. El fitness obtenido $y_t$ se reporta al modelo sustituto de la BO.
5. La BO actualiza su modelo y propone la siguiente configuración $\boldsymbol{\lambda}_{t+1}$.

Este diseño permite encontrar configuraciones de GA de alto rendimiento con un número mínimo de ejecuciones costosas, lo cual es esencial en entornos como NetSecGame donde cada episodio de evaluación involucra simulaciones complejas.

En el contexto específico de esta tesis —donde un GA evoluciona políticas para inicializar Q-tables en entornos de ciberseguridad— la capacidad de la BO para optimizar con pocas evaluaciones es particularmente valiosa, dada la complejidad de las simulaciones en entornos como NetSecGame.



---

# Análisis de Sensibilidad Global: Métodos de Sobol y Saltelli

## 1. Introducción al Análisis de Sensibilidad Global

El **análisis de sensibilidad** estudia cómo la incertidumbre en la salida de un modelo puede ser atribuida a diferentes fuentes de incertidumbre en las entradas del modelo. A diferencia del análisis de sensibilidad local (que examina el efecto de pequeñas perturbaciones alrededor de un punto), el **análisis de sensibilidad global (GSA)** explora todo el espacio de entrada de los factores [25] [26] [27]. 

### 1.1 Definición Formal

Dado un modelo $Y = f(X_1, X_2, ..., X_k)$ donde:
- $Y$ es la salida del modelo (escalar)
- $X_i$ son los $k$ factores de entrada (variables independientes)

El objetivo del GSA es cuantificar la contribución de cada factor $X_i$ (y sus interacciones) a la varianza total de $Y$.

Según Saltelli et al. (2008), el análisis de sensibilidad global es fundamental para:

1. **Factor Prioritization (FP)**: Identificar qué factores contribuyen más a la incertidumbre de la salida
2. **Factor Fixing (FF)**: Identificar factores no influyentes que pueden fijarse en cualquier valor
3. **Variance Cutting**: Reducir la varianza de la salida fijando un subconjunto de factores
4. **Factor Mapping**: Identificar qué regiones del espacio de entrada producen salidas específicas

---

## 2. Método de Sobol (Índices de Sensibilidad Basados en Varianza)

### 2.1 Fundamento Teórico

El método de Sobol se basa en la **descomposición funcional ANOVA** (Analysis of Variance) de la función del modelo. Para una función cuadrado-integrable, existe una descomposición única:

$$f(X) = f_0 + \sum_{i=1}^{k} f_i(X_i) + \sum_{i<j} f_{ij}(X_i, X_j) + ... + f_{1,2,...,k}(X_1, ..., X_k)$$

donde:
- $f_0$ es una constante (valor esperado de $f$)
- $f_i(X_i)$ representa el efecto principal del factor $X_i$
- $f_{ij}(X_i, X_j)$ representa la interacción entre $X_i$ y $X_j$
- Los términos de orden superior representan interacciones de mayor complejidad

### 2.2 Descomposición de la Varianza

La varianza total de $Y$ se descompone como:

$$V(Y) = \sum_{i=1}^{k} V_i + \sum_{i<j} V_{ij} + ... + V_{1,2,...,k}$$

donde:
- $V_i = V[E(Y|X_i)]$ es la varianza debida únicamente a $X_i$
- $V_{ij} = V[E(Y|X_i, X_j)] - V_i - V_j$ es la varianza debida a la interacción entre $X_i$ y $X_j$

### 2.3 Índices de Sobol de Primer Orden ($S_i$)

El **índice de Sobol de primer orden** mide la contribución directa (efecto principal) del factor $X_i$ a la varianza de la salida:

$$S_i = \frac{V_i}{V(Y)} = \frac{V[E(Y|X_i)]}{V(Y)}$$

**Interpretación**:
- $S_i \in [0, 1]$
- $S_i$ cercano a 1: $X_i$ explica la mayor parte de la varianza por sí solo
- $S_i$ cercano a 0: $X_i$ tiene poco efecto directo sobre $Y$
- $\sum_{i=1}^{k} S_i \leq 1$ (la igualdad se da solo si el modelo es aditivo)

### 2.4 Índices de Sobol Totales ($S_{Ti}$)

El **índice de Sobol total** cuantifica el efecto total del factor $X_i$, incluyendo todas sus interacciones con otros factores:

$$S_{Ti} = \frac{E[V(Y|X_{\sim i})]}{V(Y)} = 1 - \frac{V[E(Y|X_{\sim i})]}{V(Y)}$$

donde $X_{\sim i}$ denota todos los factores excepto $X_i$.

**Interpretación**:
- $S_{Ti} \geq S_i$ (siempre)
- $S_{Ti} - S_i$ representa la contribución de las interacciones de $X_i$
- Si $S_{Ti} \approx 0$, el factor puede fijarse sin afectar significativamente la salida

### 2.5 Índices de Segundo Orden ($S_{ij}$)

Los **índices de segundo orden** miden la interacción entre pares de factores:

$$S_{ij} = \frac{V_{ij}}{V(Y)} = \frac{V[E(Y|X_i, X_j)] - V_i - V_j}{V(Y)}$$

**Propiedades**:
- Mide la varianza explicada por la interacción $X_i \times X_j$ que no puede atribuirse a efectos individuales
- Útil para identificar sinergias o antagonismos entre parámetros

---

## 3. Método de Muestreo de Saltelli

### 3.1 El Problema del Costo Computacional

El cálculo directo de los índices de Sobol mediante integración Monte Carlo requiere un número muy elevado de evaluaciones del modelo. Para $k$ factores:
- Calcular todos los $S_i$ y $S_{Ti}$: $N \times (k + 2)$ evaluaciones
- Incluir índices de segundo orden: $N \times (2k + 2)$ evaluaciones

donde $N$ es el tamaño de muestra base.

Posteriormente, en la etapa de Diseño, se detalla como se ha implementado y cuales han sido las limitaciones encontradas al momento de aplicar este metodo. 

---

# NetSecGame: Caracterización del entorno y fundamentos de su selección para esta tesis



## Características 

[NetSecGame](https://github.com/stratosphereips/NetSecGame) (Network Security Game) es un framework para el entrenamiento y la evaluación de agentes de IA en tareas de seguridad de red (tanto ofensivas como defensivas). Desarrollado sobre el simulador de red [CYST](https://pypi.org/project/cyst/), permite la creación y prueba eficiente de agentes en escenarios altamente configurables. Ejemplos de agentes implementados pueden encontrarse en el submódulo [NetSecGameAgents](https://github.com/stratosphereips/NetSecGameAgents/tree/main). Este entorno fue desarrollado por el [Stratosphere Research Laboratory](https://www.stratosphereips.org/), grupo de investigación en ciberseguridad perteneciente al Centro de Inteligencia Artificial de la Facultad de Ingeniería Eléctrica de la Universidad Técnica Checa en Praga. Dicho grupo se especializa en la intersección entre ciberseguridad, aprendizaje automático y asistencia técnica.

NetSecGame modela escenarios realistas de redes computacionales, en los cuales los agentes pueden ejecutar acciones típicas de un atacante, tales como reconocimiento, explotación de vulnerabilidades, movimiento lateral y exfiltración de datos.

### Objetivo del simulador

El objetivo principal de NetSecGame es proporcionar un entorno controlado y reproducible que permita:
- Entrenar y evaluar agentes de aprendizaje por refuerzo en tareas de ciberseguridad.
- Simular ataques en redes computacionales.
- Facilitar la investigación en inteligencia artificial aplicada a la seguridad informática.

### Características principales

**Agente atacante**: El entorno se centra en agentes atacantes que deben explorar redes, descubrir vulnerabilidades y comprometer sistemas para alcanzar objetivos específicos.

**Entorno de red realista**: Simula topologías de red complejas con hosts, servicios, datos y reglas de conectividad que reflejan entornos empresariales reales.

**Simulación de ataques**: Reproduce el ciclo completo de un ataque cibernético: reconocimiento, acceso inicial, escalada de privilegios, movimiento lateral y exfiltración.

**Estados parcialmente observables**: Los agentes tienen conocimiento limitado del entorno y deben descubrir progresivamente la topología y recursos disponibles.

**Sistema de recompensas**: Implementa un sistema de recompensas que incentiva el logro de objetivos específicos.

---

## ¿Cómo funciona?

### Arquitectura general

NetSecGame adopta el paradigma clásico de interacción agente-entorno propio del aprendizaje por refuerzo. El ciclo de funcionamiento se compone de las siguientes etapas:

1. **Inicialización**: El entorno se configura con una topología de red específica, incluyendo hosts, servicios, datos y reglas de conectividad.

2. **Observación**: El agente recibe una observación del estado actual, que incluye su conocimiento parcial de la red (hosts conocidos, servicios descubiertos, hosts controlados, etc.).

3. **Acción**: El agente selecciona una acción conforme a su política actual (por ejemplo, escaneo de red, búsqueda de servicios, explotación de vulnerabilidades).

4. **Transición**: El entorno procesa la acción, actualiza su estado interno y determina si la acción fue exitosa según probabilidades predefinidas.

5. **Recompensa**: Se calcula una recompensa basada en el progreso del agente hacia sus objetivos y el costo de la acción ejecutada.

6. **Iteración**: El proceso se repite hasta que se alcanza una condición de terminación (éxito, límite de acciones, detección por el defensor).

### Modo de uso

Para iniciar NetSecGame, es necesario definir una configuración de tarea `task configuration`. En las pruebas realizadas, se empleó una configuración similar a la siguiente:


El entorno se inicia mediante el siguiente comando:

```
python3 -m AIDojoCoordinator.worlds.NSEGameCoordinator \
  --task_config=./examples/example_config.yaml \
  --game_port=9000
```

Una vez ejecutado, se crea un servidor de juego en localhost:9000, al cual los agentes pueden conectarse para interactuar con el entorno de NetSecGame.

#### Docker Container

NetSecGame puede inicializarse mediante un contenedor de Docker. Cuando se ejecuta dentro del entorno Docker, la aplicación puede iniciarse con el siguiente comando:

```
docker run -it --rm \
  -v $(pwd)/examples/example_config.yaml:/aidojo/netsecenv_conf.yaml \
  -v $(pwd)/logs:/aidojo/logs \
  -p 9000:9000 lukasond/aidojo-coordinator:1.0.2
```

--
## ¿Por qué fue creado?

NetSecGame surge en el marco de la investigación académica en ciberseguridad e inteligencia artificial, con el objetivo de suplir la carencia de entornos de simulación realistas y controlados para el entrenamiento de agentes autónomos en tareas de seguridad informática. En este contexto, existen otras iniciativas con propósitos similares, tales como [CybORG++](https://github.com/alan-turing-institute/CybORG_plus_plus), [CybORG](https://github.com/cage-challenge/CybORG,) [CyGil](https://arxiv.org/abs/2109.03331), [CyberBattleSim](https://github.com/microsoft/CyberBattleSim), [NASimEmu](https://github.com/jaromiru/NASimEmu), [PenGym](https://github.com/cyb3rlab/PenGym) y [CyberGym](https://github.com/sunblaze-ucb/cybergym), cada una con enfoques y niveles de complejidad distintos.

### Problemas que busca resolver

NetSecGame aborda diversas limitaciones presentes en los simuladores existentes:

**Escasez de entornos de entrenamiento**: La mayoría de los simuladores no reproducen adecuadamente las condiciones de redes empresariales reales.

**Evaluación reproducible**: Proporciona un entorno controlado que permite repetir experimentos bajo condiciones idénticas, facilitando la comparación de resultados.

**Escalabilidad**: Permite evaluar agentes en escenarios que varían desde redes simples hasta topologías complejas.

**Seguridad**: Ofrece un entorno seguro para experimentar con técnicas de ataque sin riesgo de dañar sistemas reales.

### Ventajas distintivas de NetSecGame

NetSecGame presenta varias ventajas significativas frente a otros entornos de simulación similares:

**Modularidad y extensibilidad**: Es muy modular y fácil de extender a nuevas topologías, lo que permite adaptar el entorno a diferentes necesidades de investigación.

**Realismo de la información**: El agente no recibe información artificial; todo dato disponible corresponde a lo que un atacante real podría obtener.

**Objetivo realista**: La meta principal —exfiltrar datos hacia Internet— refleja motivaciones reales en escenarios de ciberataques.

**Presencia de defensor**: La inclusión de un agente defensor añade complejidad y realismo a la simulación.

**Recompensas genéricas**: Las recompensas no están diseñadas específicamente para el problema particular, sino que son genéricas, lo que mejora la generalización de los enfoques desarrollados.

### Fundamentación en la literatura reciente

La relevancia de NetSecGame para investigación en ciberseguridad y aprendizaje por refuerzo no se limita a su disponibilidad como framework, sino que se sustenta en decisiones de diseño y resultados empíricos reportados en la literatura que motivaron su creación y uso experimental.

En primer lugar, el **objetivo de exfiltración de datos hacia Internet** se alinea con el comportamiento de ataques avanzados (p. ej., APT), en contraste con metas menos realistas usadas en otros entornos (por ejemplo, “comprometer más de la mitad de la red”). En particular, Rigaki et al. [43] destacan el realismo de definir la victoria como la **exfiltración** exitosa, y Bandhana et al. [44] formulan explícitamente el objetivo del atacante como exfiltrar datos hacia un servidor C\&C externo.

En segundo lugar, ambos trabajos refuerzan la elección de una **representación de estado basada en activos** (colecciones de redes/hosts/servicios/datos conocidos y hosts controlados). Esta formulación modela la observación parcial del atacante y el descubrimiento progresivo del entorno: el agente comienza con conocimiento limitado y expande sus activos a medida que ejecuta acciones de reconocimiento y explotación [43, 44]. Adicionalmente, este esquema es compatible con enfoques de planificación: Bandhana et al. [44] conectan la representación por activos con STRIPS (y su relajación al omitir efectos de borrado), mientras que Rigaki et al. [43] enfatizan que el entorno no debe “ayudar” al agente con información irrealista.

En tercer lugar, la **presencia de un defensor omnipresente/estocástico** y la **terminación del episodio por detección** son componentes centrales para capturar el trade-off entre progreso ofensivo y sigilo. En NetSecGame, el defensor puede modelarse como un mecanismo que detecta y finaliza la interacción bajo ciertas condiciones (p. ej., umbrales de repetición/ventanas temporales), priorizando la detección incluso si el atacante alcanzaría simultáneamente un estado ganador [43]. De manera análoga, Bandhana et al. [44] modelan un defensor con visibilidad global que asigna probabilidad de detección a las acciones, terminando el episodio al detectar al atacante.

En cuarto lugar, la literatura enfatiza que en este tipo de entornos conviene emplear **recompensas escasas y genéricas** para evitar sobre-ingeniería: Rigaki et al. [43] usan recompensas terminales (éxito y detección) más un costo por paso, sin recompensas intermedias; Bandhana et al. [44] adoptan una estructura equivalente (penalización por acción, recompensa por objetivo y penalización por detección). En consecuencia, cambios de escala (por ejemplo, usar magnitudes mayores como +1000/-1000) preservan la semántica del problema mientras se mantiene el incentivo a rutas cortas y el castigo por detección.

Finalmente, estos trabajos ofrecen referencias directas para **baselines de agentes** y expectativas de desempeño. Bandhana et al. [44] comparan Q-Learning, Naive Q-Learning y Double Q-Learning, reportando que Double Q-Learning logra el mejor equilibrio entre tasa de éxito y tasa de detección (por ejemplo, en un escenario con posición inicial fija, 74\% de éxito y 33\% de detección). Estos resultados son especialmente relevantes para esta tesis, ya que justifican el uso de variantes de Q-learning más estables en entornos ruidosos. Complementariamente, Rigaki et al. [43] muestran que agentes basados en **LLM preentrenados** pueden actuar como atacantes en NetSecGame mediante diseños de prompting (p. ej., estilo ReAct), alcanzando rendimientos comparables a agentes RL entrenados durante miles de episodios, lo cual refuerza la conexión entre planificación y decisión secuencial en el dominio.

Si bien NetSecGame cuenta actualmente con un número limitado de citas en publicaciones académicas, se trata de un entorno de alta calidad, desarrollado por expertos en ciberseguridad del Cybersecurity Group del Artificial Intelligence Centre, perteneciente a la Faculty of Electrical Engineering de la Czech Technical University in Prague. Su diseño modular, capacidad para simular escenarios ofensivos y defensivos, y su orientación a la investigación en aprendizaje por refuerzo lo convierten en una plataforma valiosa y técnicamente robusta para la experimentación en tareas de seguridad de redes.

---

### Usos principales

NetSecGame ha sido utilizado en diversos contextos:

**Investigación**: Desarrollo y evaluación de algoritmos de aprendizaje automático para ciberseguridad.

**Docencia**: Enseñanza de conceptos de seguridad informática y técnicas de ataque en un entorno controlado.

**Validación de algoritmos**: Comparación objetiva de diferentes enfoques de agentes autónomos.

---

## Justificación de su elección para esta tesis

La selección de NetSecGame como entorno de simulación se fundamenta en su alineación directa con los objetivos de esta investigación, orientada a mejorar la inicialización de políticas en algoritmos de Q-learning aplicados a ciberseguridad multiagente.

### Relevancia temática

NetSecGame se alinea perfectamente con los objetivos de esta investigación al proporcionar:

- **Modelado realista**: Simula escenarios de ciberseguridad que reflejan desafíos del mundo real.
- **Complejidad controlada**: Permite evaluar agentes en entornos de complejidad variable.
- **Observabilidad parcial**: Modela la incertidumbre inherente en escenarios de ciberseguridad reales.

### Adecuación técnica para Q-learning y ciberseguridad multiagente

El entorno presenta características técnicas que lo hacen especialmente adecuado para esta investigación:

- **Representación explícita de estados, acciones y recompensas**: Proporciona estructuras de datos claras y extensibles (GameState, Action, Observation) que facilitan la implementación de Q-learning y la experimentación con diferentes estrategias de inicialización de políticas. 

- **Complejidad escalable**: Permite evaluar métodos de inicialización desde escenarios simples (pocas redes y hosts) hasta complejos (múltiples subredes interconectadas), facilitando el análisis del impacto de diferentes estrategias de inicialización según la complejidad del problema.

- **Observabilidad parcial realista**: El descubrimiento progresivo del entorno simula condiciones reales donde el agente debe aprender con información limitada, siendo crucial para evaluar cómo diferentes inicializaciones de política afectan la exploración y el aprendizaje.

- **Arquitectura multiagente extensible**: Aunque actualmente enfocado en agentes atacantes, su diseño modular permite la extensión a escenarios multiagente donde múltiples atacantes o atacantes-defensores interactúan.

### Espacio controlado y reproducible

**Determinismo configurable**: Posibilita la repetición exacta de experimentos para análisis comparativos.

**Escalabilidad**: Facilita la evaluación desde escenarios simples hasta complejos, permitiendo análisis comparativos sistemáticos.

**Métricas integradas**: Incluye sistemas de logging y métricas que facilitan el análisis de rendimiento.

### Soporte y extensibilidad

**Código abierto**: Base de código disponible y documentada que permite modificaciones y extensiones.

**Configurabilidad**: Arquitectura modular que permite adaptar escenarios según necesidades específicas.

**Comunidad activa**: Soporte continuo y desarrollo activo por parte de la comunidad académica.

### Limitaciones conocidas

**Complejidad exponencial**: El espacio de estados crece exponencialmente con el tamaño del entorno, lo que puede limitar la escalabilidad.

**Simplicidad del defensor**: El defensor no es un agente autónomo, sino un sistema estocástico simple.

**Limitaciones de realismo**: Aunque realista, sigue siendo una abstracción de redes reales.

**Dependencias técnicas**: Requiere configuración específica y conocimiento técnico para su uso efectivo.

NetSecGame constituye la plataforma más adecuada para abordar la problemática de inicialización de políticas en Q-learning aplicado a ciberseguridad multiagente. Su diseño técnico, capacidad de simulación realista, y flexibilidad experimental permiten enfocar los esfuerzos de investigación en el análisis profundo del comportamiento de los agentes, garantizando resultados reproducibles y relevantes para aplicaciones reales.

La adopción de NetSecGame permite enfocar completamente los esfuerzos de investigación en el problema específico de inicialización de políticas, aprovechando un entorno maduro, bien documentado y técnicamente robusto que facilitará la obtención de resultados significativos y reproducibles en el área de investigación propuesta.


--- 

## Arquitectura 

NetSecGame opera como un servidor de simulación que implementa el paradigma clásico de interacción agente-entorno propio del aprendizaje por refuerzo. Los agentes se conectan al servidor mediante sockets TCP y participan en simulaciones en tiempo real, enviando acciones y recibiendo observaciones del entorno en cada iteración del ciclo de entrenamiento.

Este diseño permite ejecutar simulaciones multiagente altamente configurables, en las que cada agente puede actuar de forma autónoma y recibir retroalimentación específica según su desempeño.

### Componentes del juego

El entorno está estructurado en torno a una serie de clases que representan los elementos clave del estado del juego. Estas clases se utilizan tanto en la definición de acciones `Actions` como en la representación del estado `GameState`.

#### IP

IP es un objeto inmutable que representa un objeto IPv4 en NetSecGame. Tiene un único parámetro: la dirección en notación decimal con punto (4 octetos representados como un valor decimal separado por puntos).

Ejemplo:

```
ip = IP("192.168.1.1")
```

#### Network

Network es un objeto inmutable que representa un objeto de red IPv4 en NetSecGame. Tiene dos parámetros: 
- network_ip: str, que representa la dirección IPv4 de la red. 
- mask: int, que representa la máscara en notación CIDR.

Ejemplo: 
```
net = Network("192.168.1.0", 24)
```

#### Service

Service contiene información sobre los servicios que se ejecutan en los hosts. Cada servicio tiene cuatro parámetros: 
- name: str, nombre del servicio (p. ej., "SSH").
- type: str, pasivo o activo. Actualmente no se utiliza. 
- version: str, versión del servicio. 
- is_local: bool, indicador que especifica si el servicio es solo local. (Si es True, el servicio NO es visible sin controlar el host).

Ejemplo: 

```
s = Service('postgresql', 'passive', '14.3.0', False)
```

#### Data

Data contiene información sobre los puntos de datos (archivos) presentes en NetSecGame. Sus posibles parámetros son: 
- owner: str - especifica el usuario propietario de este punto de datos 
- id: str - identificador único del punto de datos en un host 
- size: int - tamaño del punto de datos (opcional, valor predeterminado = 0) 
- type: str - identificación del tipo de archivo (opcional, valor predeterminado = "") 
- content: str - contenido de los datos (opcional, valor predeterminado = "")

Ejemplos: 

```
d1 = Data("User1", "DatabaseData")
d2 = Data("User1", "DatabaseData", size=42, type="txt", "SecretUserDatabase")
```

## Estructura del estado

El estado del entorno se modela como una colección de activos identificados por el agente atacante, estructurados en las siguientes variables:

| Variable             | Tipo de dato                        | Descripción                                                                 |
|----------------------|-------------------------------------|-----------------------------------------------------------------------------|
| `known_networks`     | `set[str]`                          | Subredes conocidas por el agente (ej. '192.168.1.0/24').                    |
| `known_hosts`        | `set[str]`                          | IPs de hosts descubiertos mediante escaneo.                                 |
| `controlled_hosts`   | `set[str]`                          | IPs de hosts comprometidos exitosamente.                                    |
| `known_services`     | `dict[str, set[Service]]`           | Mapeo IP → conjunto de servicios descubiertos (nombre, tipo, versión).      |
| `known_data`         | `dict[str, set[Data]]`              | Mapeo IP → conjunto de datos descubiertos (propietario, identificador).     |

> Nota: Los tipos `Service` y `Data` corresponden a estructuras o clases que encapsulan la información relevante de cada servicio (nombre, tipo, versión) y de cada dato (propietario, identificador), respectivamente.

A continuación se presenta una explicación detallada de cada variable:

- **`known_networks` (`set[str]`)**: Representa el conjunto de subredes que el agente atacante ha identificado en el entorno. Cada elemento es una cadena en notación CIDR (por ejemplo, '10.0.0.0/24'). Esta variable delimita el alcance de exploración posible y condiciona las acciones de escaneo de hosts.

- **`known_hosts` (`set[str]`)**: Contiene las direcciones IP de los hosts que el agente ha descubierto mediante acciones de escaneo. Cada IP es una cadena. El crecimiento de este conjunto refleja el avance del agente en el reconocimiento de la topología de la red.

- **`controlled_hosts` (`set[str]`)**: Incluye las IPs de los hosts sobre los cuales el agente ha obtenido control, generalmente tras explotar vulnerabilidades. Desde estos hosts es posible ejecutar acciones avanzadas, como la búsqueda y exfiltración de datos. El tamaño de este conjunto es un indicador directo del progreso ofensivo del agente.

- **`known_services` (`dict[str, set[Service]]`)**: Es un diccionario donde la clave es la IP de un host conocido y el valor es un conjunto de objetos `Service`. Cada objeto `Service` describe un servicio identificado en ese host, incluyendo atributos como nombre, tipo y versión. Esta variable es fundamental para la identificación de posibles vectores de ataque y para la planificación de acciones de explotación.

- **`known_data` (`dict[str, set[Data]]`)**: Es un diccionario donde la clave es la IP de un host controlado y el valor es un conjunto de objetos `Data`. Cada objeto `Data` representa un dato descubierto, con información sobre el propietario y un identificador único. El descubrimiento de datos es el objetivo final en muchos escenarios, por lo que esta variable es crítica para la evaluación del desempeño del agente.

> Nota: El entorno no permite la eliminación de elementos del estado, lo que implica un crecimiento monótono del espacio de estados.

---

## Dinámica de actualización

La actualización de cada variable del estado depende de las acciones ejecutadas por el agente, conforme se detalla en la siguiente tabla:

| Acción del agente     | Variables afectadas         | Descripción                                                                 |
|------------------------|------------------------------|-----------------------------------------------------------------------------|
| `ScanNetwork`          | `known_hosts`                | Descubre hosts en una red conocida.                                         |
| `FindServices`         | `known_services`             | Descubre servicios en un host conocido.                                     |
| `ExploitService`       | `controlled_hosts`           | Si tiene éxito, añade el host a los controlados.                            |
| `FindData`             | `known_data`                 | Descubre datos en un host controlado.                                       |
| `ExfiltrateData`       | No modifica el estado        | Transfiere datos desde un host controlado al C&C.                           |

La dinámica de actualización del estado en NetSecGame está diseñada para reflejar el proceso progresivo de descubrimiento y control que caracteriza a los ataques en entornos reales de ciberseguridad. Cada acción ejecutada por el agente puede modificar el estado, incrementando el conocimiento o el control sobre los activos de la red. Es importante destacar que:

- El agente parte de un conocimiento parcial del entorno, limitado a una o varias redes iniciales y, en algunos escenarios, a ciertos hosts controlados de inicio.
- Las acciones de reconocimiento, como `ScanNetwork` y `FindServices`, expanden el conocimiento del agente sobre la topología y los servicios disponibles, permitiendo identificar nuevos objetivos potenciales.
- Las acciones ofensivas, como `ExploitService`, permiten al agente obtener control sobre hosts previamente conocidos, lo que habilita la ejecución de acciones más avanzadas, como la búsqueda y exfiltración de datos.
- El descubrimiento de datos (`FindData`) solo es posible en hosts que ya han sido comprometidos, lo que introduce una dependencia secuencial en la progresión del agente.
- La acción `ExfiltrateData` representa la culminación del ciclo ofensivo, pero no modifica el estado interno del agente, ya que la información exfiltrada permanece registrada como conocida.
- El entorno no contempla la pérdida de conocimiento ni el retroceso en el control de activos: una vez que un elemento es descubierto o comprometido, permanece en el estado del agente durante toda la simulación.

Esta dinámica asegura que el espacio de estados evolucione de manera monótona, reflejando el avance acumulativo del agente y permitiendo analizar estrategias de exploración, explotación y cobertura en escenarios de ciberseguridad realistas.


---

## Complejidad del espacio de estados

El espacio de estados presenta un crecimiento exponencial respecto al número de elementos presentes en el entorno, lo que incrementa significativamente la complejidad computacional de los algoritmos de aprendizaje y planificación. La cota superior puede estimarse como:

$$
\mathcal{O}\left(2^{(n-1)} \cdot 3^{(h-2)} \cdot 2^{(s-1)} \cdot 2^{(d \cdot h)}\right)
$$

Donde:
- \( n \): número de redes
- \( h \): número de hosts
- \( s \): número de servicios
- \( d \): número de datos por host

Este crecimiento implica una alta complejidad computacional para algoritmos de aprendizaje por refuerzo o planificación secuencial.

La expresión de la cota superior del espacio de estados puede desglosarse de la siguiente manera:

- $2^{(n-1)}$: Representa la posibilidad de conocer o no cada una de las $n$ redes del entorno, considerando que el agente inicia con al menos una red conocida.
- $3^{(h-2)}$: Cada uno de los $h$ hosts puede estar en uno de tres estados: desconocido, conocido o controlado. Se asume que el agente comienza con al menos dos hosts controlados.
- $2^s$: Cada uno de los $s$ servicios presentes en el entorno puede ser conocido o desconocido para el agente.
- $2^{(d \cdot h)}$: Cada uno de los $d$ datos posibles puede estar presente o no en cada uno de los $h$ hosts del entorno.

Este desglose evidencia cómo la combinación de descubrimiento progresivo y control parcial sobre los activos genera un espacio de estados de crecimiento exponencial, lo que plantea desafíos significativos para el diseño y entrenamiento de agentes inteligentes en NetSecGame.


### Observations

Tras enviar la Acción `a` al entorno, los agentes reciben una `Observation`. Cada observación consta de 4 partes: 
- state: `Gamestate`, con la vista actual del estado del entorno; 
- reward: `int`, con la recompensa inmediata que el agente recibe por ejecutar la Acción `a`; 
- end: `bool`, indica si la interacción puede continuar después de ejecutar la Acción `a`; 
- info: `dict`, marcador de posición para cualquier información proporcionada al agente (p. ej., la razón por la que `end is True`).

Este diseño permite que el agente procese la retroalimentación de forma estructurada, facilitando la actualización de su política de acción y la evaluación de su desempeño en función de los objetivos definidos.

## Sistema de recompensas

Recompensas internas del agente Q-learning

El entorno NetSecGame define y asigna una función de recompensa simple al agente de Q-learning, que asigna retroalimentación solo en eventos críticos:  

| Evento | Condición de activación |Recompensa Q-Agent |
|--------|------------------------|-------------------|
| **Paso normal** | Acción que no termina episodio | -1 |
| **Éxito (exfiltración exitosa)** | `AgentStatus.Success` | +1000 |
| **Detección** | `AgentStatus.Fail` | -1000 | 
| **Timeout (límite de pasos)** | `AgentStatus.TimeoutReached` |-100 | 


La función de recompensa no proporciona retroalimentación parcial ante logros intermedios (ej.: controlar un host o descubrir un dato). Ademas en etapas tempranas, el agente puede carecer de señales útiles para aprender rutas efectivas hacia el objetivo.

A pesar de ello, de esta manera, la recompensa está directamente vinculada al éxito operativo del agente. A su vez, la función es fácil de interpretar y mantener.

## Selección y especificación de scenario1-full

La elección del escenario Scenario1-Full dentro del entorno NetSecGame se fundamenta en su capacidad para representar de manera realista y controlada los desafíos que enfrentan los sistemas de ciberseguridad en entornos corporativos. Este escenario proporciona una base sólida para evaluar el desempeño de agentes de aprendizaje por refuerzo en tareas ofensivas como la exfiltración de datos, el movimiento lateral y la explotación de vulnerabilidades. Este escenario fue elegido por su capacidad de reproducir de manera controlada los desafíos que enfrentan los sistemas de ciberseguridad en contextos corporativos reales, integrando tanto superficies de ataque como mecanismos de defensa que permiten probar el desempeño de los agentes bajo condiciones diversas y exigentes.

Scenario1-Full fue seleccionado por las siguientes razones:

- Complejidad estructural: Integra múltiples subredes, servicios, usuarios y políticas de acceso que simulan una red empresarial real.
- Presencia de mecanismos defensivos: Incluye firewalls y segmentación de red que obligan al agente a planificar rutas de ataque sofisticadas.
- Escalabilidad: Permite extender la arquitectura para evaluar el comportamiento del agente en escenarios más complejos.
- Relevancia práctica: Refleja situaciones comunes en entornos corporativos, lo que facilita la transferencia de resultados a aplicaciones reales.

### Arquitectura de red

#### Topología general

La arquitectura de red del Scenario1 Full presentada en la Figura N, se estructura mediante una topología segmentada que comprende dos subredes principales interconectadas a través de un router central con funcionalidades de firewall integradas. Esta configuración refleja las mejores prácticas de segmentación de red utilizadas en entornos empresariales para limitar el alcance de potenciales compromisos de seguridad.

![Topología del escenario full](../NetSecGame/figures/scenario_1.png)
*Figura X: Topología de red del escenario1 full de NetSecGame.*

Las subredes están organizadas de la siguiente manera:

- **Subred de servidores**: 192.168.1.0/24 - Aloja los recursos críticos de la organización.
- **Subred de clientes**: 192.168.2.0/24 - Representa las estaciones de trabajo de usuarios finales.
- **Conectividad externa**: 213.47.23.192/26 - Simula la conectividad a Internet.

### Router central

El router central, accesible mediante las direcciones 192.168.1.1 y 192.168.2.1, funciona como el punto de control y seguridad de la red. Este dispositivo implementa:

- Funcionalidades de firewall con políticas restrictivas configuradas por defecto (política DENY).
- Reglas de acceso específicas que regulan la comunicación entre las diferentes subredes.
- Gateway de conectividad externa para operaciones que requieren acceso a Internet.
- Filtrado de tráfico basado en políticas de seguridad predefinidas.


### Descripción de nodos

#### Nodos servidor

La subred de servidores contiene cinco sistemas que alojan diferentes servicios y tipos de datos, cada uno configurado con características específicas que representan diferentes roles dentro de una infraestructura corporativa.

##### Servidor SMB (192.168.1.2)

Este sistema ejecuta Windows Server y proporciona servicios de compartición de archivos mediante el protocolo SMB (Server Message Block). Los servicios configurados incluyen:

- **microsoft-ds**: Servicio SMB/CIFS para compartición de archivos, identificado como vulnerable a exploits remotos.
- **ms-wbt-server**: Servicio de Remote Desktop Protocol para acceso remoto.
- **windows login**: Sistema de autenticación local.

El servidor almacena múltiples conjuntos de datos sensibles: DataFromServer1 (propiedad de User1), Data2FromServer1 (propiedad de User2), y Data3FromServer1 (propiedad de User1). Los usuarios autorizados incluyen User1 a User5 y el usuario Administrator.

La vulnerabilidad del servicio SMB constituye un vector de ataque principal, permitiendo la explotación remota para acceder a los datos almacenados en el sistema.

##### Servidor de base de datos (192.168.1.3)

Sistema basado en Linux que aloja servicios de base de datos críticos:

- **ssh**: OpenSSH versión 8.1.0 para acceso remoto seguro.
- **postgresql**: Sistema de gestión de base de datos PostgreSQL versión 14.3.0.

El servidor contiene DatabaseData (propiedad de User1) y cuenta con usuarios User1 a User5 además del usuario root. El acceso requiere autenticación SSH válida, proporcionando una capa adicional de seguridad comparado con otros servicios.

##### Servidor web (192.168.1.4)

Sistema Linux configurado para servicios web con las siguientes características:

- **http**: Servidor web lighttpd versión 1.4.54.
- **ssh**: OpenSSH versión 8.1.0.

Almacena WebServerData (propiedad de User2). Los usuarios autorizados incluyen User1 a User5 y root.

##### Servidores adicionales (192.168.1.5 y 192.168.1.6)

Ambos sistemas ejecutan Linux y proporcionan servicios básicos:

- **ssh**: Acceso remoto únicamente.
- **Usuarios**: Solo el usuario root.
- **Función**: Servidores de propósito general con acceso altamente restringido.

Estos nodos sirven como objetivos secundarios y puntos potenciales para movimiento lateral dentro de la red.

#### Nodos cliente

La subred de clientes comprende cinco estaciones de trabajo que representan diferentes puntos de entrada potenciales para un atacante. Estos sistemas simulan las estaciones de trabajo típicas encontradas en entornos corporativos.

##### Cliente 1 (192.168.2.2)

Constituye el punto de ataque principal del escenario:

- **Sistema operativo**: Windows.
- **Servicios**: ms-wbt-server y can_attack_start_here (marcador de punto de inicio).
- **Servicio especial**: attacker - representa al agente atacante controlado por IA.
- **Usuarios**: User1 y Administrator.

Este nodo está preconfigurado como el punto de inicio predeterminado para el agente atacante, proporcionando la base para iniciar operaciones de reconocimiento y ataque.

##### Clientes 2-5 (192.168.2.3-192.168.2.6)

Los clientes restantes proporcionan diversidad en términos de sistemas operativos y configuraciones:

- **Cliente 2** (192.168.2.3): Sistema Windows  y marcador de inicio, usuarios User2 y Administrator.
- **Cliente 3** (192.168.2.4): Sistema Linux con SSH y marcador de inicio, usuarios User3 y root.
- **Cliente 4** (192.168.2.5): Sistema Linux con SSH y marcador de inicio, usuarios User4 y root.
- **Cliente 5** (192.168.2.6): Sistema Linux con acceso solo local, usuarios User5 y root.

Esta diversidad permite evaluar la capacidad del agente para adaptarse a diferentes plataformas y configuraciones de seguridad.

#### Nodo externo

##### Outside node C&C Server (213.47.23.195)

Representa un sistema externo en Internet configurado específicamente para operaciones de exfiltración:

- **Ubicación**: Internet simulado.
- **Servicios**: listener para recepción de datos exfiltrados.
- **Control**: Bajo control del atacante.
- **Función**: Destino final para la transferencia de datos comprometidos.

### Dinámicas del entorno

#### Objetivo y mecánicas de juego

El objetivo principal del agente atacante consiste en completar una secuencia de acciones que comprende: iniciación desde un nodo cliente, exploración de la red para identificar servicios y vulnerabilidades, explotación de sistemas vulnerables, localización de datos sensibles en los servidores, y exfiltración de información al nodo externo.

Esta secuencia requiere que el agente desarrolle estrategias de planificación secuencial, evaluación de riesgos, y optimización de recursos dentro de las limitaciones impuestas por los mecanismos de defensa del entorno.

#### Rutas de ataque

##### Ruta principal: explotación SMB

La estrategia de ataque más directa involucra:

1. **Iniciación**: Activación del agente en Cliente 1 con servicio atacante activo.
2. **Reconocimiento**: Escaneo sistemático de la subred de servidores para identificar servicios disponibles.
3. **Explotación**: Utilización del exploit SMB contra el servicio microsoft-ds en el servidor SMB.
4. **Acceso a datos**: Recuperación de archivos críticos almacenados en el sistema comprometido.
5. **Exfiltración**: Transferencia de datos al outside node através de la conectividad externa.

#### Configuración de acceso y autenticación

##### Sistemas de autenticación

Cada nodo mantiene su propio sistema de usuarios y credenciales:

- **Autenticación local**: Cada sistema gestiona independientemente sus usuarios autorizados
- **Niveles de privilegio**:
  - LIMITED: Acceso básico de usuario con permisos restringidos.
  - ELEVATED: Privilegios administrativos con acceso completo al sistema.

##### Políticas de firewall

El router central implementa políticas de acceso estrictas:

- **Cadena INPUT**: Permite únicamente acceso directo desde subredes específicamente autorizadas.
- **Cadena FORWARD**: Reglas granulares para comunicación entre subredes.
- **Política predeterminada**: DENY (denegación explícita de todo tráfico no autorizado).

Esta configuración refleja las mejores prácticas de seguridad de red, requiriendo que el agente desarrolle estrategias sofisticadas para navegar las restricciones de acceso.

### Complejidad computacional y escalabilidad

#### Dimensiones del espacio de estados

El Scenario1 Full presenta un espacio de estados multidimensional caracterizado por:

- **Diez nodos activos**: Cada uno con múltiples servicios y estados de configuración posibles.
- **Servicios heterogéneos**: Diferentes protocolos, versiones y configuraciones de seguridad.
- **Estados de compromiso**: Múltiples niveles de acceso y control por nodo.
- **Distribución de datos**: Información crítica dispersa en varios servidores con diferentes niveles de protección.

#### Variabilidad del entorno

El entorno presenta características dinámicas que aumentan su complejidad:

- **Múltiples rutas de solución**: Diversas estrategias válidas para alcanzar los objetivos del escenario.
- **Escalabilidad**: Arquitectura base que puede extenderse para crear escenarios de mayor complejidad.


### Relevancia para la investigación

El Scenario1 Full de NetSecGame proporciona un entorno de entrenamiento completo y metodológicamente riguroso para la investigación en ciberseguridad y aprendizaje automático. Su diseño incorpora elementos realistas de infraestructuras de red corporativas, manteniendo al mismo tiempo la controlabilidad necesaria para experimentos reproducibles.

La complejidad inherente del escenario, combinada con sus múltiples rutas de solución, lo convierte en una plataforma valiosa para evaluar y comparar diferentes aproximaciones algorítmicas en el dominio de la ciberseguridad ofensiva. Además, su arquitectura escalable proporciona una base sólida para el desarrollo de escenarios más complejos en investigaciones futuras.






---

# Anexos

## Anexo A: netsecenv_conf.yaml

```python
# Configuration file for the NetSecGame environment

coordinator:
  # Define the conf for all the 'attacker' agents.
  agents:
    Attacker:
      max_steps: 100
      goal:
        description: "Exfiltrate data to '213.47.23.195'"
        is_any_part_of_goal_random: True
        known_networks: []
        #known_networks: [192.168.1.0/24, 192.168.3.0/24]
        known_hosts: []
        #known_hosts: [192.168.1.1, 192.168.1.2]
        controlled_hosts: []
        #controlled_hosts: [213.47.23.195, 192.168.1.3]
        # Services are defined as a target host where the service must be, and then a description in the form 'name,type,version,is_local'
        known_services: {}
        #known_services: {192.168.1.3: [Local system, lanman server, 10.0.19041, False], 192.168.1.4: [Other system, SMB server, 21.2.39421, False]}
        # In data, put the target host that must have the data and which data in format user,data
        # Example to fix the data in one host
        known_data: {213.47.23.195: [[User1,DataFromServer1]]}
        # Example to fix two data in one host
        #known_data: {213.47.23.195: [[User1,DataFromServer1], [User5,DataFromServer5]]}
        # Example to fix the data in two host
        #known_data: {213.47.23.195: [User1,DataFromServer1], 192.168.3.1: [User3,Data3FromServer3]}
        # Example to ask a random data in a specific server. Putting 'random' in the data, forces the env to randomly choose where the goal data is
        # known_data: {213.47.23.195: [random]}
        known_blocks: {}
        # Example of known blocks. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}
      start_position:
        known_networks: []
        known_hosts: []
        # The attacker must always at least control the CC if the goal is to exfiltrate there
        # Example of fixing the starting point of the agent in a local host
        controlled_hosts: [213.47.23.195, random]
        # Example of asking a random position to start the agent
        # controlled_hosts: [213.47.23.195, random]
        # Services are defined as a target host where the service must be, and then a description in the form 'name,type,version,is_local'
        known_services: {}
        # known_services: {192.168.1.3: [Local system, lanman server, 10.0.19041, False], 192.168.1.4: [Other system, SMB server, 21.2.39421, False]}
        # Same format as before
        known_data: {}
        known_blocks: {}
        # Example of known blocks to start with. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}

    Defender:
      goal:
        description: "Block all attackers"
        is_any_part_of_goal_random: False
        known_networks: []
        # Example
        #known_networks: [192.168.1.0/24, 192.168.3.0/24]
        known_hosts: []
        # Example
        #known_hosts: [192.168.1.1, 192.168.1.2]
        controlled_hosts: []
        # Example
        #controlled_hosts: [213.47.23.195, 192.168.1.3]
        # Services are defined as a target host where the service must be, and then a description in the form 'name,type,version,is_local'
        known_services: {}
        # Example
        #known_services: {192.168.1.3: [Local system, lanman server, 10.0.19041, False], 192.168.1.4: [Other system, SMB server, 21.2.39421, False]}
        # In data, put the target host that must have the data and which data in format user,data
        # Example to fix the data in one host
        known_data: {}
        # Example to fix two data in one host
        #known_data: {213.47.23.195: [[User1,DataFromServer1], [User5,DataFromServer5]]}
        # Example to fix the data in two host
        #known_data: {213.47.23.195: [User1,DataFromServer1], 192.168.3.1: [User3,Data3FromServer3]}
        # Example to ask a random data in a specific server. Putting 'random' in the data, forces the env to randomly choose where the goal data is
        # known_data: {213.47.23.195: [random]}
        known_blocks: {213.47.23.195: 'all_attackers'}
        # Example of known blocks. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}
        # You can also use the wildcard string 'all_routers', and 'all_attackers', to mean that all the controlled hosts of all the attackers should be in this list in order to win

      start_position:
        # should be empty for defender - will be extracted from controlled hosts
        known_networks: []
        # should be empty for defender - will be extracted from controlled hosts
        known_hosts: []
        # list of controlled hosts, wildard "all_local" can be used to include all local IPs
        controlled_hosts: [all_local]
        known_services: {}
        known_data: {}
        # Blocked IPs
        blocked_ips: {}
        known_blocks: {}
        # Example of known blocks to start with. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}

env:
  # random means to choose the seed in a random way, so it is not fixed
  random_seed: 'random'
  # Or you can fix the seed
  # random_seed: 42
  scenario: 'scenario1'
  use_global_defender: False
  use_dynamic_addresses: False
  use_firewall: True
  save_trajectories: False
  rewards:
    success: 100
    step: -1
    fail: -10
  actions:
    scan_network:
      prob_success: 1.0
    find_services:
      prob_success: 1.0
    exploit_service:
      prob_success: 1.0
    find_data:
      prob_success: 1.0
    exfiltrate_data:
      prob_success: 1.0
    block_ip:
```

### Anexo B: netsecenv_conf_dynamic.yaml

```python
# Configuration file for the NetSecGame environment

coordinator:
  # Define the conf for all the 'attacker' agents.
  agents:
    Attacker:
      max_steps: 100
      goal:
        description: "Exfiltrate data to '213.47.23.195'"
        is_any_part_of_goal_random: True
        known_networks: []
        #known_networks: [192.168.1.0/24, 192.168.3.0/24]
        known_hosts: []
        #known_hosts: [192.168.1.1, 192.168.1.2]
        controlled_hosts: []
        #controlled_hosts: [213.47.23.195, 192.168.1.3]
        # Services are defined as a target host where the service must be, and then a description in the form 'name,type,version,is_local'
        known_services: {}
        #known_services: {192.168.1.3: [Local system, lanman server, 10.0.19041, False], 192.168.1.4: [Other system, SMB server, 21.2.39421, False]}
        # In data, put the target host that must have the data and which data in format user,data
        # Example to fix the data in one host
        known_data: {213.47.23.195: [[User1,DataFromServer1]]}
        # Example to fix two data in one host
        #known_data: {213.47.23.195: [[User1,DataFromServer1], [User5,DataFromServer5]]}
        # Example to fix the data in two host
        #known_data: {213.47.23.195: [User1,DataFromServer1], 192.168.3.1: [User3,Data3FromServer3]}
        # Example to ask a random data in a specific server. Putting 'random' in the data, forces the env to randomly choose where the goal data is
        # known_data: {213.47.23.195: [random]}
        known_blocks: {}
        # Example of known blocks. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}
      start_position:
        known_networks: []
        known_hosts: []
        # The attacker must always at least control the CC if the goal is to exfiltrate there
        # Example of fixing the starting point of the agent in a local host
        controlled_hosts: [213.47.23.195, random]
        # Example of asking a random position to start the agent
        # controlled_hosts: [213.47.23.195, random]
        # Services are defined as a target host where the service must be, and then a description in the form 'name,type,version,is_local'
        known_services: {}
        # known_services: {192.168.1.3: [Local system, lanman server, 10.0.19041, False], 192.168.1.4: [Other system, SMB server, 21.2.39421, False]}
        # Same format as before
        known_data: {}
        known_blocks: {}
        # Example of known blocks to start with. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}

    Defender:
      goal:
        description: "Block all attackers"
        is_any_part_of_goal_random: False
        known_networks: []
        # Example
        #known_networks: [192.168.1.0/24, 192.168.3.0/24]
        known_hosts: []
        # Example
        #known_hosts: [192.168.1.1, 192.168.1.2]
        controlled_hosts: []
        # Example
        #controlled_hosts: [213.47.23.195, 192.168.1.3]
        # Services are defined as a target host where the service must be, and then a description in the form 'name,type,version,is_local'
        known_services: {}
        # Example
        #known_services: {192.168.1.3: [Local system, lanman server, 10.0.19041, False], 192.168.1.4: [Other system, SMB server, 21.2.39421, False]}
        # In data, put the target host that must have the data and which data in format user,data
        # Example to fix the data in one host
        known_data: {}
        # Example to fix two data in one host
        #known_data: {213.47.23.195: [[User1,DataFromServer1], [User5,DataFromServer5]]}
        # Example to fix the data in two host
        #known_data: {213.47.23.195: [User1,DataFromServer1], 192.168.3.1: [User3,Data3FromServer3]}
        # Example to ask a random data in a specific server. Putting 'random' in the data, forces the env to randomly choose where the goal data is
        # known_data: {213.47.23.195: [random]}
        known_blocks: {213.47.23.195: 'all_attackers'}
        # Example of known blocks. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}
        # You can also use the wildcard string 'all_routers', and 'all_attackers', to mean that all the controlled hosts of all the attackers should be in this list in order to win

      start_position:
        # should be empty for defender - will be extracted from controlled hosts
        known_networks: []
        # should be empty for defender - will be extracted from controlled hosts
        known_hosts: []
        # list of controlled hosts, wildard "all_local" can be used to include all local IPs
        controlled_hosts: [all_local]
        known_services: {}
        known_data: {}
        # Blocked IPs
        blocked_ips: {}
        known_blocks: {}
        # Example of known blocks to start with. In the host 192.168.2.2, block all connections coming or going to 192.168.1.3
        # known_blocks: {192.168.2.2: {192.168.1.3}}

env:
  # random means to choose the seed in a random way, so it is not fixed
  random_seed: 'random'
  # Or you can fix the seed
  # random_seed: 42
  scenario: 'scenario1'
  use_global_defender: False
  use_dynamic_addresses: True
  use_firewall: True
  save_trajectories: False
  rewards:
    success: 100
    step: -1
    fail: -10
  actions:
    scan_network:
      prob_success: 1.0
    find_services:
      prob_success: 1.0
    exploit_service:
      prob_success: 1.0
    find_data:
      prob_success: 1.0
    exfiltrate_data:
      prob_success: 1.0
    block_ip:
```




# Referencias Bibliográficas

[1]: Russell, S. & Norvig, P. (2021). Artificial Intelligence, Global Edition. (4th ed.). Pearson Education.

[2]: Mitchell, T. M. (1997). Machine Learning (Vol. 1). McGraw-Hill.

[3]: Sutton, R. S., Barto, A. G. (2018). Reinforcement Learning: An Introduction. The MIT Press.

[4]: Holland, J. H. (1975). Adaptation in Natural and Artificial Systems. University of Michigan Press. (Reeditado por MIT Press, 1992).

[5]: Goldberg, D. E. (1989). Genetic Algorithms in Search, Optimization, and Machine Learning. Addison-Wesley.

[6]: Katoch, S., Chauhan, S. S., & Kumar, V. (2021). A review on genetic algorithm: past, present, and future. *Multimedia Tools and Applications*, 80, 8091–8126. Springer. https://doi.org/10.1007/s11042-020-10139-6

[7]: Lambora, A., Gupta, K., & Chopra, K. (2019). Genetic Algorithm – A Literature Review. *International Conference on Machine Learning, Big Data, Cloud and Parallel Computing (COMITCon)*, pp. 380–384. IEEE. https://doi.org/10.1109/COMITCon.2019.8862255

[8]: Grefenstette, J. J. & Ramsey, C. L. (1992). An Approach to Anytime Learning. *Proceedings of the Ninth International Conference on Machine Learning*, pp. 189–195. Morgan Kaufmann.

[9]: Jia Wu, Xiu-Yun Chen, "Hyperparameter Optimization for Machine Learning Models Based on Bayesian Optimization" Journal of Electronic Science and Technology, Volume 17, Issue 1, 2019.

[10]: Feurer, M., & Hutter, F. (2019). Hyperparameter Optimization. Automated Machine Learning.

[11]: Andonie, R. Hyperparameter optimization in learning systems. J Membr Comput 1, 279–291 (2019).

[12]: Frazier, P.I. (2018). Bayesian Optimization. Recent Advances in Optimization and Modeling of Contemporary Problems.

[13]: Komer, B., Bergstra, J., Eliasmith, C. (2019). Hyperopt-Sklearn. In: Hutter, F., Kotthoff, L., Vanschoren, J. (eds) Automated Machine Learning. The Springer Series on Challenges in Machine Learning. Springer

[14]: Lindauer, M., Eggensperger, K., Feurer, M., Biedenkapp, A., Deng, D., Benjamins, C., … Hutter, F. (2022). SMAC3: A Versatile Bayesian Optimization Package for Hyperparameter Optimization.

[15]: Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A Next-generation Hyperparameter Optimization Framework.

[16]: Bergstra, J., & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization.

[17]: Bergstra, J., Bardenet, R., Bengio, Y., & Kégl, B. (2011). Algorithms for Hyper-Parameter Optimization. Neural Information Processing Systems.

[18]: C. J. Watkins and P. Dayan, “Q-learning,” Machine learning, vol. 8, no. 3-4, pp. 279–292, 1992.

[19]: Grefenstette, J. J., Moriarty, D. E., & Schultz, A. C. (1999). Evolutionary algorithms for reinforcement learning. Journal of Artificial Intelligence Research, 11, 241–276.

[20]: Bai, H., Cheng, R., & Jin, Y. (2023). Evolutionary reinforcement learning: A survey. Intelligent Computing.

[21]: Li, P., Hao, J., Tang, H., Fu, X., Zheng, Y., & Tang, K. (2024). Bridging evolutionary algorithms and reinforcement learning: A comprehensive survey on hybrid algorithms.

[22]: Neustroev, G., & de Weerdt, M. M. (2020). Generalized optimistic Q-learning with provable efficiency.

[23]: Levine, S., Kumar, A., Tucker, G., & Fu, J. (2020). Offline reinforcement learning: Tutorial, review, and perspectives on open problems.

[24]: Prudencio, R. F., Maximo, M. R. O. A., & Colombini, E. L. (2023). A survey on offline reinforcement learning: Taxonomy, review, and open problems.

[25]: Sobol, I. M. (1993). Sensitivity estimates for nonlinear mathematical models. *Mathematical Modelling and Computational Experiments*, 1(4), 407-414.

[26]: Saltelli, A. (2002). Making best use of model evaluations to compute sensitivity indices. *Computer Physics Communications*, 145(2), 280-297.

[27]: Saltelli, A., Annoni, P., Azzini, I., Campolongo, F., Ratto, M., & Tarantola, S. (2010). Variance based sensitivity analysis of model output. Design and estimator for the total sensitivity index. *Computer Physics Communications*, 181(2), 259-270.

[28]: Herman, J., & Usher, W. (2017). SALib: An open-source Python library for sensitivity analysis. *Journal of Open Source Software*, 2(9), 97. ---

[29]: Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M., & Tarantola, S. (2008). *Global Sensitivity Analysis: The Primer*. John Wiley & Sons.

[30]: Robino, L., Pacini, E., Garí, Y., Mateos, C., Yannibelli, V., & Monge, D. (2025). Reinforcement learning-based cloud autoscaler initialization via evolutionary algorithms. In Proceedings of the Genetic and Evolutionary Computation Conference Companion (pp. 319–322). Association for Computing Machinery. https://doi.org/10.1145/3712255.3726754

[31]: Robino, L., Garí, Y., Pacini, E., Mateos, C., Yannibelli, V., & Monge, D. (2025). Comparación entre algoritmos evolutivos y Q-Learning para autoescalado de workflows en Cloud. En 54 JAIIO: Jornadas Argentinas de Informática e Investigación Operativa.

[32]: Russell, S. J., & Norvig, P. (2010). Artificial intelligence: A modern approach (3rd ed.). Prentice Hall.

[33]: Deb, Kalyanmoy. Multi-objective optimization using evolutionary algorithms. Vol. 16. John Wiley & Sons, 2001.

[34]: Eiben, A. E., & Smith, J. E. (2015). Introduction to evolutionary computing. Springer.

[35]: Garí, Y., Pacini, E., Robino, L., Mateos, C., & Monge, D.A. (2024). Online rl-based cloud autoscaling for scientific workflows: Evaluation of q-learning and sarsa. Future Generation Computer Systems, 157, 573–586. https://doi.org/10.1016/j.future.2024.04.014.

[36]: Garí, Y., Monge, D.A., Pacini, E., Mateos, C., & García Garino, C. (2021). Reinforcement learning-based application autoscaling in the cloud: A survey. Engineering Applications of Artificial Intelligence, 102, 104288. doi:https://doi.org/10.1016/j.engappai.2021.104288.

[37]: Monge, D.A., Pacini, E., Mateos, C., Alba, E., & Garcia Garino, C. (2020). CMI: An online multi-objective genetic autoscaler for scientific and engineering workflows in cloud infrastructures with unreliable virtual machines. Journal of Network and Computer Applications, 149, 102464. doi:https://doi.org/10.1016/j.jnca.2019.102464.

[38]: Breiman, L. (2001). Random forests. *Machine Learning*, 45, 5–32.


[39] Konidaris, G., Osentoski, S., & Thomas, P. S. (2011). Value function approximation in reinforcement learning using the Fourier basis. In Proceedings of the Twenty-Fifth AAAI Conference on Artificial Intelligence (AAAI).


[40] Watkins, C. J. C. H., & Dayan, P. (1992). Q-learning. Machine Learning, 8(3–4), 279–292. https://doi.org/10.1007/BF00992698.

[41] Li, L., Walsh, T. J., & Littman, M. L. (2006). Towards a unified theory of state abstraction for MDPs. In Proceedings of the 9th International Symposium on Artificial Intelligence and Mathematics (ISAIM).

[42] Kott, A., Théron, P., Drašar, M., Dushku, E., LeBlanc, B., Losiewicz, P., Guarino, A., Mancini, L., Panico, A., Pihelgas, M., Rzadca, K., & De Gaspari, F. (2023). Autonomous intelligent cyber-defense agent (AICA) reference architecture. Release 2.0. arXiv. https://arxiv.org/abs/1803.10664

[43] Rigaki, M., Lukáš, O., Catania, C., & Garcia, S. (2024). Out of the cage: How stochastic parrots win in cyber security environments. Proceedings of the 16th International Conference on Agents and Artificial Intelligence, 774–781. SCITEPRESS – Science and Technology Publications. https://doi.org/10.5220/0012391800003636

[44] Bandhana, A., Lukáš, O., Garcia, S., & Kroupa, T. (2023). Catch me if you can: Improving adversaries in cyber-security with Q-learning algorithms. Proceedings of the 15th International Conference on Agents and Artificial Intelligence, 442–449. SCITEPRESS – Science and Technology Publications. https://doi.org/10.5220/0011684500003393