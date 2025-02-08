import sys
import time

from metrics import Metrics
sys.path.append('../')

from fastapi import FastAPI, Request, Depends
from database.database import DataBase
from indexer.indexer import Indexer

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    app.metrics.api_respose_time.labels(endpoint=request.url.path, method=request.method).observe(process_time)
    return response

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