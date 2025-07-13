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

## Referencias 

[1]: C. J. Watkins and P. Dayan, “Q-learning,” Machine learning, vol. 8, no. 3-4, pp. 279–292, 1992.

[2]: Sutton, R. S., Barto, A. G. (2018). Reinforcement Learning: An Introduction. The MIT Press.
 