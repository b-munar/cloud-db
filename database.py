from sqlalchemy import create_engine
from sqlalchemy.engine import URL


url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="database",
    database="postgres",
    password="postgres",
)

engine = create_engine(url)