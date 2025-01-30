import random
import time
import randomname
from DTO.events_dto import EventsDto
from data_streaming.data_streaming_interface import DataStreamingInterface


def producer(broker: DataStreamingInterface) -> None:
    names = [randomname.get_name() for _ in range(200)]
    events = ["Compra", "Venda", "Login", "Cadastro", "Pesquisa", "Carrinho de compra"]

    while True:
        event = EventsDto(
            client=random.choice(names),
            event=random.choice(events),
            price=round(random.uniform(10, 1000), 2),
            timestamp=time.time()
        )

        broker.send(event)
        print('Evento enviado!')
        time.sleep(random.random())    