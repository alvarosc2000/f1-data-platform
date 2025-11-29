# db/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base  # Importamos Base desde el nuevo archivo
from sqlalchemy.orm import Session

# URL de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Cambia esto si es necesario

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear las tablas en la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)

# Llamada a la inicialización de las tablas
init_db()
