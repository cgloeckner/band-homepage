from abc import abstractmethod, ABC

from .server import Server


class Module(ABC):
    def __init__(self, server: Server) -> None:
        self.server = server
        self.template = None
        self.data = {}

        self.band_name: str = 'ERR: No band name was set'
        self.genre: str = 'ERR: No genre was set'
        self.domain: str = 'ERR: No domain was set'
        self.description: str = 'ERR: No description was set'
        self.keywords: list[str] = ['Err: No keywords were set']

    @property
    def title(self) -> str:
        return f'{self.band_name.upper()} - {self.genre}'

    @abstractmethod
    def render(self) -> None: ...
