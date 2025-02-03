import sys
sys.path.append('../')

from fastapi import FastAPI
from database.database import DataBase


app = FastAPI()

@app.get("/eventos_db/")
def get_eventos():
    db = DataBase()
    eventos = db.get_all()
    return eventos