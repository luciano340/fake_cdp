import json
from typing import Iterator
from kafka import KafkaConsumer, KafkaProducer
from DTO.events_dto import EventsDto
from data_streaming.data_streaming_interface import T, DataStreamingInterface 

class DataStreaming(DataStreamingInterface):
    def __init__(self, group_id: str = "Estudos",  bootstrap_servers: str = 'localhost:9092' , topic: str = 'eventos_clientes'):
        self.topic = topic
        self.__producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self.__consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="earliest",
        )

    def send(self, msg: EventsDto) -> None:
        self.__producer.send(self.topic, msg.json())

    def recv(self) -> Iterator[T]:
        for msg in self.__consumer:
            yield EventsDto(**msg.value)
    
    def close(self):
        self.__producer.close()
        self.__consumer.close()