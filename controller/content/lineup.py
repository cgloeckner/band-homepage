import tomli
import bottle
import logging

from controller.base.module import Module, Server


class Lineup(Module):
    def __init__(self, server: Server, cfg: dict) -> None:
        super().__init__(server, cfg)

        self.biography = cfg['biography']
        self.base_title = 'Lineup & Biografie'

    def load_from_file(self) -> None:
        filename = self.server.get_model_file('lineup')
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return

        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('lineup/index', module=self)
