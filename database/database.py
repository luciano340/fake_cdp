from typing import Optional
from uuid import UUID
import uuid
from DTO.events_dto import EventsDto
from database.database_interface import DataBaseInterface
from sqlalchemy import create_engine, Column, String, DateTime, DECIMAL
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from database.exceptions import EventEmptyORM, EventInsertErroORM

DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/cdp"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
class EventoORM(Base):
    __tablename__ = "events"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    client = Column(String(255))
    event = Column(String(255))
    price = Column(DECIMAL(10, 2))
    long_text = Column(LONGTEXT)
    timestamp = Column(DateTime)
Base.metadata.create_all(bind=engine)

class DataBase(DataBaseInterface):
    _instance: Optional[Session] = None
    
    def __init__(self):
        self.session = DataBase.get_instance()

    @classmethod
    def get_instance(cls) -> Session:
        if cls._instance is None:
            cls._instance = SessionLocal()
        return cls._instance

    def insert(self, event_raw: EventsDto) -> None:
        self.session
        event = EventoORM(
            id=str(event_raw.id),
            client=event_raw.client,
            event=event_raw.event,
            price=event_raw.price,
            timestamp=event_raw.timestamp,
            long_text=event_raw.long_text
        )
        try:
            self.session.add(event)
            self.session.commit()
        except Exception as err:
            raise EventInsertErroORM(err)
    
    def get_all(self) -> list[EventsDto]:
        raw_events = self.session.query(EventsDto).all()

        if raw_events is None:
            raise EventEmptyORM(f"Events cannot be found!")
        
        events = []

        for e in raw_events:
            events.append(
                EventsDto(
                    id=e.id,
                    client=e.client,
                    event=e.event,
                    price=e.price,
                    timestamp=e.timestamp
                )
            )
        
        return events