from cloud_db.models import Base
from cloud_db.database import  engine

def main():
    Base.metadata.create_all(engine)
    
if __name__ == "__main__":
    main()