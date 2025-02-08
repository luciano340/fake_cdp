from threading import Thread
from data_streaming.data_streaming import DataStreaming
from database.database import DataBase
from indexer.indexer import Indexer
from metrics import Metrics
from producer import producer
from consumer import consumer
import uvicorn
import sys

metrics = Metrics()
broker = DataStreaming()
db = DataBase()

if len(sys.argv) == 1:
    exit(1)

print(sys.argv[1])

if sys.argv[1] == "producer":
    metrics.start_server(1000)
    t1 = Thread(target=producer, args=(broker, metrics))
    t2 = Thread(target=producer, args=(broker, metrics))
    t1.start()
    t2.start()
elif sys.argv[1] == "consumer":
    metrics.start_server(1001)
    indexer = Indexer()
    consumer(broker=broker, db=db, indexer=indexer, metrics=metrics)
elif sys.argv[1] == "api":
    from api.api import app
    app.metrics = metrics
    metrics.start_server(1002)
    uvicorn.run(app, host="0.0.0.0", port=8000)
