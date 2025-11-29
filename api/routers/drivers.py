# routers/drivers.py
import requests
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from db.db import get_db
from db.models.driver import Driver
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

# routers/drivers.py
@router.post("/load_drivers/")
def load_drivers(db: Session = Depends(get_db)):
    url = "https://api.openf1.org/v1/drivers"
    response = requests.get(url)

    if response.status_code == 200:
        drivers_data = response.json()
        new_drivers_count = 0
        
        for driver in drivers_data:
            try:
                # Verificar si el conductor ya existe en la base de datos
                existing_driver = db.query(Driver).filter(Driver.driver_number == driver["driver_number"]).first()

                if existing_driver is None:  # Si no existe, lo agregamos
                    db_driver = Driver(
                        driver_number=driver["driver_number"],
                        broadcast_name=driver["broadcast_name"],
                        first_name=driver["first_name"],
                        full_name=driver["full_name"],
                        last_name=driver["last_name"],
                        headshot_url=driver["headshot_url"],
                        country_code=driver["country_code"],
                        meeting_key=driver["meeting_key"],
                        name_acronym=driver["name_acronym"],
                        session_key=driver["session_key"],
                        team_colour=driver["team_colour"],
                        team_name=driver["team_name"],
                    )
                    db.add(db_driver)
                    new_drivers_count += 1

            except SQLAlchemyError as e:
                db.rollback()  # Si ocurre un error de base de datos, deshacer la transacción
                return {"error": f"An error occurred while saving the driver: {str(e)}"}

        db.commit()  # Guardar todos los cambios de una vez
        return {"message": f"{new_drivers_count} drivers loaded successfully!"}
    else:
        return {"error": "Failed to fetch drivers from the external API"}