from dataclasses import dataclass, asdict
import time


@dataclass
class EventsDto:
    client: str
    event: str
    price: int
    timestamp: time

    def json(self) -> dict:
        return asdict(self)
