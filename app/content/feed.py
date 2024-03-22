import tomli
import bottle
import logging
import datetime

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

        # filter out expired posts
        today = datetime.datetime.today().date()
        #self.data = {key:  value for key, value in self.data.items() if value.get('expire', today) >= today}

    def render(self) -> None:
        self.template = bottle.template('feed/index', module=self)
