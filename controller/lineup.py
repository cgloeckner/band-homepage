import tomli
import bottle
import logging

from .modules import BaseModule, BaseWebServer


class Lineup(BaseModule):
    def __init__(self, api: BaseWebServer) -> None:
        super().__init__(api)

        self.base_title = 'Lineup & Biografie'

    def load_from_file(self) -> None:
        filename = self.server.local_root / 'model' / 'data' / 'lineup.toml'
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return

        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('lineup/index', module=self, data=self.data,
                                        get_static_url=self.server.get_static_url)
