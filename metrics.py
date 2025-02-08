from prometheus_client import Gauge, Histogram, start_http_server, multiprocess, CollectorRegistry, Counter

class Metrics:   
    def __init__(self):
        self.registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(self.registry)
        self.events_queue = Gauge("kafka_events_queue", "Eventos na fila do Kafka")
        self.errors = Counter("application_error_count", "Erros na aplicação", ['method', 'error_msg'])
        self.event_process_time = Histogram("events_process_time", "Tempo total para o evento passar por todo o fluxo da aplicação")
        self.api_respose_time = Histogram("http_request_duration_seconds", "Tempo de resposta dos endpoints", ['endpoint', 'method'])

    def start_server(self, port: int):
        try:
            print(f'Iniciando prometheus server na porta {port}')
            start_http_server(port, registry=self.registry)
        except Exception as err:
            print(f'Erro ao iniciar prometheus server na porta {port}: {err}')
            exit(1)