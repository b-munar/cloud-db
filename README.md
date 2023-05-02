docker compose up database
```
from cloud_db.models import Base
from cloud_db.database import  engine

def main():
    Base.metadata.create_all(engine)
```
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
