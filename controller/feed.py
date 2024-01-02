import tomli
import bottle
import logging

from .modules import BaseModule, BaseWebServer


class Feed(BaseModule):
    def __init__(self, api: BaseWebServer) -> None:
        super().__init__(api)

    def load_from_file(self) -> None:
        filename = self.server.local_root / 'model' / 'data' / 'feed.toml'
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return

        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('feed/index', module=self, data=self.data,
                                        get_static_url=self.server.get_static_url)
