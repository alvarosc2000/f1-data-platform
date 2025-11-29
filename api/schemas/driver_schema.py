# api/schemas/driver_schema.py
from pydantic import BaseModel

class DriverBase(BaseModel):
    driver_number: int
    broadcast_name: str
    first_name: str
    full_name: str
    last_name: str
    headshot_url: str
    country_code: str
    meeting_key: str
    name_acronym: str
    session_key: str
    team_colour: str
    team_name: str

class DriverCreate(DriverBase):
    pass

class DriverOut(DriverBase):
    class Config:
        orm_mode = True
