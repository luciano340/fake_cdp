import sys
sys.path.append('../')

from fastapi import FastAPI
from database.database import DataBase
from indexer.indexer import Indexer

app = FastAPI()

@app.get("/eventos_db/")
def get_eventos():
    db = DataBase()
    eventos = db.get_all()
    db.kill_instance()
    return eventos

@app.get("/eventos_es/")
def get_eventos():
    indexer = Indexer()
    response = indexer.search_all()
    return response