from datetime import datetime
import re
import time
import randomname
from random import randint
from data_streaming.data_streaming_interface import DataStreamingInterface
from database import database_interface
from database.exceptions import EventInsertErroORM
from indexer.indexer_interface import IndexerInterface
from metrics import Metrics

def consumer(broker: DataStreamingInterface, db: database_interface, indexer: IndexerInterface, metrics: Metrics) -> None:
        for msg in broker.recv():
            print("Mensangem recebida do broker!", msg)
            msg.long_text = " ".join(randomname.get_name() for _ in range(randint(2000, 5000)))
            try:
                db.insert(msg)
                indexer.send(msg)
                timestamp_end = datetime.now().isoformat(sep=" ", timespec="seconds")
                dt_end = datetime.strptime(timestamp_end, "%Y-%m-%d %H:%M:%S")
                dt_start = datetime.strptime(str(msg.timestamp), "%Y-%m-%d %H:%M:%S")
                elapsed_seconds = (dt_end - dt_start).total_seconds()
                metrics.events_queue.dec(1)
                metrics.event_process_time.observe(elapsed_seconds)
            except EventInsertErroORM as err:
                err_msg = re.sub(r'\W+', '', str(err))
                metrics.errors.labels("producer", err_msg).inc()
                continue

            print('Evento salvo no banco de dados com sucesso!')
            time.sleep(1)
