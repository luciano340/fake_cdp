from threading import Thread
from data_streaming.data_streaming import DataStreaming
from producer import producer
from consumer import consumer

broker = DataStreaming()
t1 = Thread(target=producer, args=(broker,))
t2 = Thread(target=producer, args=(broker,))
t1.start()
t2.start()

consumer(broker)