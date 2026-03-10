# Análisis de Sensibilidad Global: Métodos de Sobol y Saltelli

## Referencia Principal

> Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M., & Tarantola, S. (2008). *Global Sensitivity Analysis: The Primer*. John Wiley & Sons.

---

## 1. Introducción al Análisis de Sensibilidad Global

El **análisis de sensibilidad** estudia cómo la incertidumbre en la salida de un modelo puede ser atribuida a diferentes fuentes de incertidumbre en las entradas del modelo. A diferencia del análisis de sensibilidad local (que examina el efecto de pequeñas perturbaciones alrededor de un punto), el **análisis de sensibilidad global (GSA)** explora todo el espacio de entrada de los factores.

### 1.1 Definición Formal

Dado un modelo $Y = f(X_1, X_2, ..., X_k)$ donde:
- $Y$ es la salida del modelo (escalar)
- $X_i$ son los $k$ factores de entrada (variables independientes)

El objetivo del GSA es cuantificar la contribución de cada factor $X_i$ (y sus interacciones) a la varianza total de $Y$.

### 1.2 Motivación

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

### 3.2 Esquema de Muestreo de Saltelli

Saltelli (2002) propuso un esquema eficiente basado en dos matrices de muestreo:

**Paso 1**: Generar dos matrices independientes $\mathbf{A}$ y $\mathbf{B}$ de dimensión $N \times k$, donde cada fila representa una muestra y cada columna un factor.

**Paso 2**: Construir matrices $\mathbf{A}_B^{(i)}$ donde la columna $i$-ésima proviene de $\mathbf{B}$ y las demás de $\mathbf{A}$.

**Paso 3**: Evaluar el modelo en todas las matrices:
- $f(\mathbf{A})$: vector de $N$ evaluaciones
- $f(\mathbf{B})$: vector de $N$ evaluaciones  
- $f(\mathbf{A}_B^{(i)})$: vector de $N$ evaluaciones para cada $i$

### 3.3 Estimadores de Saltelli

**Estimador de $S_i$ (primer orden)**:

$$\hat{S}_i = \frac{\frac{1}{N}\sum_{j=1}^{N} f(\mathbf{B})_j \left( f(\mathbf{A}_B^{(i)})_j - f(\mathbf{A})_j \right)}{\hat{V}(Y)}$$

**Estimador de $S_{Ti}$ (total)**:

$$\hat{S}_{Ti} = \frac{\frac{1}{2N}\sum_{j=1}^{N} \left( f(\mathbf{A})_j - f(\mathbf{A}_B^{(i)})_j \right)^2}{\hat{V}(Y)}$$

**Varianza total**:

$$\hat{V}(Y) = \frac{1}{N-1}\sum_{j=1}^{N} \left( f(\mathbf{A})_j - \bar{f} \right)^2$$

### 3.4 Número Total de Muestras

Para el esquema de Saltelli:
- **Sin índices de segundo orden**: $N \times (k + 2)$ evaluaciones
- **Con índices de segundo orden**: $N \times (2k + 2)$ evaluaciones

**Ejemplo**: Con $N = 1024$ y $k = 6$ factores:
- Sin segundo orden: $1024 \times 8 = 8,192$ evaluaciones
- Con segundo orden: $1024 \times 14 = 14,336$ evaluaciones

---

## 4. Implementación en SALib

La biblioteca **SALib** (Sensitivity Analysis Library) implementa los métodos de Saltelli y Sobol. El flujo típico es:

### 4.1 Definición del Problema

```python
problem = {
    'num_vars': 6,
    'names': ['population_size', 'n_generations', 'sbx_prob', 
              'sbx_eta', 'pm_prob_var', 'pm_eta'],
    'bounds': [
        [10, 20],      # population_size
        [10, 20],      # n_generations
        [0.8, 1.0],    # sbx_prob
        [0, 60],       # sbx_eta
        [0.01, 0.6],   # pm_prob_var
        [0, 60]        # pm_eta
    ]
}
```

### 4.2 Generación de Muestras (Saltelli)

```python
from SALib.sample import saltelli

param_values = saltelli.sample(problem, N=1024, calc_second_order=True)
# Genera N*(2k+2) = 1024*14 = 14,336 muestras
```

### 4.3 Evaluación del Modelo

```python
Y = np.zeros(len(param_values))
for i, params in enumerate(param_values):
    Y[i] = evaluate_model(params)  # Ejecutar GA y obtener win_rate
```

### 4.4 Análisis de Sobol

```python
from SALib.analyze import sobol

Si = sobol.analyze(problem, Y, calc_second_order=True)
# Retorna: S1, S1_conf, ST, ST_conf, S2, S2_conf
```

### 4.5 Funcionamiento Detallado de `sobol.analyze()`

La función `sobol.analyze()` es el núcleo del análisis de sensibilidad en SALib. A continuación se describe su funcionamiento interno:

#### 4.5.1 Firma de la Función

```python
sobol.analyze(problem, Y, calc_second_order=True, num_resamples=100, 
              conf_level=0.95, print_to_console=False, seed=None)
```

**Parámetros principales**:
| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `problem` | `dict` | Diccionario con `num_vars`, `names` y `bounds` |
| `Y` | `np.ndarray` | Vector de salidas del modelo (shape: `N*(2k+2)` o `N*(k+2)`) |
| `calc_second_order` | `bool` | Si `True`, calcula índices de interacción $S_{ij}$ |
| `num_resamples` | `int` | Número de remuestreos bootstrap para intervalos de confianza |
| `conf_level` | `float` | Nivel de confianza para los intervalos (default: 0.95) |
| `seed` | `int` | Semilla para reproducibilidad del bootstrap |

#### 4.5.2 Estructura Interna del Algoritmo

**Paso 1: Validación y Reestructuración de Datos**

La función primero valida que el tamaño de `Y` sea consistente con el esquema de muestreo de Saltelli:

```python
# Verificación interna
if calc_second_order:
    expected_size = N * (2 * k + 2)
else:
    expected_size = N * (k + 2)
```

**Paso 2: Separación de Matrices de Evaluación**

El vector `Y` se reestructura en las evaluaciones correspondientes a cada matriz:

$$Y = [f(\mathbf{A}), f(\mathbf{B}), f(\mathbf{A}_B^{(1)}), ..., f(\mathbf{A}_B^{(k)}), f(\mathbf{B}_A^{(1)}), ..., f(\mathbf{B}_A^{(k)})]$$

Internamente:
```python
# Pseudocódigo de la separación
A = Y[0:N]           # Evaluaciones de matriz A
B = Y[N:2*N]         # Evaluaciones de matriz B
AB = Y[2*N:].reshape(k, N)  # Matrices A_B^(i)
```

**Paso 3: Cálculo de Índices de Primer Orden ($S_1$)**

Se aplica el estimador de Saltelli (2010):

$$\hat{S}_i = \frac{\frac{1}{N}\sum_{j=1}^{N} f(\mathbf{B})_j \cdot f(\mathbf{A}_B^{(i)})_j - f_0^2}{\hat{V}(Y)}$$

donde $f_0 = \frac{1}{2N}\sum_{j=1}^{N}(f(\mathbf{A})_j + f(\mathbf{B})_j)$

**Paso 4: Cálculo de Índices Totales ($S_T$)**

Se utiliza el estimador de Jansen (1999):

$$\hat{S}_{Ti} = \frac{\frac{1}{2N}\sum_{j=1}^{N} \left( f(\mathbf{A})_j - f(\mathbf{A}_B^{(i)})_j \right)^2}{\hat{V}(Y)}$$

**Paso 5: Cálculo de Índices de Segundo Orden ($S_2$)** (si `calc_second_order=True`)

$$\hat{S}_{ij} = \frac{V_{ij}}{V(Y)} - S_i - S_j$$

donde $V_{ij}$ se estima usando las matrices $\mathbf{B}_A^{(i)}$.

**Paso 6: Bootstrap para Intervalos de Confianza**

Se aplica remuestreo bootstrap para estimar la incertidumbre:

```python
for _ in range(num_resamples):
    idx = np.random.randint(0, N, N)  # Muestreo con reemplazo
    S1_boot[i] = compute_S1(Y[idx])
    ST_boot[i] = compute_ST(Y[idx])

S1_conf = np.percentile(S1_boot, [alpha/2, 1-alpha/2])
```

#### 4.5.3 Estructura del Resultado

La función retorna un diccionario `SALib.util.ResultDict` con:

```python
{
    'S1': np.ndarray,      # Índices de primer orden (shape: k)
    'S1_conf': np.ndarray, # Intervalos de confianza de S1 (shape: k)
    'ST': np.ndarray,      # Índices totales (shape: k)
    'ST_conf': np.ndarray, # Intervalos de confianza de ST (shape: k)
    'S2': np.ndarray,      # Índices de segundo orden (shape: k×k) [opcional]
    'S2_conf': np.ndarray  # Intervalos de confianza de S2 (shape: k×k) [opcional]
}
```


---

## 5. Interpretación de Resultados

### 5.1 Índices de Primer Orden ($S_1$)

| Valor de $S_i$ | Interpretación |
|----------------|----------------|
| $S_i > 0.5$ | Factor altamente influyente |
| $0.1 < S_i < 0.5$ | Factor moderadamente influyente |
| $S_i < 0.1$ | Factor poco influyente por sí solo |

### 5.2 Índices Totales ($S_T$)

| Valor de $S_{Ti}$ | Interpretación |
|-------------------|----------------|
| $S_{Ti} > 0.5$ | Factor crítico (considerar para optimización) |
| $0.05 < S_{Ti} < 0.5$ | Factor relevante |
| $S_{Ti} < 0.05$ | Factor fijable (Factor Fixing) |

### 5.3 Índice de Interacción ($S_T - S_1$)

| Valor | Interpretación |
|-------|----------------|
| $S_{Ti} - S_i \approx 0$ | Sin interacciones significativas |
| $S_{Ti} - S_i > 0.1$ | Interacciones importantes con otros factores |
| $S_{Ti} >> S_i$ | El factor actúa principalmente a través de interacciones |

### 5.4 Suma de Índices de Primer Orden

$$\sum_{i=1}^{k} S_i$$

| Valor | Interpretación |
|-------|----------------|
| $\approx 1$ | Modelo aditivo (sin interacciones) |
| $< 0.7$ | Presencia significativa de interacciones |
| $< 0.5$ | Modelo dominado por interacciones |

---

## 6. Consideraciones Prácticas

### 6.1 Tamaño de Muestra Recomendado

Según Saltelli et al. (2008):
- **Mínimo**: $N = 500$ para estimaciones preliminares
- **Recomendado**: $N = 1000$ para resultados confiables
- **Alto**: $N > 2000$ para alta precisión en índices pequeños

### 6.2 Convergencia de Estimadores

Los intervalos de confianza (`S1_conf`, `ST_conf`) indican la incertidumbre en los estimadores:
- Intervalos amplios → Aumentar $N$
- Valores negativos de $S_i$ → Inestabilidad numérica, aumentar $N$

### 6.3 Distribución de Entrada

El método asume distribuciones uniformes en los rangos especificados. Para otras distribuciones:
- Transformar las muestras uniformes a la distribución deseada
- Usar `SALib.sample.latin` para Latin Hypercube Sampling

### 6.4 Limitaciones

1. **Costo computacional**: Requiere miles de evaluaciones del modelo
2. **Independencia**: Asume factores de entrada independientes
3. **Monotonicidad**: Puede subestimar efectos no monótonos
4. **Varianza finita**: Requiere que $Y$ tenga varianza finita

---

## 7. Aplicación al Algoritmo Genético

En el contexto del script `sensitivity_analysis.py`, el análisis de sensibilidad se aplica a los hiperparámetros del algoritmo genético:

### 7.1 Factores Analizados

| Factor | Descripción | Rango |
|--------|-------------|-------|
| `population_size` | Tamaño de la población del GA | [10, 20] |
| `n_generations` | Número de generaciones | [10, 20] |
| `sbx_prob` | Probabilidad de cruce SBX | [0.8, 1.0] |
| `sbx_eta` | Índice de distribución SBX | [0, 60] |
| `pm_prob_var` | Probabilidad de mutación por variable | [0.01, 0.6] |
| `pm_eta` | Índice de distribución de mutación polinomial | [0, 60] |

### 7.2 Salida del Modelo

$$Y = \text{win\_rate}(\text{Q-table optimizada por GA})$$

El win_rate representa el porcentaje de victorias del agente Q-learning usando la Q-table generada por el GA con los hiperparámetros dados.

### 7.3 Objetivo del Análisis

1. **Identificar** qué hiperparámetros del GA tienen mayor impacto en el rendimiento
2. **Priorizar** esfuerzos de tuning en los factores más influyentes
3. **Simplificar** fijando factores no influyentes en valores por defecto
4. **Detectar** interacciones importantes entre hiperparámetros

---

## 8. Referencias Adicionales

1. Sobol', I. M. (1993). Sensitivity estimates for nonlinear mathematical models. *Mathematical Modelling and Computational Experiments*, 1(4), 407-414.

2. Saltelli, A. (2002). Making best use of model evaluations to compute sensitivity indices. *Computer Physics Communications*, 145(2), 280-297.

3. Saltelli, A., Annoni, P., Azzini, I., Campolongo, F., Ratto, M., & Tarantola, S. (2010). Variance based sensitivity analysis of model output. Design and estimator for the total sensitivity index. *Computer Physics Communications*, 181(2), 259-270.

4. Herman, J., & Usher, W. (2017). SALib: An open-source Python library for sensitivity analysis. *Journal of Open Source Software*, 2(9), 97.

---

## Apéndice A: Fórmulas Resumidas

### Índices de Sobol

| Índice | Fórmula | Interpretación |
|--------|---------|----------------|
| $S_i$ | $\frac{V[E(Y\|X_i)]}{V(Y)}$ | Efecto principal de $X_i$ |
| $S_{Ti}$ | $1 - \frac{V[E(Y\|X_{\sim i})]}{V(Y)}$ | Efecto total de $X_i$ |
| $S_{ij}$ | $\frac{V[E(Y\|X_i,X_j)] - V_i - V_j}{V(Y)}$ | Interacción $X_i \times X_j$ |

### Propiedades

$$\sum_{i} S_i + \sum_{i<j} S_{ij} + ... + S_{1,...,k} = 1$$

$$S_{Ti} = S_i + \sum_{j \neq i} S_{ij} + \sum_{j \neq i, l \neq i, j < l} S_{ijl} + ...$$

---