from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv

load_dotenv()

def url_postgresql(username, host, database, password, port):
    url = URL.create(
        drivername="postgresql",
        username=username,
        host=host,
        database=database,
        password=password,
        port=port
    )
    return url

engine = create_engine(url_postgresql(
        username=os.getenv("USERNAME"),
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        password=os.getenv("PASSWORD"),
        port=os.getenv("PORT")
        )
    )