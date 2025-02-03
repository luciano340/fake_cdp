from threading import Thread
from data_streaming.data_streaming import DataStreaming
from database.database import DataBase
from indexer.indexer import Indexer
from producer import producer
from consumer import consumer

indexer = Indexer()
broker = DataStreaming()
db = DataBase()
t1 = Thread(target=producer, args=(broker,))
t2 = Thread(target=producer, args=(broker,))
t1.start()
t2.start()


consumer(broker=broker, db=db, indexer=indexer)