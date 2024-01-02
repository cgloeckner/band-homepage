from abc import abstractmethod, ABC

from .server import Server


class Module(ABC):
    def __init__(self, server: Server, cfg: dict) -> None:
        self.server = server
        self.template = None
        self.data = {}

        self.band_name: str = cfg['band_name']
        self.genre: str = cfg['genre']
        self.domain: str = cfg['domain']
        self.description: str = cfg['description']
        self.keywords: list[str] = cfg['keywords']
        self.navigation: list[str] = cfg['navigation']

    @property
    def title(self) -> str:
        return f'{self.band_name.upper()} - {self.genre}'

    @abstractmethod
    def render(self) -> None: ...
