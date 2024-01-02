import tomli
import bottle
import logging

from app.base.module import Module, Server


class Feed(Module):
    def __init__(self, server: Server, cfg: dict) -> None:
        super().__init__(server, cfg)

    def load_from_file(self) -> None:
        filename = self.server.path.get_content_file('feed')
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return

        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('feed/index', module=self)
