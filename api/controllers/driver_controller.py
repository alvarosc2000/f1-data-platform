from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session  # Añadido para la sesión de la DB
from db.db import get_db  # Corregido: importamos get_db desde db/db.py
from db.models.driver import Driver
from api.schemas.driver_schema import DriverCreate, DriverOut
from etl.extract import extract_driver_data

# Obtener todos los drivers
async def get_drivers(db: Session = Depends(get_db)):  # Dependencia de la sesión de DB
    drivers = db.query(Driver).all()
    return drivers

# Obtener un driver por ID
async def get_driver_by_id(driver_number: int, db: Session = Depends(get_db)):  # Dependencia de la sesión de DB
    driver = db.query(Driver).filter(Driver.driver_number == driver_number).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

# Crear un nuevo driver
async def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):  # Dependencia de la sesión de DB
    try:
        # Extraemos los datos de la API externa de manera asíncrona
        driver_data = await extract_driver_data(driver.driver_number)  

        new_driver = Driver(
            driver_number=driver.driver_number,
            broadcast_name=driver_data["broadcast_name"],
            first_name=driver_data["first_name"],
            full_name=driver_data["full_name"],
            last_name=driver_data["last_name"],
            headshot_url=driver_data["headshot_url"],
            country_code=driver_data["country_code"],
            meeting_key=driver_data["meeting_key"],
            name_acronym=driver_data["name_acronym"],
            session_key=driver_data["session_key"],
            team_colour=driver_data["team_colour"],
            team_name=driver_data["team_name"]
        )

        db.add(new_driver)
        db.commit()

        return new_driver
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")
