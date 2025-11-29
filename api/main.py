from fastapi import FastAPI
from api.routers.drivers import router as driver_router
from db.db import init_db  # Importa la función init_db para crear las tablas

# Crear la aplicación FastAPI
app = FastAPI(
    title="Proyecto de ingeniería de datos de F1"
)

# Llamar a init_db() para crear las tablas al arrancar la aplicación
init_db()

# Incluir el router de los drivers
app.include_router(driver_router, prefix="/drivers", tags=["drivers"])
