# Juego de Trivia - Práctica Calificada 5

## Descripción
Aplicación de trivia interactiva desarrollada en Python con FastAPI y PostgreSQL. El juego permite a los usuarios responder preguntas de diferentes niveles de dificultad y mantiene un registro de las mejores puntuaciones.

## Características
- **Juego de trivia** con 10 preguntas por ronda
- **Tres niveles de dificultad**: Fácil (1 pto), Media (5 pts), Difícil (10 pts)
- **Sistema de puntuación** y tabla de clasificación
- **API REST** con FastAPI
- **Base de datos PostgreSQL** para persistencia
- **Interfaz de línea de comandos** interactiva
- **Contenedores Docker** para facilitar el despliegue

## Estructura del Proyecto
```
├── src/                    # Código fuente de la API
│   ├── api/               # Endpoints y esquemas de la API
│   └── db/                # Modelos y operaciones de base de datos
├── game_objects/          # Clases del juego (Question, Quiz)
├── pos_db/               # Scripts de inicialización de PostgreSQL
├── test/                 # Pruebas unitarias y de integración
├── main.py               # Aplicación cliente del juego
└── docker-compose.yml    # Configuración de contenedores

```

## Instalación y Ejecución

### Usando Docker (Recomendado)
```bash
# Levantar los servicios
docker-compose up --build

# Ejecutar el juego
python main.py
```

### Instalación Manual
```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos PostgreSQL
# Ejecutar scripts en pos_db/

# Ejecutar la API
uvicorn src.api.app:app --host 0.0.0.0 --port 8000

# Ejecutar el juego
python main.py
```

## Uso
1. Ejecutar `python main.py` para iniciar el juego
2. Elegir entre:
   - Comenzar un nuevo juego
   - Ver tabla de clasificación
   - Salir
3. Responder las 10 preguntas del quiz
4. Registrar tu nombre para guardar la puntuación

## Pruebas
```bash
# Ejecutar tests con Docker
docker-compose run tests

# O ejecutar directamente
pytest test/
```

## Tecnologías Utilizadas
- **Python 3.x**
- **FastAPI** - Framework web
- **PostgreSQL** - Base de datos
- **Docker & Docker Compose** - Contenedores
- **Requests** - Cliente HTTP
- **Pytest** - Framework de pruebas

## API Endpoints
- `GET /` - Mensaje de bienvenida
- `GET /questions` - Obtener preguntas del quiz
- `POST /game_session` - Registrar puntuación
- `GET /top_scores` - Obtener mejores puntuaciones
