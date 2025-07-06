# Análisis del sistema de recompensas en NetSecGame

## 1. Resumen ejecutivo

Este informe examina el diseño y la implementación del sistema de recompensas en el entorno NetSecGame, con énfasis en su impacto sobre el aprendizaje del agente Q-learning. Se analizan tanto las recompensas proporcionadas por el entorno como las redefinidas internamente por el agente, evaluando su alineación con los objetivos del entorno, su capacidad para guiar el aprendizaje y su influencia en la convergencia del modelo.

### Recompensas del entorno 
El entorno NetSecGame define una función de recompensa simple, que asigna retroalimentación solo en eventos críticos:

Las recompensas de cada acción son escasas. 
| Evento                         | Condición                                      | Recompensa del entorno |
|-------------------------------|------------------------------------------------|------------------------|
| Paso normal                | No conduce al objetivo ni a detección          | -1                     |
| Éxito (exfiltración exitosa) | El agente alcanza el estado objetivo           | +100                   |
| Detección                    | El agente es detectado por el defensor         | -50                    |

### Recompensas internas del agente Q-learning

Para mejorar la eficiencia del aprendizaje, el agente de Q-learning redefine la función de recompensa mediante el método `recompute_reward`, con el objetivo de:

- Aumentar el contraste entre éxito y fracaso.
- Penalizar más severamente los errores.
- Acelerar la convergencia del valor Q.
 
#### Eventos que disparan Recompensas

| Evento | Condición de activación |Recompensa Q-Agent |
|--------|------------------------|-------------------|
| **Paso normal** | Acción que no termina episodio | -1 |
| **Éxito (exfiltración exitosa)** | `AgentStatus.Success` | +1000 |
| **Detección** | `AgentStatus.Fail` | -1000 | 
| **Timeout (límite de pasos)** | `AgentStatus.TimeoutReached` |-100 | 


---

### Hallazgos Clave

#### Fortalezas Principales:
- **Alineación con los objetivos del entorno**: El rediseño refuerza el comportamiento deseado (exfiltración sin ser detectado).
- **Simplicidad y claridad**: La función es fácil de interpretar y mantener.


#### Limitaciones Críticas:

- **Ausencia de recompensas intermedias**:  La función de recompensa no proporciona retroalimentación parcial ante logros intermedios (ej.: controlar un host o descubrir un dato). 

- **Exploración poco guiada**: En etapas tempranas, el agente puede carecer de señales útiles para aprender rutas efectivas hacia el objetivo.


---
