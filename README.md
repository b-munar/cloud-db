docker compose up database

from .models import Base
from .database import  engine

def main():
    Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()