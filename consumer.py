import time
import randomname
from random import randint
from data_streaming.data_streaming_interface import DataStreamingInterface
from database import database_interface
from database.exceptions import EventInsertErroORM

def consumer(broker: DataStreamingInterface, db: database_interface) -> None:
        for msg in broker.recv():
            print("Mensangem recebida do broker!", msg)
            msg.long_text = " ".join(randomname.get_name() for _ in range(randint(2000, 5000)))
            try:
                db.insert(msg)
            except EventInsertErroORM as err:
                 print(err)
                 continue
            print('Evento salvo no banco de dados com sucesso!')
