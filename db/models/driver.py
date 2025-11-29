from sqlalchemy import Column, Integer, String
from db.db import Base

class Driver(Base):
    __tablename__ = 'drivers'
    
    id = Column(Integer, primary_key=True, index=True)
    driver_number = Column(Integer) 
    broadcast_name = Column(String)
    first_name = Column(String)
    full_name = Column(String)
    last_name = Column(String)
    headshot_url = Column(String)
    country_code = Column(String)
    meeting_key = Column(Integer)
    name_acronym = Column(String)
    session_key = Column(Integer)
    team_colour = Column(String)
    team_name = Column(String)
