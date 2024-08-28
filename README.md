# OpenTelemetry Observability Stack

Este repositorio contiene una configuración completa para desplegar una pila de observabilidad utilizando OpenTelemetry, Jaeger, Grafana, Prometheus, y Nginx. El objetivo de este proyecto es demostrar cómo implementar un sistema de monitoreo y trazabilidad distribuida para aplicaciones basadas en microservicios.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Visualización de Trazas](#visualización-de-trazas)
- [Casos de Uso](#casos-de-uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Introducción

En un entorno de microservicios, es fundamental contar con una infraestructura robusta de monitoreo y trazabilidad para identificar problemas, analizar el rendimiento y comprender el comportamiento de las aplicaciones. Este proyecto proporciona una solución integrada utilizando OpenTelemetry para recopilar métricas y trazas, Jaeger para visualizar trazas distribuidas y Grafana para monitorizar métricas y trazas en paneles personalizables.

## Tecnologías Utilizadas

- **OpenTelemetry**: Framework de código abierto para la recopilación de trazas y métricas.
- **Jaeger**: Sistema de trazabilidad distribuida que permite rastrear las solicitudes a través de microservicios.
- **Grafana**: Plataforma de análisis y monitoreo para visualizar métricas y trazas.
- **Prometheus**: Sistema de monitoreo y alerta que recopila métricas de los servicios.
- **Nginx**: Servidor proxy inverso para redirigir el tráfico a la aplicación de Flask.
- **Flask**: Microframework de Python utilizado para crear la aplicación de ejemplo.
- **Docker**: Plataforma de contenedores utilizada para ejecutar los servicios de manera aislada y consistente.

## Estructura del Proyecto

/OpenTelemetry-Observability-Stack 

├── app/ │

├── app.py # Aplicación de ejemplo en Flask │

└── Dockerfile # Dockerfile para la aplicación Flask 

├── nginx/ │ 

└── nginx.conf # Configuración de Nginx

├── collector/ │

└── config.yaml # Configuración del colector OpenTelemetry 

├── grafana/ │ 

└── provisioning/ # Configuración inicial de Grafana 

├── prometheus/ │ 

└── prometheus.yml # Configuración de Prometheus 

├── docker-compose.yml # Archivo de configuración de Docker Compose 

└── README.md # Este archivo


## Requisitos Previos

Antes de comenzar, asegúrate de tener los siguientes programas instalados:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Instalación y Configuración

1. **Clonar el repositorio**:

    ```bash
    git clone https://github.com/Munchkinland/OpenTelemetry-Observability-Stack.git
    cd OpenTelemetry-Observability-Stack
    ```

2. **Configurar variables de entorno**: Si tu configuración requiere alguna variable de entorno (por ejemplo, para conectar a bases de datos), agrégala en un archivo `.env` en la raíz del proyecto.

3. **Iniciar los servicios con Docker Compose**:

    ```bash
    docker-compose up -d
    ```

    Este comando iniciará todos los servicios definidos en el archivo `docker-compose.yml`.

4. **Verificar los servicios**: Asegúrate de que los servicios están en ejecución accediendo a las siguientes URLs en tu navegador:

    - **Aplicación Flask**: [http://localhost:8080](http://localhost:8080)
    - **Jaeger**: [http://localhost:16686](http://localhost:16686)
    - **Grafana**: [http://localhost:3000](http://localhost:3000) (credenciales por defecto: `admin` / `admin`)
    - **Prometheus**: [http://localhost:9090](http://localhost:9090)

## Visualización de Trazas

Una vez que las trazas son enviadas al colector de OpenTelemetry, se pueden visualizar en Jaeger y Grafana.

### Accediendo a Jaeger:

1. Navegar a [http://localhost:16686](http://localhost:16686) para acceder a la interfaz de usuario de Jaeger.
2. Utilizar la interfaz para buscar y explorar trazas específicas basadas en criterios como el nombre del servicio o la operación.

### Accediendo a Grafana:

1. Navegar a [http://localhost:3000](http://localhost:3000) y acceder con las credenciales por defecto (`admin`/`admin`).
2. Configurar las fuentes de datos para integrar Prometheus y Jaeger.
3. Crear paneles de visualización para observar tanto métricas como trazas, permitiendo una comprensión profunda de la aplicación.

## Casos de Uso

- **Monitorización de microservicios**: Esta configuración es ideal para empresas que utilizan microservicios y necesitan una solución de trazabilidad distribuida.
- **Optimización del rendimiento**: Permite identificar cuellos de botella en el rendimiento y tiempos de respuesta de los servicios.
- **Detección de fallos**: Mejora la capacidad de detectar y diagnosticar problemas en tiempo real.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar este proyecto, siéntete libre de abrir un *issue* o enviar un *pull request*.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
