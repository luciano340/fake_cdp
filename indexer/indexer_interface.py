from abc import ABC, abstractmethod

from DTO.events_dto import EventsDto

class IndexerInterface(ABC):
    @abstractmethod
    def send(self, msg: EventsDto) -> None:
        pass
    
    def search_all(self) -> list[EventsDto]:
        pass