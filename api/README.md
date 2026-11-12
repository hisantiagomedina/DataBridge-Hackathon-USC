# Hello World!, I'm CLAIMOS API :)
API REST para la gestión de incidencias y solicitudes de soporte de un sistema de software interno de una aseguradora.

## Versión
0.1.0

## Descripción
Este proyecto busca centralizar la gestión de tickets, permitiendo registrar, consultar, actualizar y realizar seguimiento a las incidencias reportadas por los usuarios del sistema.

## Objetivos
- Gestionar el ciclo de vida de los tickets.
- Facilitar el seguimiento de incidencias.
- Organizar las solicitudes según su estado y prioridad.
- Mantener un registro de las operaciones realizadas sobre cada ticket.

## Tecnologías
- **Lenguaje:** Python
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL & DataBricks
- **ORM:** Por definir
- **Control de versiones:** Git version 2.53.0.windows.2

## Estructura del proyecto

```text
api/
│   .gitignore
│   index.py
│   requirements.txt
│   
├───auth
├───database
├───docs
│       README.md
│       
├───services
├───tests
└───workers
```

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd ticket-management-api
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

Windows:
```bash
venv\Scripts\activate
```

Linux / macOS:
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
uvicorn index:app --reload
```

## Documentación de la API

FastAPI proporciona documentación interactiva mediante Swagger UI:

```text
http://localhost:8000/docs
```

## Desarrollador
Hecho por Santiago M. @ Noviembre 12-13 / 2026
