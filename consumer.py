from data_streaming.data_streaming_interface import DataStreamingInterface


def consumer(broker: DataStreamingInterface) -> None:
        for msg in broker.recv():
            print("Mensangem recebida do broker!", msg.json())