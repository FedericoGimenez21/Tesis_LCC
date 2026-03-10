# Optimización de Hiperparámetros y Optimización Bayesiana en Algoritmos Genéticos

## 1. Introducción a la Meta-Optimización y Algoritmos Genéticos

En el ámbito de la investigación de operaciones y las ciencias de la computación, los Algoritmos Genéticos (GA, por sus siglas en inglés) se han consolidado como una de las metaheurísticas más poderosas y versátiles para resolver problemas de optimización combinatoria complejos y NP-duros (como problemas de enrutamiento de vehículos, diseño de antenas y optimización de topologías). Inspirados en los procesos biológicos de la selección natural y la evolución, los GA exploran el espacio de soluciones mediante operadores probabilísticos de selección, cruce (crossover) y mutación.

Sin embargo, el rendimiento, la capacidad de convergencia global y la eficiencia computacional de un Algoritmo Genético dependen de manera intrínseca de la correcta configuración de sus parámetros de control o "hiperparámetros". El proceso de encontrar el conjunto óptimo de estos parámetros para un algoritmo de optimización se conoce formalmente como meta-optimización o ajuste de parámetros (parameter tuning).

Tradicionalmente, la configuración de un GA dependía de la intuición humana, metodologías de ensayo y error empíricas, o reglas generales heurísticas. Una selección inadecuada de hiperparámetros puede inducir a una convergencia prematura en óptimos locales (si hay poca diversidad) o a un comportamiento asintótico puramente aleatorio e ineficiente (si la presión de selección es insuficiente o la mutación es excesiva). Los hiperparámetros influyen significativamente en la capacidad de generalización, velocidad de convergencia y rendimiento final del modelo. Por ello, la selección adecuada de hiperparámetros es una etapa crítica del desarrollo de modelos de aprendizaje automático. [1]

Dado que evaluar el rendimiento de un GA en problemas del mundo real es computacionalmente costoso y su naturaleza es inherentemente estocástica, la optimización de sus hiperparámetros representa un desafío de optimización de "caja negra" (black-box). Frente a esto, la Optimización Bayesiana (BO) destaca por su extrema eficiencia muestral para aproximar la topología del rendimiento del GA con una cantidad muy reducida de evaluaciones costosas.

---

## 2. El Problema de la Optimización de Hiperparámetros

### 2.1 Definición formal

El problema de optimización de hiperparámetros (HPO, por sus siglas en inglés) puede formularse como un problema de optimización de caja negra. Dado un algoritmo $\mathcal{A}$ con un vector de hiperparámetros $\boldsymbol{\lambda} \in \Lambda$, donde $\Lambda$ es el espacio de configuraciones admisibles, el objetivo es encontrar la configuración óptima $\boldsymbol{\lambda}^*$ que minimice (o maximice) una función objetivo $f$ [2]:

$$\boldsymbol{\lambda}^* = \arg\min_{\boldsymbol{\lambda} \in \Lambda} f(\boldsymbol{\lambda})$$

donde $f(\boldsymbol{\lambda})$ representa una métrica de rendimiento del algoritmo $\mathcal{A}$ configurado con $\boldsymbol{\lambda}$, evaluada sobre un conjunto de datos o un entorno específico. En el contexto de esta tesis, $\mathcal{A}$ corresponde a un Algoritmo Genético cuya función objetivo $f$ mide la calidad de las políticas evolucionadas para inicializar Q-tables en entornos de ciberseguridad.

La dificultad fundamental de este problema radica en que la función $f$ es típicamente:
- **No derivable**: no existe una expresión analítica cerrada de $f$ respecto a $\boldsymbol{\lambda}$.
- **Costosa de evaluar**: cada evaluación requiere ejecutar el algoritmo completo, posiblemente durante múltiples episodios o generaciones.
- **Ruidosa**: debido a la naturaleza estocástica de los GA, evaluaciones repetidas con la misma configuración $\boldsymbol{\lambda}$ producen resultados distintos.
- **Con espacio de búsqueda mixto**: los hiperparámetros pueden ser continuos, discretos o categóricos [1, 3].

### 2.2 Hiperparámetros vs. parámetros

Es fundamental distinguir entre parámetros e hiperparámetros de un modelo. Los **parámetros** son variables internas que el algoritmo ajusta durante su ejecución (por ejemplo, los pesos de una red neuronal, o los valores Q en una Q-table). Los **hiperparámetros**, en cambio, son variables de configuración establecidas antes de la ejecución del algoritmo y que controlan su comportamiento de aprendizaje [2]. En el contexto de un Algoritmo Genético, los parámetros son los valores de aptitud (*fitness*) de los individuos de la población, mientras que los hiperparámetros incluyen la tasa de mutación, la tasa de cruce, el tamaño de la población, entre otros.

Formalmente, si $\theta$ representa los parámetros del modelo y $\boldsymbol{\lambda}$ los hiperparámetros, el proceso de aprendizaje puede verse como una optimización de dos niveles (*bilevel optimization*) [2]:

$$\boldsymbol{\lambda}^* = \arg\min_{\boldsymbol{\lambda} \in \Lambda} f(\theta^*(\boldsymbol{\lambda}), \boldsymbol{\lambda})$$

$$\text{donde} \quad \theta^*(\boldsymbol{\lambda}) = \arg\min_{\theta} \mathcal{L}(\theta, \boldsymbol{\lambda})$$

En el nivel inferior, el algoritmo optimiza sus parámetros $\theta$ dado un conjunto fijo de hiperparámetros $\boldsymbol{\lambda}$. En el nivel superior, se busca la configuración $\boldsymbol{\lambda}^*$ que produce el mejor rendimiento global.

---

## 3. Hiperparámetros Críticos de los Algoritmos Genéticos

Los Algoritmos Genéticos poseen un conjunto de hiperparámetros cuya interacción determina el balance entre exploración (búsqueda global del espacio de soluciones) y explotación (refinamiento de las mejores soluciones encontradas). A continuación, se describen los hiperparámetros más relevantes.

### 3.1 Tamaño de la población ($N$)

El tamaño de la población determina el número de individuos (soluciones candidatas) que coexisten en cada generación. Una población grande incrementa la diversidad genética y reduce el riesgo de convergencia prematura, pero aumenta proporcionalmente el costo computacional por generación. Una población demasiado pequeña puede llevar a una pérdida rápida de diversidad y al estancamiento en óptimos locales [3].

### 3.2 Tasa de cruce ($p_c$)

La tasa de cruce (o crossover rate) es la probabilidad de que dos individuos padres intercambien material genético para producir nuevos descendientes. Valores típicos se encuentran en el rango $p_c \in [0.6, 0.9]$. Una tasa alta favorece la combinación de bloques constructivos (*building blocks*) de buenas soluciones, mientras que una tasa baja preserva más individuos intactos de una generación a la siguiente.

### 3.3 Tasa de mutación ($p_m$)

La tasa de mutación es la probabilidad de que un gen individual sea alterado de forma aleatoria. Actúa como el principal mecanismo para mantener la diversidad genética y prevenir la convergencia prematura. Valores típicos son pequeños, en el rango $p_m \in [0.001, 0.1]$. Una mutación excesiva degrada la búsqueda a un paseo aleatorio, mientras que una mutación insuficiente puede llevar al estancamiento [3].

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

### 4.1 Búsqueda manual y ensayo-error

El enfoque más elemental consiste en que un experto humano ajuste los hiperparámetros iterativamente basándose en su intuición y experiencia. Aunque puede ser efectivo cuando el practicante tiene conocimiento profundo del dominio, este método es inherentemente subjetivo, no reproducible y no escala a espacios de alta dimensionalidad [2].

### 4.2 Búsqueda por cuadrícula (Grid Search)

La búsqueda por cuadrícula discretiza cada dimensión del espacio de hiperparámetros en un conjunto finito de valores y evalúa todas las combinaciones posibles. Para $d$ hiperparámetros, cada uno con $k$ valores candidatos, se requieren $k^d$ evaluaciones. Su principal limitación es que sufre de la *maldición de la dimensionalidad*: el número de evaluaciones crece exponencialmente con el número de hiperparámetros, lo que la hace impracticable para espacios de más de 3-4 dimensiones [2].

### 4.3 Búsqueda aleatoria (Random Search)

Propuesta por Bergstra y Bengio (2012), la búsqueda aleatoria muestrea configuraciones uniformemente al azar del espacio de hiperparámetros. Bergstra y Bengio demostraron teórica y empíricamente que, cuando solo un subconjunto de hiperparámetros tiene influencia significativa en el rendimiento (lo cual es frecuente en la práctica), la búsqueda aleatoria es más eficiente que la búsqueda por cuadrícula, ya que explora más valores únicos de cada hiperparámetro relevante con el mismo presupuesto de evaluaciones [2, 3].

Sin embargo, tanto Grid Search como Random Search tratan cada evaluación como independiente, sin utilizar información de evaluaciones previas para guiar la búsqueda. Esto las convierte en estrategias pasivas que no aprenden del historial de evaluaciones.

---

## 5. Optimización Bayesiana

### 5.1 Fundamento conceptual

La Optimización Bayesiana (BO) es un marco de optimización secuencial basado en modelos (*Sequential Model-Based Optimization*, SMBO) diseñado para la optimización eficiente de funciones de caja negra costosas de evaluar [4]. La idea fundamental es construir un modelo sustituto probabilístico (*surrogate model*) de la función objetivo $f(\boldsymbol{\lambda})$ y utilizar este modelo para decidir de manera informada dónde evaluar a continuación, maximizando la información obtenida por cada evaluación costosa.

A diferencia de Grid Search o Random Search, la Optimización Bayesiana es una estrategia **activa** que utiliza toda la información recopilada en evaluaciones previas para construir y actualizar un modelo estadístico de $f$, guiando la búsqueda de manera inteligente hacia regiones prometedoras del espacio de configuraciones [4].

### 5.2 Formulación del marco SMBO

El proceso iterativo de la Optimización Bayesiana se describe mediante el siguiente ciclo [4]:

1. **Inicialización**: Se evalúa $f$ en un conjunto inicial pequeño de configuraciones $\mathcal{D}_0 = \{(\boldsymbol{\lambda}_1, y_1), ..., (\boldsymbol{\lambda}_n, y_n)\}$, donde $y_i = f(\boldsymbol{\lambda}_i) + \epsilon$ y $\epsilon$ captura el ruido de evaluación.

2. **Construcción del modelo sustituto**: Con los datos $\mathcal{D}_t$ disponibles en la iteración $t$, se ajusta un modelo probabilístico $\mathcal{M}_t$ que proporciona, para cada punto $\boldsymbol{\lambda}$ del espacio, una distribución predictiva $p(y | \boldsymbol{\lambda}, \mathcal{D}_t)$ con media $\mu(\boldsymbol{\lambda})$ y varianza $\sigma^2(\boldsymbol{\lambda})$.

3. **Maximización de la función de adquisición**: Se selecciona el siguiente punto a evaluar como $\boldsymbol{\lambda}_{t+1} = \arg\max_{\boldsymbol{\lambda} \in \Lambda} \alpha(\boldsymbol{\lambda} | \mathcal{M}_t)$, donde $\alpha$ es una función de adquisición que cuantifica la utilidad esperada de evaluar en $\boldsymbol{\lambda}$.

4. **Evaluación y actualización**: Se evalúa $y_{t+1} = f(\boldsymbol{\lambda}_{t+1})$, se actualiza el conjunto de datos $\mathcal{D}_{t+1} = \mathcal{D}_t \cup \{(\boldsymbol{\lambda}_{t+1}, y_{t+1})\}$, y se reconstruye el modelo sustituto.

5. **Criterio de parada**: Se repite el ciclo hasta agotar el presupuesto de evaluaciones o alcanzar un criterio de convergencia.

### 5.3 Modelos sustitutos (*Surrogate Models*)

#### 5.3.1 Procesos Gaussianos (GP)

El modelo sustituto más utilizado en la Optimización Bayesiana clásica es el **Proceso Gaussiano** (*Gaussian Process*, GP) [4]. Un GP define una distribución sobre funciones, de forma que cualquier conjunto finito de puntos sigue una distribución normal multivariante:

$$f(\boldsymbol{\lambda}) \sim \mathcal{GP}(m(\boldsymbol{\lambda}), k(\boldsymbol{\lambda}, \boldsymbol{\lambda}'))$$

donde:
- $m(\boldsymbol{\lambda})$ es la función de media (frecuentemente se asume $m(\boldsymbol{\lambda}) = 0$).
- $k(\boldsymbol{\lambda}, \boldsymbol{\lambda}')$ es la función de covarianza o *kernel* que codifica supuestos sobre la suavidad y estructura de $f$.

Dado el conjunto de observaciones $\mathcal{D}_t = \{(\boldsymbol{\lambda}_i, y_i)\}_{i=1}^{t}$, la distribución predictiva posterior en un punto nuevo $\boldsymbol{\lambda}_*$ es analíticamente tratable:

$$\mu(\boldsymbol{\lambda}_*) = \mathbf{k}_*^T (\mathbf{K} + \sigma_n^2 \mathbf{I})^{-1} \mathbf{y}$$

$$\sigma^2(\boldsymbol{\lambda}_*) = k(\boldsymbol{\lambda}_*, \boldsymbol{\lambda}_*) - \mathbf{k}_*^T (\mathbf{K} + \sigma_n^2 \mathbf{I})^{-1} \mathbf{k}_*$$

donde $\mathbf{K}$ es la matriz de covarianza entre las observaciones, $\mathbf{k}_*$ es el vector de covarianzas entre $\boldsymbol{\lambda}_*$ y las observaciones, y $\sigma_n^2$ es la varianza del ruido.

Los GP ofrecen estimaciones calibradas de incertidumbre, lo que los hace ideales para guiar la exploración. Su principal limitación es la complejidad computacional $\mathcal{O}(n^3)$ para la inversión de la matriz de covarianza, lo que los hace menos adecuados cuando el número de evaluaciones es muy grande [4].

#### 5.3.2 Tree-structured Parzen Estimator (TPE)

Una alternativa popular a los GP es el **Tree-structured Parzen Estimator** (TPE), propuesto por Bergstra et al. (2011) e implementado en la librería Hyperopt. En lugar de modelar $p(y | \boldsymbol{\lambda})$ directamente, el TPE modela las densidades condicionales $\ell(\boldsymbol{\lambda}) = p(\boldsymbol{\lambda} | y < y^*)$ y $g(\boldsymbol{\lambda}) = p(\boldsymbol{\lambda} | y \geq y^*)$, donde $y^*$ es un umbral que separa evaluaciones "buenas" de "malas" [2]. La función de adquisición EI se maximiza al maximizar la razón $\ell(\boldsymbol{\lambda}) / g(\boldsymbol{\lambda})$, lo que favorece regiones donde la densidad de buenas configuraciones es alta respecto a las malas.

El TPE maneja naturalmente espacios condicionales y jerárquicos, lo que lo hace particularmente adecuado para hiperparámetros con dependencias estructurales (como elegir *tipo de selección* y luego *tamaño de torneo* solo si el tipo es torneo).

#### 5.3.3 Random Forests (SMAC)

El framework **SMAC** (*Sequential Model-based Algorithm Configuration*) utiliza Random Forests como modelo sustituto. Los Random Forests estiman la media y varianza de la función objetivo mediante un ensamble de árboles de decisión, lo que los hace robustos ante hiperparámetros categóricos y espacios de alta dimensionalidad [2]. SMAC es particularmente útil cuando el espacio de configuración incluye una mezcla compleja de tipos de hiperparámetros.

### 5.4 Funciones de adquisición

Las funciones de adquisición formalizan el compromiso entre exploración (evaluar en regiones de alta incertidumbre) y explotación (evaluar cerca de las mejores soluciones conocidas). Las más utilizadas son [4]:

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

1. **Evaluaciones costosas**: Cada evaluación de una configuración de hiperparámetros de un GA requiere ejecutar el algoritmo completo durante múltiples generaciones, lo cual puede tardar minutos u horas. La eficiencia muestral de la BO es crítica en este contexto [4].

2. **Estocasticidad inherente**: Los GA son algoritmos inherentemente estocásticos, por lo que la función objetivo $f(\boldsymbol{\lambda})$ es ruidosa. Los modelos probabilísticos de la BO (especialmente los GP) manejan naturalmente esta incertidumbre.

3. **Interacciones complejas**: Como se discutió en la Sección 3.6, los hiperparámetros de un GA interactúan de formas no triviales. La BO captura estas interacciones a través de su modelo sustituto, a diferencia de métodos que asumen independencia entre dimensiones.

4. **Espacio de búsqueda mixto**: Los GA poseen hiperparámetros de naturaleza diversa (continuos como $p_m$, discretos como $N$, categóricos como el tipo de selección), un escenario que los modelos sustitutos como TPE y SMAC manejan de forma nativa [2].

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

---

## 7. Consideraciones Prácticas y Herramientas

### 7.1 Frameworks de Optimización Bayesiana

Existen múltiples frameworks de código abierto que implementan las técnicas descritas:

- **Optuna**: Framework moderno que implementa TPE y otros samplers, con soporte para pruning de evaluaciones subóptimas y paralelización.
- **Hyperopt**: Implementación original de TPE con soporte para espacios de búsqueda condicionales.
- **Scikit-Optimize (skopt)**: Implementación basada en Procesos Gaussianos, integrable con scikit-learn.
- **SMAC3**: Implementación del framework SMAC con Random Forests, especialmente adecuada para configuración de algoritmos.


### 7.2 Restricciones computacionales

En aplicaciones prácticas, el presupuesto total de evaluaciones es limitado. La Optimización Bayesiana es especialmente ventajosa cuando el número total de evaluaciones es reducido (típicamente entre 20 y 200 evaluaciones), ya que su eficiencia muestral permite obtener configuraciones competitivas con un presupuesto que sería insuficiente para Grid Search o incluso para Random Search [4].

---

## 8. Conclusiones del Estado del Arte

La optimización de hiperparámetros de Algoritmos Genéticos mediante Optimización Bayesiana representa un enfoque riguroso y eficiente para el problema de meta-optimización. Los principales puntos de este análisis son:

1. Los hiperparámetros de un GA (tamaño de población, tasas de cruce y mutación, mecanismo de selección, número de generaciones) interactúan de formas complejas, haciendo inadecuados los métodos de ajuste manual o unidimensionales.

2. La Optimización Bayesiana, a través de sus modelos sustitutos (GP, TPE, Random Forests) y funciones de adquisición (EI, PI, UCB), ofrece un marco matemáticamente fundamentado para navegar espacios de hiperparámetros mixtos y de alta dimensionalidad con eficiencia muestral superior.

3. La naturaleza estocástica y el alto costo computacional de los GA los convierten en candidatos ideales para la BO, que maximiza la información obtenida por cada evaluación costosa.

4. En el contexto específico de esta tesis —donde un GA evoluciona políticas para inicializar Q-tables en entornos de ciberseguridad— la capacidad de la BO para optimizar con pocas evaluaciones es particularmente valiosa, dada la complejidad de las simulaciones en entornos como NetSecGame.



---

# Referencias

[1]: Jia Wu, Xiu-Yun Chen, "Hyperparameter Optimization for Machine Learning Models Based on Bayesian Optimization" Journal of Electronic Science and Technology, Volume 17, Issue 1, 2019.

[2]: Feurer, M., & Hutter, F. (2019). Hyperparameter Optimization. Automated Machine Learning.

[3]: Andonie, R. Hyperparameter optimization in learning systems. J Membr Comput 1, 279–291 (2019).

[4]: Frazier, P.I. (2018). Bayesian Optimization. Recent Advances in Optimization and Modeling of Contemporary Problems.

