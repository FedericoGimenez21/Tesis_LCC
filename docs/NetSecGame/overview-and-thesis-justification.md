# NetSecGame: Caracterización del entorno y fundamentos de su selección para esta tesis

## Tabla de contenidos

1. [¿Qué es NetSecGame?](#qué-es-netsecgame)
2. [¿Cómo funciona?](#cómo-funciona)
3. [¿Por qué fue creado?](#por-qué-fue-creado)
4. [Justificación de su elección para esta tesis](#justificación-de-su-elección-para-esta-tesis)
5. [Conclusiones](#conclusiones)
---

## ¿Qué es NetSecGame?

NetSecGame es un entorno de simulación avanzado diseñado específicamente para la evaluación de agentes autónomos en tareas de ciberseguridad ofensiva. Fue creado por [Stratosphere Research Laboratory](https://www.stratosphereips.org/), el grupo de ciberseguridad del Centro de Inteligencia Artificial de la Facultad de Ingeniería Eléctrica de la Universidad Técnica Checa en Praga. Este grupo trabaja en la intersección de ciberseguridad, aprendizaje automático y asistencia a otros.

Se trata de un simulador que modela escenarios realistas de redes computacionales donde los agentes pueden ejecutar acciones típicas de un atacante: reconocimiento, explotación de vulnerabilidades, movimiento lateral y exfiltración de datos.

### Objetivo del simulador

El objetivo principal de NetSecGame es proporcionar un entorno controlado y reproducible para:
- Entrenar y evaluar agentes de aprendizaje por refuerzo en tareas de ciberseguridad
- Simular ataques en redes computacionales
- Facilitar la investigación en inteligencia artificial aplicada a la seguridad informática

### Características principales

**Agente atacante**: El simulador se centra en agentes atacantes que deben navegar por redes, descubrir vulnerabilidades y comprometer sistemas para alcanzar objetivos específicos.

**Entorno de red realista**: Modela topologías de red complejas con hosts, servicios, datos y reglas de conectividad que reflejan entornos empresariales reales.

**Simulación de ataques**: Reproduce el ciclo completo de un ataque cibernético: reconocimiento, acceso inicial, escalada de privilegios, movimiento lateral y exfiltración.

**Estados parcialmente observables**: Los agentes tienen conocimiento limitado del entorno y deben descubrir progresivamente la topología y recursos disponibles.

**Sistema de recompensas**: Implementa un sistema de recompensas que incentiva el logro de objetivos específicos mientras penaliza acciones ineficientes.

---

## ¿Cómo funciona?

### Arquitectura general

NetSecGame sigue el paradigma clásico de interacción agente-entorno en aprendizaje por refuerzo:

1. **Inicialización**: El entorno se configura con una topología de red específica, incluyendo hosts, servicios, datos y reglas de conectividad.

2. **Observación**: El agente recibe una observación del estado actual, que incluye su conocimiento parcial de la red (hosts conocidos, servicios descubiertos, hosts controlados, etc.).

3. **Acción**: El agente selecciona una acción basada en su política actual (escaneo de red, búsqueda de servicios, explotación, etc.).

4. **Transición**: El entorno procesa la acción, actualiza su estado interno y determina si la acción fue exitosa según probabilidades predefinidas.

5. **Recompensa**: Se calcula una recompensa basada en el progreso del agente hacia sus objetivos y el costo de la acción ejecutada.

6. **Iteración**: El proceso se repite hasta que se alcanza una condición de terminación (éxito, tiempo límite, detección).

### Representación de escenarios

Los escenarios se definen mediante archivos de configuración YAML que especifican:
- **Topología de red**: Subredes, hosts y reglas de conectividad
- **Servicios**: Aplicaciones ejecutándose en cada host con sus respectivas vulnerabilidades
- **Datos**: Información sensible distribuida en los hosts
- **Objetivos**: Metas específicas que el agente debe alcanzar
- **Parámetros del defensor**: Comportamiento del sistema de defensa estocástico


---

## ¿Por qué fue creado?

### Contexto académico

NetSecGame fue desarrollado en el contexto de investigación académica en ciberseguridad e inteligencia artificial, específicamente para abordar la falta de entornos de simulación realistas y controlados para el entrenamiento de agentes autónomos en tareas de ciberseguridad.

### Problemas que busca resolver

**Escasez de entornos de entrenamiento**: Los simuladores existentes carecen del realismo necesario.

**Evaluación reproducible**: Proporciona un marco controlado donde los experimentos pueden ser repetidos con condiciones idénticas, facilitando la comparación de diferentes enfoques.

**Escalabilidad**: Permite evaluar agentes en escenarios de complejidad variable, desde redes simples hasta topologías empresariales complejas.

**Seguridad**: Ofrece un entorno seguro para experimentar con técnicas de ataque sin riesgo de dañar sistemas reales.

### Ventajas distintivas de NetSecGame

NetSecGame presenta varias ventajas significativas frente a otros entornos de simulación similares:

**Modularidad y extensibilidad**: Es muy modular y fácil de extender a nuevas topologías, lo que permite adaptar el entorno a diferentes necesidades de investigación.

**Realismo de la información**: El agente no recibe información auxiliar no realista en el estado. Toda la información disponible corresponde a lo que un atacante real podría obtener.

**Objetivo realista**: El objetivo es muy realista: exfiltrar datos hacia Internet, reflejando motivaciones reales de atacantes.

**Presencia de defensor**: Existe un defensor presente en el entorno, añadiendo una capa de complejidad y realismo a la simulación.

**Recompensas genéricas**: Las recompensas no están diseñadas específicamente para el problema particular, sino que son genéricas, lo que mejora la generalización de los enfoques desarrollados.

### Referencias relevantes

Si bien NetSecGame cuenta actualmente con un número limitado de citas en publicaciones académicas, se trata de un entorno de alta calidad, desarrollado por expertos en ciberseguridad del Cybersecurity Group del Artificial Intelligence Centre, perteneciente a la Faculty of Electrical Engineering de la Czech Technical University in Prague. Su diseño modular, capacidad para simular escenarios ofensivos y defensivos, y su orientación a la investigación en aprendizaje por refuerzo lo convierten en una plataforma valiosa y técnicamente robusta para la experimentación en tareas de seguridad de redes.

---

### Usos principales

**Investigación**: Desarrollo y evaluación de algoritmos de aprendizaje automático para ciberseguridad.

**Docencia**: Enseñanza de conceptos de seguridad informática y técnicas de ataque en un entorno controlado.

**Validación de algoritmos**: Comparación objetiva de diferentes enfoques de agentes autónomos.

---

## Justificación de su elección para esta tesis

### Relevancia temática

NetSecGame se alinea perfectamente con los objetivos de esta investigación al proporcionar:

- **Modelado realista**: Representa escenarios de ciberseguridad que reflejan desafíos del mundo real
- **Complejidad controlada**: Permite evaluar agentes en entornos de complejidad variable
- **Observabilidad parcial**: Modela la incertidumbre inherente en escenarios de ciberseguridad reales

### Adecuación técnica para Q-learning y ciberseguridad multiagente

El entorno NetSecGame presenta características técnicas específicamente alineadas con los objetivos de mejora de la inicialización de políticas en algoritmos de Q-learning para entornos de ciberseguridad multiagente:

- **Representación explícita de estados, acciones y recompensas**: Proporciona estructuras de datos claras y extensibles (GameState, Action, Observation) que facilitan la implementación de Q-learning y la experimentación con diferentes estrategias de inicialización de políticas. Las tablas Q pueden construirse directamente sobre estas representaciones estructuradas.

- **Complejidad escalable**: Permite evaluar métodos de inicialización desde escenarios simples (pocas redes y hosts) hasta complejos (múltiples subredes interconectadas), facilitando el análisis del impacto de diferentes estrategias de inicialización según la complejidad del problema.

- **Observabilidad parcial realista**: El descubrimiento progresivo del entorno simula condiciones reales donde el agente debe aprender con información limitada, siendo crucial para evaluar cómo diferentes inicializaciones de política afectan la exploración y el aprendizaje.

- **Arquitectura multiagente extensible**: Aunque actualmente enfocado en agentes atacantes, su diseño modular permite la extensión a escenarios multiagente donde múltiples atacantes o atacantes-defensores interactúan, siendo relevante para la investigación propuesta.


### Espacio controlado y reproducible

**Determinismo configurable**: Permite controlar la aleatoriedad para garantizar reproducibilidad de experimentos.

**Escalabilidad**: Facilita la evaluación desde escenarios simples hasta complejos, permitiendo análisis comparativos sistemáticos.

**Métricas integradas**: Incluye sistemas de logging y métricas que facilitan el análisis de rendimiento.

### Soporte y extensibilidad

**Código abierto**: Base de código disponible y documentada que permite modificaciones y extensiones.

**Configurabilidad**: Arquitectura modular que permite adaptar escenarios según necesidades específicas.

**Comunidad activa**: Soporte continuo y desarrollo activo por parte de la comunidad académica.

### Limitaciones conocidas

**Complejidad exponencial**: El espacio de estados crece exponencialmente con el tamaño del entorno, lo que puede limitar la escalabilidad.

**Simplicidad del defensor**: El defensor no es un agente autónomo, sino un sistema estocástico simple.

**Limitaciones de realismo**: Aunque realista, sigue siendo una simplificación de entornos de ciberseguridad reales.

**Dependencias técnicas**: Requiere configuración específica y conocimiento técnico para su uso efectivo.

---

## Conclusiones

NetSecGame se presenta como la opción más adecuada para la investigación sobre "Mejora de la inicialización de políticas en algoritmos de Q-learning para entornos de ciberseguridad multiagente" por las siguientes razones fundamentales:

**Alineación temática perfecta**: Combina los dominios de ciberseguridad y aprendizaje por refuerzo de manera natural, proporcionando un contexto realista donde las mejoras en inicialización de políticas tienen impacto directo en la efectividad de agentes atacantes.

**Idoneidad técnica para Q-learning**: Su espacio de estados bien estructurado facilita la implementación de algoritmos tabulares como Q-learning, mientras que sus métricas específicas de ciberseguridad permiten evaluar objetivamente el impacto de diferentes estrategias de inicialización.

**Escalabilidad experimental**: Permite un análisis sistemático desde escenarios simples hasta complejos, facilitando la evaluación gradual de cómo las mejoras en inicialización se comportan según aumenta la complejidad del problema.

**Relevancia práctica**: Los resultados obtenidos en este entorno tienen aplicación directa en problemas reales de ciberseguridad, donde la eficiencia en el aprendizaje de agentes autónomos es crucial para sistemas de detección y respuesta automatizada.

La adopción de NetSecGame permite enfocar completamente los esfuerzos de investigación en el problema específico de inicialización de políticas, aprovechando un entorno maduro, bien documentado y técnicamente robusto que facilitará la obtención de resultados significativos y reproducibles en el área de investigación propuesta.
