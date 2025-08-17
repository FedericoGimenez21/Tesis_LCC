# Scenario1 Full de NetSecGame

## Introducción

El Scenario1 Full de NetSecGame constituye un entorno de simulación de ciberseguridad diseñado para el entrenamiento de agentes de aprendizaje automático en técnicas de penetración y defensa. Este escenario representa una red corporativa compleja que simula un ambiente de seguridad realista, proporcionando un entorno controlado para evaluar las capacidades de los agentes en tareas de exfiltración de datos y movimiento lateral dentro de infraestructuras de red.

El diseño del escenario se basa en principios de seguridad de redes empresariales típicas, incorporando múltiples capas de defensa, diversos tipos de sistemas y configuraciones de red que reflejan entornos reales de producción. Esta aproximación permite evaluar la efectividad de diferentes estrategias de ataque y defensa en un contexto controlado pero representativo.

## Arquitectura de red

### Topología general

La arquitectura de red del Scenario1 Full presentada en la Figura N, se estructura mediante una topología segmentada que comprende dos subredes principales interconectadas a través de un router central con funcionalidades de firewall integradas. Esta configuración refleja las mejores prácticas de segmentación de red utilizadas en entornos empresariales para limitar el alcance de potenciales compromisos de seguridad.

![Topología del escenario full](../NetSecGame/figures\scenario_1.png)
*Figura X: Topología de red del escenario1 full de NetSecGame.*

Las subredes están organizadas de la siguiente manera:

- **Subred de servidores**: 192.168.1.0/24 - Aloja los recursos críticos de la organización
- **Subred de clientes**: 192.168.2.0/24 - Representa las estaciones de trabajo de usuarios finales
- **Conectividad externa**: 213.47.23.192/26 - Simula la conectividad a Internet

### Router central

El router central, accesible mediante las direcciones 192.168.1.1 y 192.168.2.1, funciona como el punto de control y seguridad de la red. Este dispositivo implementa:

- Funcionalidades de firewall con políticas restrictivas configuradas por defecto (política DENY)
- Reglas de acceso específicas que regulan la comunicación entre las diferentes subredes
- Gateway de conectividad externa para operaciones que requieren acceso a Internet
- Filtrado de tráfico basado en políticas de seguridad predefinidas


## Descripción de nodos

### Nodos servidor

La subred de servidores contiene cinco sistemas que alojan diferentes servicios y tipos de datos, cada uno configurado con características específicas que representan diferentes roles dentro de una infraestructura corporativa.

#### Servidor SMB (192.168.1.2)

Este sistema ejecuta Windows Server y proporciona servicios de compartición de archivos mediante el protocolo SMB (Server Message Block). Los servicios configurados incluyen:

- **microsoft-ds**: Servicio SMB/CIFS para compartición de archivos, identificado como vulnerable a exploits remotos
- **ms-wbt-server**: Servicio de Remote Desktop Protocol para acceso remoto
- **windows login**: Sistema de autenticación local

El servidor almacena múltiples conjuntos de datos sensibles: DataFromServer1 (propiedad de User1), Data2FromServer1 (propiedad de User2), y Data3FromServer1 (propiedad de User1). Los usuarios autorizados incluyen User1 a User5 y el usuario Administrator.

La vulnerabilidad del servicio SMB constituye un vector de ataque principal, permitiendo la explotación remota para acceder a los datos almacenados en el sistema.

#### Servidor de base de datos (192.168.1.3)

Sistema basado en Linux que aloja servicios de base de datos críticos:

- **ssh**: OpenSSH versión 8.1.0 para acceso remoto seguro
- **postgresql**: Sistema de gestión de base de datos PostgreSQL versión 14.3.0

El servidor contiene DatabaseData (propiedad de User1) y cuenta con usuarios User1 a User5 además del usuario root. El acceso requiere autenticación SSH válida, proporcionando una capa adicional de seguridad comparado con otros servicios.

#### Servidor web (192.168.1.4)

Sistema Linux configurado para servicios web con las siguientes características:

- **http**: Servidor web lighttpd versión 1.4.54
- **ssh**: OpenSSH versión 8.1.0

Almacena WebServerData (propiedad de User2). Los usuarios autorizados incluyen User1 a User5 y root.

#### Servidores adicionales (192.168.1.5 y 192.168.1.6)

Ambos sistemas ejecutan Linux y proporcionan servicios básicos:

- **ssh**: Acceso remoto únicamente
- **Usuarios**: Solo el usuario root
- **Función**: Servidores de propósito general con acceso altamente restringido

Estos nodos sirven como objetivos secundarios y puntos potenciales para movimiento lateral dentro de la red.

### Nodos cliente

La subred de clientes comprende cinco estaciones de trabajo que representan diferentes puntos de entrada potenciales para un atacante. Estos sistemas simulan las estaciones de trabajo típicas encontradas en entornos corporativos.

#### Cliente 1 (192.168.2.2)

Constituye el punto de ataque principal del escenario:

- **Sistema operativo**: Windows
- **Servicios**: ms-wbt-server y can_attack_start_here (marcador de punto de inicio)
- **Servicio especial**: attacker - representa al agente atacante controlado por IA
- **Usuarios**: User1 y Administrator

Este nodo está preconfigurado como el punto de inicio predeterminado para el agente atacante, proporcionando la base para iniciar operaciones de reconocimiento y ataque.

#### Clientes 2-5 (192.168.2.3-192.168.2.6)

Los clientes restantes proporcionan diversidad en términos de sistemas operativos y configuraciones:

- **Cliente 2** (192.168.2.3): Sistema Windows  y marcador de inicio, usuarios User2 y Administrator
- **Cliente 3** (192.168.2.4): Sistema Linux con SSH y marcador de inicio, usuarios User3 y root
- **Cliente 4** (192.168.2.5): Sistema Linux con SSH y marcador de inicio, usuarios User4 y root
- **Cliente 5** (192.168.2.6): Sistema Linux con acceso solo local, usuarios User5 y root

Esta diversidad permite evaluar la capacidad del agente para adaptarse a diferentes plataformas y configuraciones de seguridad.

### Nodo externo

#### Outside node (213.47.23.195)

Representa un sistema externo en Internet configurado específicamente para operaciones de exfiltración:

- **Ubicación**: Internet simulado
- **Servicios**: listener para recepción de datos exfiltrados
- **Control**: Bajo control del atacante
- **Función**: Destino final para la transferencia de datos comprometidos

## Dinámicas del entorno

### Objetivo y mecánicas de juego

El objetivo principal del agente atacante consiste en completar una secuencia de acciones que comprende: iniciación desde un nodo cliente, exploración de la red para identificar servicios y vulnerabilidades, explotación de sistemas vulnerables, localización de datos sensibles en los servidores, y exfiltración de información al nodo externo.

Esta secuencia requiere que el agente desarrolle estrategias de planificación secuencial, evaluación de riesgos, y optimización de recursos dentro de las limitaciones impuestas por los mecanismos de defensa del entorno.

### Rutas de ataque

#### Ruta principal: explotación SMB

La estrategia de ataque más directa involucra:

1. **Iniciación**: Activación del agente en Cliente 1 con servicio atacante activo
2. **Reconocimiento**: Escaneo sistemático de la subred de servidores para identificar servicios disponibles
3. **Explotación**: Utilización del exploit SMB contra el servicio microsoft-ds en el servidor SMB
4. **Acceso a datos**: Recuperación de archivos críticos almacenados en el sistema comprometido
5. **Exfiltración**: Transferencia de datos al outside node através de la conectividad externa

### Configuración de acceso y autenticación

#### Sistemas de autenticación

Cada nodo mantiene su propio sistema de usuarios y credenciales:

- **Autenticación local**: Cada sistema gestiona independientemente sus usuarios autorizados
- **Niveles de privilegio**:
  - LIMITED: Acceso básico de usuario con permisos restringidos
  - ELEVATED: Privilegios administrativos con acceso completo al sistema


#### Políticas de firewall

El router central implementa políticas de acceso estrictas:

- **Cadena INPUT**: Permite únicamente acceso directo desde subredes específicamente autorizadas
- **Cadena FORWARD**: Reglas granulares para comunicación entre subredes
- **Política predeterminada**: DENY (denegación explícita de todo tráfico no autorizado)

Esta configuración refleja las mejores prácticas de seguridad de red, requiriendo que el agente desarrolle estrategias sofisticadas para navegar las restricciones de acceso.

## Complejidad computacional y escalabilidad

### Dimensiones del espacio de estados

El Scenario1 Full presenta un espacio de estados multidimensional caracterizado por:

- **Diez nodos activos**: Cada uno con múltiples servicios y estados de configuración posibles
- **Servicios heterogéneos**: Diferentes protocolos, versiones y configuraciones de seguridad
- **Estados de compromiso**: Múltiples niveles de acceso y control por nodo
- **Distribución de datos**: Información crítica dispersa en varios servidores con diferentes niveles de protección

### Variabilidad del entorno

El entorno presenta características dinámicas que aumentan su complejidad:

- **Múltiples rutas de solución**: Diversas estrategias válidas para alcanzar los objetivos del escenario
- **Escalabilidad**: Arquitectura base que puede extenderse para crear escenarios de mayor complejidad


## Relevancia para la investigación

El Scenario1 Full de NetSecGame proporciona un entorno de entrenamiento completo y metodológicamente riguroso para la investigación en ciberseguridad y aprendizaje automático. Su diseño incorpora elementos realistas de infraestructuras de red corporativas, manteniendo al mismo tiempo la controlabilidad necesaria para experimentos reproducibles.

La complejidad inherente del escenario, combinada con sus múltiples rutas de solución, lo convierte en una plataforma valiosa para evaluar y comparar diferentes aproximaciones algorítmicas en el dominio de la ciberseguridad ofensiva. Además, su arquitectura escalable proporciona una base sólida para el desarrollo de escenarios más complejos en investigaciones futuras.


## Análisis de resultados experimentales del algoritmo Q-learning en Scenario1 de NetSecGame

A continuacion se presentan resultados obtenidos tras ejecutar 10 iteraciones independientes del algoritmo Q-learning en el Scenario1 Full de NetSecGame, evaluando diferentes configuraciones de episodios de entrenamiento (1,000 a 15,000 episodios). Los datos presentados proporcionan información sobre el rendimiento, consistencia y variabilidad del algoritmo en un entorno de ciberseguridad simulado.

![Distribución de Winrate por episodios de entrenamiento](../../outputs/figures/comparison_analysis/scenario1/winrate_02_boxplot_by_episodes.png)
*Figura X+1: Distribución de winrate por episodios de entrenamiento. Los boxplots muestran la mediana (línea roja), cuartiles y valores atípicos para cada configuración.*

![Winrate promedio por episodios de entrenamiento](../../outputs/figures/comparison_analysis/scenario1/winrate_01_bars_by_episodes.png)
*Figura X+2: Winrate promedio por episodios de entrenamiento. Las barras de error representan el error estándar de la media (n=10 por configuración).*

![Tabla 1: Resumen estadístico de winrate por episodios de entrenamiento](../../outputs/figures/comparison_analysis/scenario1/winrate_03_summary_table.png)
*Tabla 1: Resumen estadístico obtenido tras 10 ejecuciones independientes.*

### Análisis del rendimiento general

#### Tendencias de los promedios

Los resultados observados en la Figura X+1, muestran un rendimiento general modesto del algoritmo Q-learning, con winrates promedio que oscilan entre 4.12% y 9.72% a lo largo de las diferentes configuraciones de episodios de entrenamiento. El análisis de las medias revela un patrón no monótono en el rendimiento, donde el incremento en el número de episodios de entrenamiento no se traduce consistentemente en mejoras del winrate.

La configuración de 14,000 episodios presenta el mejor rendimiento promedio (9.72%), seguida por las configuraciones de 6,000 episodios (6.72%) y 13,000 episodios (6.52%). Este comportamiento sugiere que el algoritmo puede beneficiarse de un entrenamiento prolongado en ciertos rangos específicos, pero no muestra una curva de aprendizaje estrictamente creciente.

Las medianas, en general, mantienen valores cercanos a las medias (diferencias típicas menores al 1%), lo que indica distribuciones relativamente simétricas en la mayoría de las configuraciones. Esta característica sugiere ausencia de sesgos significativos hacia valores extremos en el rendimiento.

#### Análisis de consistencia y variabilidad

La desviación estándar de los resultados presenta variaciones considerables entre configuraciones, oscilando desde 0.76% (9,000 episodios) hasta 11.71% (14,000 episodios). Esta variabilidad heterogénea indica que la consistencia del algoritmo está fuertemente influenciada por el número de episodios de entrenamiento.

Las configuraciones con menor variabilidad (9,000, 13,000 y 7,000 episodios con desviaciones estándar de 0.76%, 0.94% y 1.30% respectivamente) demuestran mayor estabilidad en el rendimiento, mientras que la configuración de 14,000 episodios, a pesar de mostrar el mejor rendimiento promedio, exhibe la mayor variabilidad (11.71% de desviación estándar).


### Interpretación del análisis distribucional

#### Comparación entre gráfico de barras y boxplot

El boxplot correspondiente a 14,000 episodios presentado en la Figura X+2, muestra un valor atípico significativo (aproximadamente 42.4%), lo que explica la elevada desviación estándar observada en esta configuración. Este outlier sugiere que, bajo ciertas condiciones específicas, el algoritmo puede alcanzar rendimientos sustancialmente superiores, pero esta mejora no es reproducible consistentemente.

La presencia de valores atípicos en varias configuraciones (particularmente visibles en 3,000, 4,000 y 14,000 episodios) indica que el algoritmo ocasionalmente encuentra estrategias exitosas, pero estas no se consolidan como comportamiento estándar.


### Factores contribuyentes a la variabilidad

La variabilidad observada puede atribuirse principalmente a tres factores fundamentales:

1. **Inicialización en cero de Q-tables**: Comenzar con todos los valores Q igual a cero establece un punto de partida uniforme para todos los estados y acciones. Si bien esto elimina la variabilidad inicial causada por valores aleatorios, también puede generar trayectorias de aprendizaje más lentas en las etapas tempranas del entrenamiento debido a la ausencia de sesgos exploratorios iniciales.

2. **Balance exploración-explotación**: La política ε-greedy utilizada introduce estocasticidad inherente que puede resultar en diferentes rutas de descubrimiento de estrategias exitosas entre ejecuciones.

3. **Complejidad del entorno**: El Scenario1 Full presenta múltiples rutas de ataque posibles y estados intermedios, creando un espacio de búsqueda complejo donde pequeñas diferencias en las decisiones tempranas pueden amplificarse significativamente.


## Conclusion

En conclusion, los resultados presentados constituyen una línea base importante para futuras mejoras algorítmicas y proporcionan evidencia empírica de la complejidad inherente del dominio de ciberseguridad simulada en NetSecGame.

En la implementación actual de Q-learning, las políticas derivadas de las Q-tables se inicializan con un valor uniforme de cero para todos los pares estado-acción. Si bien este enfoque garantiza imparcialidad inicial, puede inducir a un aprendizaje más lento, ya que el agente no recibe señales iniciales que lo orienten hacia acciones potencialmente más prometedoras.

Se propone investigar y evaluar técnicas avanzadas de inicialización de Q-tables y políticas que aceleren la convergencia y mejoren la exploración,tales como:

- Inicialización optimista: usar valores iniciales más altos para fomentar la exploración temprana.
- Preentrenamiento: entrenar una Q-table inicial mediante episodios de prueba.
- Técnicas evolutivas: optimizar la Q-table inicial mediante algoritmos genéticos o estrategias evolutivas, especialmente para entornos con alto espacio de estados.
