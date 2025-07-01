# Análisis técnico de la representación del estado en NetSecGame

Este documento presenta un análisis detallado de la representación del estado en el entorno de simulación **NetSecGame**, orientado a la evaluación de agentes en tareas de ciberseguridad ofensiva. 

---

## Tabla de contenidos

1. [Introducción](#introducción)
2. [Estructura del estado](#estructura-del-estado)
3. [Dinámica de actualización](#dinámica-de-actualización)
4. [Relevancia estratégica de las variables](#relevancia-estratégica-de-las-variables)
5. [Complejidad del espacio de estados](#complejidad-del-espacio-de-estados)
6. [Observaciones finales](#observaciones-finales)

---

## Introducción

NetSecGame constituye un entorno de simulación avanzado para la evaluación de agentes autónomos en escenarios de ciberseguridad ofensiva. La representación del estado, entendida como la percepción parcial del agente atacante, es fundamental para la toma de decisiones y la planificación estratégica. Este análisis examina en profundidad la estructura, dinámica y complejidad de dicha representación, proporcionando una base sólida para investigaciones futuras en el área.

---

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

## Relevancia estratégica de las variables

La importancia estratégica de cada variable se resume a continuación, destacando su impacto en la capacidad del agente para alcanzar los objetivos del escenario:

| Variable             | Relevancia | Justificación                                                                 |
|----------------------|------------|--------------------------------------------------------------------------------|
| `known_networks`     | Alta       | Define el alcance inicial de exploración.                                     |
| `known_hosts`        | Alta       | Permite seleccionar objetivos para escaneo de servicios.                      |
| `controlled_hosts`   | Crítica    | Solo desde estos hosts se pueden buscar datos o exfiltrarlos.                 |
| `known_services`     | Alta       | Esencial para identificar vectores de explotación.                            |
| `known_data`         | Crítica    | Determina si el objetivo del escenario puede ser alcanzado.                   |

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

---

## Observaciones finales

En síntesis, la representación del estado en NetSecGame reproduce condiciones realistas de ciberataques, favoreciendo la evaluación rigurosa de agentes inteligentes bajo restricciones de observabilidad y dinámica estocástica. La estructura modular del estado permite evaluar la capacidad de generalización, razonamiento y planificación de agentes basados en LLMs o RL. La presencia de un defensor estocástico introduce una capa adicional de complejidad estratégica, penalizando acciones repetitivas o agresivas.

