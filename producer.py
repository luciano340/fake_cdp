import random
import time
import randomname
import re
from DTO.events_dto import EventsDto
from data_streaming.data_streaming_interface import DataStreamingInterface
from metrics import Metrics

def producer(broker: DataStreamingInterface, metrics: Metrics) -> None:
    names = [randomname.get_name() for _ in range(200)]
    events = ["Compra", "Venda", "Login", "Cadastro", "Pesquisa", "Carrinho de compra"]

    while True:
        event = EventsDto(
            client=random.choice(names),
            event=random.choice(events),
            price=round(random.uniform(10, 1000), 2)
        )
        try:
            broker.send(event)
            metrics.events_queue.inc()
        except Exception as err:
            err_msg = re.sub(r'\W+', '', str(err))
            metrics.errors.labels("producer", err_msg).inc()

        print('Evento enviado!')
        time.sleep(random.random())
