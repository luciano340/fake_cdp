from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from DTO.events_dto import EventsDto


class DataBaseInterface(ABC):
    @abstractmethod
    def get_instance(self) -> Session:
        pass

    @abstractmethod
    def insert(self, event: EventsDto) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[EventsDto]:
        pass