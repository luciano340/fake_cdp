from threading import Thread
from data_streaming.data_streaming import DataStreaming
from database.database import DataBase
from indexer.indexer import Indexer
from producer import producer
from consumer import consumer
from api.api import app
import uvicorn
import sys


broker = DataStreaming()
db = DataBase()
if len(sys.argv) == 1:
    exit(1)

if sys.argv[1] == "producer":
    t1 = Thread(target=producer, args=(broker,))
    t2 = Thread(target=producer, args=(broker,))
    t1.start()
    t2.start()
elif sys.argv[1] == "consumer":
    indexer = Indexer()
    consumer(broker=broker, db=db, indexer=indexer)
elif sys.argv[1] == "api":
    uvicorn.run(app, host="0.0.0.0", port=8000)
