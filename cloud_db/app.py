from .models import Base
from .database import  engine

def main():
    Base.metadata.create_all(engine)