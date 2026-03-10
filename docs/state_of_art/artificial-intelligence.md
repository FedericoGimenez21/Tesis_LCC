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
- **Sensibilidad a hiperparámetros**: El rendimiento depende críticamente de la configuración de hiperparámetros ($N$, $p_c$, $p_m$, $G$, mecanismo de selección), cuya optimización constituye un problema de meta-optimización no trivial (desarrollado en el documento de Optimización Bayesiana).
- **Convergencia prematura**: Si la presión selectiva es excesiva o la diversidad genética se agota rápidamente, el algoritmo puede converger a un óptimo local antes de explorar suficientemente el espacio de búsqueda [6].
- **Costo computacional**: Cada generación requiere evaluar la función de aptitud de $N$ individuos, lo que puede ser prohibitivo cuando las evaluaciones son costosas (como simulaciones en entornos complejos de ciberseguridad).

### Complementariedad entre Algoritmos Genéticos y Aprendizaje por Refuerzo

La intersección entre los Algoritmos Genéticos y el Aprendizaje por Refuerzo constituye un área activa de investigación con una rica historia que se remonta a los trabajos pioneros de Grefenstette et al. [8]. Ambos paradigmas buscan optimizar el comportamiento de un agente en un entorno, pero desde perspectivas complementarias:

| Dimensión | Aprendizaje por Refuerzo (Q-Learning) | Algoritmos Genéticos |
|-----------|---------------------------------------|---------------------|
| Unidad de aprendizaje | Un agente individual | Una población de soluciones |
| Mecanismo de mejora | Actualización incremental de valores Q | Evolución generacional por selección y recombinación |
| Uso de la señal de recompensa | Paso a paso (TD error) | Episódica (fitness acumulado) |
| Exploración | Epsilon-greedy, UCB, etc. | Mutación y cruce |
| Representación del conocimiento | Q-table o aproximador de funciones | Cromosoma (política codificada) |

Esta complementariedad sugiere que combinar ambos enfoques —utilizando la evolución para generar políticas iniciales informadas que luego se refinan mediante Q-Learning— puede superar las limitaciones individuales de cada paradigma. En particular, los GA pueden proporcionar una exploración global eficiente del espacio de políticas, mientras que el Q-Learning ofrece un refinamiento local preciso basado en experiencia secuencial [8].



# Bibliografía 

1. Russell, S. & Norvig, P. (2021). Artificial Intelligence, Global Edition. (4th ed.). Pearson Education.
2. Mitchell, T. M. (1997). Machine Learning (Vol. 1). McGraw-Hill.
3. Sutton, R. S., Barto, A. G. (2018). Reinforcement Learning: An Introduction. The MIT Press.
4. Holland, J. H. (1975). Adaptation in Natural and Artificial Systems. University of Michigan Press. (Reeditado por MIT Press, 1992).
5. Goldberg, D. E. (1989). Genetic Algorithms in Search, Optimization, and Machine Learning. Addison-Wesley.
6. Katoch, S., Chauhan, S. S., & Kumar, V. (2021). A review on genetic algorithm: past, present, and future. *Multimedia Tools and Applications*, 80, 8091–8126. Springer. https://doi.org/10.1007/s11042-020-10139-6
7. Lambora, A., Gupta, K., & Chopra, K. (2019). Genetic Algorithm – A Literature Review. *International Conference on Machine Learning, Big Data, Cloud and Parallel Computing (COMITCon)*, pp. 380–384. IEEE. https://doi.org/10.1109/COMITCon.2019.8862255
8. Grefenstette, J. J. & Ramsey, C. L. (1992). An Approach to Anytime Learning. *Proceedings of the Ninth International Conference on Machine Learning*, pp. 189–195. Morgan Kaufmann.