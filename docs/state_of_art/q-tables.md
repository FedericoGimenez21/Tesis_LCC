# Técnicas fundamentales de inicialización de Q-Tables en el aprendizaje por refuerzo

## Resumen ejecutivo

Q-Learning es un algoritmo central en el aprendizaje por refuerzo sin modelo, ampliamente utilizado para resolver problemas de toma de decisiones secuenciales en entornos inciertos. Su objetivo principal es permitir que un agente aprenda una política óptima —es decir, una estrategia de acciones que maximice la recompensa acumulada— dentro de un Proceso de Decisión de Markov (MDP). Para lograrlo, el algoritmo mantiene una Q-Table, una estructura de datos que almacena los valores Q, los cuales representan la recompensa esperada al ejecutar una acción específica en un determinado estado y seguir una política óptima a futuro. Estos valores se actualizan iterativamente utilizando la ecuación de Bellman, lo que permite que el agente mejore progresivamente su comportamiento mediante prueba y error, sin necesidad de conocer previamente el modelo del entorno [1]. Un aspecto crítico del proceso es la inicialización de la Q-Table, ya que los valores asignados inicialmente determinan la estrategia de exploración temprana del agente y, en consecuencia, afectan la velocidad de convergencia y la eficacia del aprendizaje. Entre las técnicas más comunes se encuentran la inicialización con ceros, con valores aleatorios pequeños o con valores optimistas. Cada una de estas estrategias influye directamente en el equilibrio entre exploración y explotación, así como en la dinámica general del proceso de aprendizaje.

Este informe detallará estas técnicas, y sus fundamentos teóricos. 

## Tecnicas principales de inicializacion de Q-tables


### Inicialización a ceros

Esta es la técnica de inicialización más directa y, por ende, la más común en la práctica del Q-Learning. Consiste en establecer todas las entradas de la Q-Table en un valor de cero [2]. La justificación de esta práctica radica en que, al inicio del proceso de aprendizaje, el agente carece de cualquier información o conocimiento sobre las recompensas esperadas de las acciones en los diferentes estados. Por lo tanto, un valor neutral de cero sirve como un punto de partida imparcial. 

Cuando todos los valores Q son cero, el agente no tiene una preferencia intrínseca por ninguna acción en un estado dado. En ausencia de otros mecanismos de exploración, esto puede llevar a que el agente elija acciones de manera puramente aleatoria. Esta aleatoriedad inicial es a menudo gestionada por políticas de exploración como la estrategia epsilon-greedy, donde el agente elige una acción aleatoria con una probabilidad ε.

Este sesgo, aunque no impide la convergencia a largo plazo en espacios de estados discretos si se garantiza suficiente exploración , puede afectar la eficiencia del aprendizaje inicial. Podría ralentizar el descubrimiento de rutas óptimas si la acción preferida por defecto no es la mejor, o si se necesitan múltiples exploraciones para corregir este sesgo inicial

### Inicialización con valores aleatorios

Una alternativa a la inicialización a ceros es establecer los valores Q iniciales como números aleatorios dentro de un rango limitado (por ejemplo, entre [-k, k] o [0, k], siendo k un valor real pequeño típicamente ≤ 0.5). Esta práctica se alinea con las recomendaciones de Sutton y Barto [2] donde señalan que:  

><em>“Initialize Q(s,a) arbitrarily…”</em>
- Donde "arbitrariamente" incluye explícitamente valores aleatorios pequeños 

Sus principales ventajas son romper la simetría inicial y prevenir preferencias prematuras hacia acciones específicas, fomentando exploración diversificada en etapas tempranas del aprendizaje. Al asignar valores ligeramente distintos a cada par estado-acción, se eliminan empates iniciales que ocurren con la inicialización a cero. Esto evita que el agente seleccione siempre la misma acción por defecto (ej: la primera en el orden de procesamiento) cuando múltiples acciones tienen valores idénticos.

### Inicialización optimista

La inicialización optimista es una técnica utilizada en el aprendizaje por refuerzo, específicamente en algoritmos de aprendizaje de valores como Q-learning. Consiste en asignar valores iniciales elevados a la función de valor acción-estado, Q(s,a), antes de que el agente comience a interactuar con el entorno. En otras palabras, se le da al agente una expectativa "optimista" sobre las recompensas futuras de todas las acciones en cualquier estado. Esto significa que el agente, al principio, creerá que cualquier acción que tome en un estado dado le reportará una recompensa muy alta.


La principal ventaja de este enfoque es que fomenta una exploración exhaustiva inicial. Incluso si el agente utiliza una política puramente codiciosa (greedy), que normalmente lo llevaría a explotar rápidamente las acciones que parecen más prometedoras, la inicialización optimista lo impulsa a probar todas las acciones suficientes veces. Esto ocurre porque todas las estimaciones iniciales de Q(s,a) son muy altas. Para que el agente "confíe" en que una acción es realmente peor que otra, debe explorar y experimentar recompensas reales que disminuyan su valor Q(s,a) estimado. Este comportamiento es fundamental para garantizar que no se pasen por alto acciones potencialmente óptimas, un concepto bien documentado por Sutton y Barto [2]. 

Sin embargo, la inicialización optimista introduce un hiperparámetro adicional: el nivel de optimismo, es decir, cuán alto se deben inicializar los valores de Q(s,a). Elegir el valor óptimo es crucial y depende del problema específico. Si el valor inicial es demasiado alto, el agente podría dedicar un tiempo excesivo a explorar acciones subóptimas, lo que ralentizaría la convergencia. Por el contrario, si es demasiado bajo, no se logrará una exploración inicial suficiente, y el agente podría converger prematuramente a una política subóptima. Una heurística común es inicializar Q(s,a) con un valor cercano al máximo teórico posible de la recompensa acumulada.

En entornos no estacionarios, donde las recompensas o las transiciones del entorno cambian con el tiempo, la inicialización optimista puede ser menos efectiva. El sesgo inicial puede persistir y dificultar la adaptación del agente a los cambios dinámicos del entorno. Si bien al inicio el agente puede experimentar recompensas subóptimas debido a la exploración excesiva de acciones aparentemente malas, este es un compromiso (trade-off) necesario para asegurar que no se ignoren acciones potencialmente buenas que, de otra manera, podrían haber sido pasadas por alto.

A diferencia de la inicialización a cero (donde todos los Q(s,a) se inicializan en 0) o la inicialización aleatoria, el sesgo optimista es deliberado y temporal. Se corrige a medida que el agente explora el entorno y actualiza sus estimaciones de Q(s,a). La inicialización aleatoria, por su parte, no garantiza una exploración uniforme, ya que algunas acciones podrían tener valores iniciales más altos por pura casualidad, lo que llevaría al agente a favorecerlas sin una exploración sistemática.

## Referencias 

[1]: C. J. Watkins and P. Dayan, “Q-learning,” Machine learning, vol. 8, no. 3-4, pp. 279–292, 1992.

[2]: Sutton, R. S., Barto, A. G. (2018). Reinforcement Learning: An Introduction. The MIT Press.
 
[3]: Grefenstette, J. J., Moriarty, D. E., & Schultz, A. C. (1999). Evolutionary algorithms for reinforcement learning. Journal of Artificial Intelligence Research, 11, 241–276.

[4]: Bai, H., Cheng, R., & Jin, Y. (2023). Evolutionary reinforcement learning: A survey. Intelligent Computing. 

[5]: Li, P., Hao, J., Tang, H., Fu, X., Zheng, Y., & Tang, K. (2024). Bridging evolutionary algorithms and reinforcement learning: A comprehensive survey on hybrid algorithms. 

[6]: Neustroev, G., & de Weerdt, M. M. (2020). Generalized optimistic Q-learning with provable efficiency.

[7]: Levine, S., Kumar, A., Tucker, G., & Fu, J. (2020). Offline reinforcement learning: Tutorial, review, and perspectives on open problems.

[8]: Prudencio, R. F., Maximo, M. R. O. A., & Colombini, E. L. (2023). A survey on offline reinforcement learning: Taxonomy, review, and open problems.