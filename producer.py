import random
from threading import Thread
import time
import randomname
from DTO.events_dto import EventsDto
from data_streaming.data_streaming import DataStreaming
from data_streaming.data_streaming_interface import DataStreamingInterface


def producer(broker: DataStreamingInterface) -> None:
    names = [randomname.get_name() for _ in range(200)]
    events = ["Compra", "Venda", "Login", "Cadastro", "Pesquisa", "Carrinho de compra"]

    while threat_controller:
        event = EventsDto(
            client=random.choice(names),
            event=random.choice(events),
            price=round(random.uniform(10, 1000), 2),
            timestamp=time.time()
        )

        broker.send(event)
        print('Evento enviado!')
        time.sleep(random.random())

if __name__ == "__main__":
    threat_controller = True
    broker = DataStreaming()
    t1 = Thread(target=producer, args=(broker,))
    t2 = Thread(target=producer, args=(broker,))
    t1.start()
    t2.start()

    #simulando consumer.
    try:
        for msg in broker.recv():
            print("Mensangem recebida do broker!", msg)
    except KeyboardInterrupt:
        print("Encerrando....")
        threat_controller = False
    
    t1.join()
    t2.join()
    print("Encerrando!")
    