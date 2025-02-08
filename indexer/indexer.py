from elasticsearch import Elasticsearch
from DTO.events_dto import EventsDto
from indexer.indexer_interface import IndexerInterface


class Indexer(IndexerInterface):
    def __init__(self, index: str = "cdp_eventos"):
        self.conn = Elasticsearch("http://elasticsearch:9200")
        print(self.conn.info())
        self.index = index

    def send(self, msg: EventsDto) -> None:
        self.conn.index(index=self.index, document=msg.to_json_string())

    def search_all(self) -> list[EventsDto]:
        query = {"query": {"match_all": {}}}  # Retorna todos os documentos
        response = self.conn.search(index=self.index, body=query)

        eventos = [hit["_source"] for hit in response["hits"]["hits"]]
        return eventos