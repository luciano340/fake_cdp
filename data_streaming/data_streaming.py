from queue import Queue
from typing import Iterator
from DTO.events_dto import EventsDto
from data_streaming.data_streaming_interface import T, DataStreamingInterface


class DataStreaming(DataStreamingInterface):
    def __init__(self):
        self.__broker = Queue()

    def send(self, msg: EventsDto) -> None:
        self.__broker.put(msg)

    def recv(self) -> Iterator[T]:
        while True:
            msg = self.__broker.get()
            yield msg