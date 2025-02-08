import sys
import time

from metrics import Metrics
sys.path.append('../')

from fastapi import FastAPI, Request, Depends
from database.database import DataBase
from indexer.indexer import Indexer

app = FastAPI()

@app.get("/eventos_db/")
def get_eventos():
    start_time = time.time()
    db = DataBase()
    eventos = db.get_all()
    db.kill_instance()
    process_time = time.time() - start_time
    app.metrics.api_respose_time.labels(endpoint="/eventos_db/", method="GET").observe(process_time)
    return eventos

@app.get("/eventos_es/")
def get_eventos():
    start_time = time.time()
    indexer = Indexer()
    response = indexer.search_all()
    process_time = time.time() - start_time
    app.metrics.api_respose_time.labels(endpoint="/eventos_es/", method="GET").observe(process_time)
    return response