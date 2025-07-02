from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.db.core.config import settings

# Creación de objeto que establece conexión con la base de datos mediante el objeto de configuración
engine = create_engine(settings.DATABASE_URL)

# Creación de objeto de generación de sesiones de interacción con la base de datos
SessionLocal = sessionmaker(autoflush=False, bind=engine)

# Declaración de objeto Base para inicialización de objetos de la base de datos
Base = declarative_base()

# Función de inicialización y partida de operaciones SQL
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
