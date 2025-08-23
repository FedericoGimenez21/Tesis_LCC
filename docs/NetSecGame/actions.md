
## Conjunto de acciones

Actualmente, NetSecGame solo soporta agentes atacantes y acciones de ataque (el defensor no es un agente autónomo). Las acciones definen las transiciones entre estados en el entorno. Si bien existen cinco tipos básicos de acciones principales asociadas al ciclo de ataque, el agente puede ejecutar más acciones según la definición de la enumeración `ActionType` en el código fuente. Cada una de estas acciones recibe un conjunto diferente de parámetros:

- **ScanNetwork**: recibe una red objetivo (`target_network`).
- **FindServices**: recibe un host objetivo (`target_host`).
- **ExploitService**: recibe un host objetivo y un servicio objetivo (`target_host`, `target_service`).
- **FindData**: recibe un host objetivo (`target_host`).
- **ExfiltrateData**: recibe un host fuente, un host destino y un dato objetivo (`source_host`, `target_host`, `target_data`).

Esto hace que el espacio de acciones sea considerablemente complejo, ya que el número exacto de acciones únicas depende de la configuración específica del entorno (cantidad de redes, hosts, servicios y datos). Cabe destacar que las acciones no se envían a los agentes en ninguna forma; en cada estado del entorno, solo ciertas acciones son válidas, pero corresponde a los agentes determinar cuáles están disponibles a partir de la observación del estado actual.

Cada acción básica tiene una probabilidad de éxito predefinida, lo que representa una simplificación de la realidad (pérdida de paquetes, problemas de red, incompatibilidades, etc.). Si una acción tomada por el agente es válida en ese estado, su éxito se evalúa según la distribución de probabilidad definida en el archivo de configuración. Si la acción no tiene éxito, el estado del entorno no cambia (equivalente a un self-loop en el espacio de estados). Es importante señalar que el agente no recibe ninguna indicación explícita de que la acción fue fallida, y que la penalización por paso se aplica independientemente del éxito o fracaso de la acción.

### Enumeración de acciones posibles

Según la definición de la enumeración `ActionType` en el código fuente, el agente puede ejecutar las siguientes acciones:

- **ScanNetwork**
- **FindServices**
- **FindData**
- **ExploitService**
- **ExfiltrateData**
- **BlockIP**
- **JoinGame**
- **QuitGame**
- **ResetGame**

### Clasificación por tipo y requerimientos

#### Acciones de reconocimiento (exploración)
- **ScanNetwork**  
  - Efecto: Descubre hosts en una red conocida.
  - Requisito: Conocer la red objetivo y tener control sobre un host fuente.
- **FindServices**  
  - Efecto: Descubre servicios en un host conocido.
  - Requisito: Control sobre un host fuente y conocer el host objetivo.

#### Acciones ofensivas (explotación y control)
- **ExploitService**  
  - Efecto: Intenta explotar un servicio en un host para obtener control sobre él.
  - Requisito: Conocer el servicio objetivo y control sobre un host fuente.

#### Acciones de obtención y exfiltración de datos
- **FindData**  
  - Efecto: Descubre datos almacenados en un host controlado.
  - Requisito: Control sobre el host objetivo.
- **ExfiltrateData**  
  - Efecto: Transfiere datos desde un host controlado a otro (típicamente al C&C).
  - Requisito: Control sobre el host fuente y destino, y haber descubierto los datos.

#### Acciones de defensa o manipulación de red
- **BlockIP**  
  - Efecto: Bloquea la comunicación entre dos hosts.
  - Requisito: Permisos de defensa o control sobre la política de red.

#### Acciones de gestión de la simulación
- **JoinGame**  
  - Efecto: El agente se une a la simulación.
  - Requisito: Ninguno (acción inicial).
- **QuitGame**  
  - Efecto: El agente abandona la simulación.
  - Requisito: Ninguno.
- **ResetGame**  
  - Efecto: Reinicia el entorno de simulación.
  - Requisito: Permisos de administración o condiciones específicas.

### Representación de las acciones

Cada acción se representa como un objeto de la clase `Action`, que incluye:
- `action_type`: Un valor de la enumeración `ActionType` (por ejemplo, `ActionType.ScanNetwork`).
- `parameters`: Un diccionario con los parámetros requeridos (por ejemplo, `source_host`, `target_host`, `target_network`, `target_service`, `data`).

Ejemplo:
```python
Action(action_type=ActionType.FindServices, parameters={'source_host': IP('10.0.0.2'), 'target_host': IP('10.0.0.3')})
```

### Impacto de las acciones en el entorno

- **ScanNetwork**: Aumenta el conjunto de hosts conocidos (`known_hosts`).
- **FindServices**: Aumenta el conjunto de servicios conocidos en un host (`known_services`).
- **ExploitService**: Si tiene éxito, añade el host a los controlados (`controlled_hosts`).
- **FindData**: Aumenta el conjunto de datos conocidos en un host (`known_data`).
- **ExfiltrateData**: No modifica el estado interno, pero puede registrar la transferencia de datos.
- **BlockIP**: Modifica las reglas de comunicación, afectando la conectividad.
- **JoinGame/QuitGame/ResetGame**: Afectan el ciclo de vida del agente o la simulación, pero no el estado de la red.