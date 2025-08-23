# Escenario Tiny de NetSecGame

## Documentación del entorno mínimo para aprendizaje por refuerzo

## 1. Introducción

### 1.1 Descripción general

El **escenario Tiny** representa la configuración más simple y fundamental del entorno NetSecGame, diseñado específicamente como un entorno mínimo reproducible para investigación en aprendizaje por refuerzo aplicado a ciberseguridad. 

### 1.2 Contextualización en NetSecGame

NetSecGame es un simulador de ciberseguridad que modela ataques y defensas en redes corporativas complejas. El escenario Tiny actúa como:

- **Entorno de referencia**: Base para comparación de algoritmos de aprendizaje por refuerzo
- **Banco de pruebas**: Validación inicial de nuevos enfoques antes de escalar a escenarios más complejos
- **Herramienta de debugging**: Facilitación del análisis del comportamiento del agente en un espacio controlado

### 1.3 Objetivo como entorno mínimo

El diseño del escenario Tiny busca:

- **Preservar la esencia** de los desafíos de ciberseguridad reales
- **Minimizar la complejidad** del espacio de estados y acciones
- **Garantizar reproducibilidad** en experimentos de investigación
- **Facilitar interpretación** de resultados y comportamientos del agente

---

## 2. Composición del escenario Tiny

### 2.1 Arquitectura de red

El escenario Tiny implementa una topología de red simplificada pero representativa, como se muestra en la siguiente figura:

![Topología del escenario Tiny](../NetSecGame/figures\scenario_1_tiny.png)
*Figura 1: Topología de red del escenario Tiny de NetSecGame.*

#### 2.1.1 Descripción de la topología

La arquitectura del escenario Tiny está compuesta por:

- **Red cliente (Client Subnetwork)**: Subred 192.168.2.0/24 donde se encuentra el punto de inicio
- **Red servidor (Server Subnetwork)**: Subred 192.168.1.0/24 que contiene el objetivo principal
- **Router central**: Elemento de infraestructura que conecta las subredes internas
- **Internet**: Simulación de conectividad externa
- **Servidor C&C**: Nodo externo controlado por el atacante para exfiltración

### 2.2 Inventario de hosts

| Host           | Tipo              | IP                          | Rol                  | Descripción                                      |
|----------------|-------------------|------------------------------|-----------------------|--------------------------------------------------|
| **client_1**    | Nodo cliente      | 192.168.2.2                  | **Punto inicial**     | Host desde donde inicia el agente atacante       |
| **smb_server**  | Servidor Windows  | 192.168.1.2                  | **Objetivo principal**| Servidor con servicios SMB vulnerables           |
| **router1**     | Router            | 192.168.1.1<br>192.168.2.1   | Infraestructura       | Control de tráfico entre redes                   |
| **outside_node**| Servidor externo  | 213.47.23.195                | **Exfiltración**      | Nodo controlado por atacante para C&C            |

### 2.3 Servicios por host

#### 2.3.1 Client 1 (punto inicial)

**Servicios activos:**
- **attacker**: Servicio principal del agente atacante que permite la ejecución de acciones ofensivas

**Servicios pasivos:**
- **ms-wbt-server**: Servicio de Remote Desktop Protocol (RDP) para acceso remoto
- **powershell**: Intérprete de línea de comandos Windows para ejecución de scripts
- **can_attack_start_here**: Marcador especial que identifica este nodo como punto de partida válido

**Características:**
- **Sistema operativo**: Windows 10 versión 10.0.19041 (Windows 10 20H1)
- **Nivel de acceso inicial**: Privilegios limitados de usuario estándar
- **Cuentas de usuario**: User1 (estándar) y Administrator (privilegiada)

#### 2.3.2 SMB Server (objetivo principal)

**Servicios pasivos:**
- **microsoft-ds**: Servicio SMB/CIFS para compartición de archivos (VULNERABLE a exploits remotos)
- **ms-wbt-server**: Servicio Remote Desktop para acceso administrativo remoto
- **windows login**: Sistema de autenticación local Windows
- **powershell**: Shell de comandos para administración del servidor

**Características:**
- **Sistema operativo**: Windows Server versión 10.0.19041
- **Vulnerabilidad principal**: Servicio SMB susceptible a exploits de ejecución remota de código
- **Datos sensibles**: Contiene 3 archivos confidenciales de diferentes usuarios del sistema
- **Cuentas de usuario**: User1-5 (usuarios estándar) y Administrator (cuenta privilegiada)

#### 2.3.3 Outside Node (exfiltración)

**Servicios pasivos:**
- **bash**: Shell de línea de comandos de sistema Linux/Unix
- **listener**: Servicio especializado para recepción de datos exfiltrados

**Características:**
- **Sistema operativo**: Distribución Linux (no especificada)
- **Propósito operacional**: Actúa como servidor de comando y control (C&C) externo
- **Control de acceso**: Completamente controlado por el atacante desde el inicio

## 3. Beneficios de trabajar con un entorno reducido

### 3.1 Eficiencia computacional

El escenario Tiny ofrece una complejidad manejable comparado con entornos más realistas. Principalmente, solo 3 nodos están activos versus más de 10 en escenarios corporativos complejos. 

## 4. Justificación de uso en la tesis

### 4.1 Rol estratégico como caso base

El escenario Tiny establece una base metodológica robusta para la investigación:

- **Validación de algoritmos**: Permite pruebas de concepto en un entorno completamente controlado antes de escalar
- **Debugging profundo**: Facilita la identificación y corrección de problemas fundamentales en los algoritmos
- **Optimización de hiperparámetros**: Proporciona feedback rápido para ajuste fino de parámetros algorítmicos
- **Desarrollo iterativo**: Acelera los ciclos de mejora mediante experimentación eficiente

## 5. Conclusiones

### 5.1 Síntesis de beneficios

El uso estratégico del escenario Tiny permite:

1. **Establecer línea base confiable** para evaluación algorítmica
2. **Desarrollar comprensión profunda** de mecanismos de aprendizaje
3. **Validar hipótesis específicas** con control experimental total
4. **Acelerar ciclos de desarrollo** e iteración metodológica


