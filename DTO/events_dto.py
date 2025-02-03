from dataclasses import dataclass, asdict, field
import json
from uuid import UUID, uuid4
from datetime import datetime



@dataclass
class EventsDto:
    client: str
    event: str
    price: int
    timestamp: datetime = field(default_factory=lambda: datetime.now().isoformat(sep=" ", timespec="seconds"))
    id: UUID = field(default_factory=uuid4)
    long_text: str = ""

    def to_json_string(self) -> dict:
        return json.dumps(asdict(self), default=str)