from interfaces import ClientInterface, AdapterInterface  # pyright: ignore


class JsonClient(ClientInterface):

    _adapter: AdapterInterface

    def __init__(self, adapter: AdapterInterface) -> None:
        self._adapter = adapter

    def exec_operation(self) -> None:
        self._adapter.exec_operation()
