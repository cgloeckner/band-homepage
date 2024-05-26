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
        self.profiles: dict[str, dict[str, str]] = cfg['profiles']
        self.navigation: list[str] = cfg['navigation']
        self.merch: dict[str, str] | None = cfg['merch']

        self.social_icons: dict[str, str] = {
            'facebook': 'https://static.xx.fbcdn.net/rsrc.php/yT/r/aGT3gskzWBf.ico',
            'instagram': 'https://static.cdninstagram.com/rsrc.php/y4/r/QaBlI0OZiks.ico',
            'youtube': 'https://www.youtube.com/s/desktop/691ad9c2/img/favicon_32x32.png',
            'spotify': 'https://open.spotifycdn.com/cdn/images/favicon.0f31d2ea.ico',
            'bandcamp': 'https://s4.bcbits.com/img/favicon/favicon-32x32.png',
            'soundcloud': 'https://a-v2.sndcdn.com/assets/images/sc-icons/favicon-2cadd14bdb.ico'
        }

    @property
    def title(self) -> str:
        return f'{self.band_name.upper()} - {self.genre}'

    @abstractmethod
    def render(self) -> None: ...
