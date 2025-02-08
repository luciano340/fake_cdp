from abc import ABC, abstractmethod
from typing import Iterator, TypeVar
from DTO.events_dto import EventsDto

T = TypeVar("T")

class DataStreamingInterface(ABC):
    @abstractmethod
    def send(self, msg: EventsDto) -> None:
        pass

    @abstractmethod
    def recv(self) -> Iterator[T]:
        pass

    @abstractmethod
    def close(self) -> None:
        pass