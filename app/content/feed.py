import tomli
import yaml
import bottle
import logging
import datetime

from app.base.module import Module, Server


class Feed(Module):
    def __init__(self, server: Server, cfg: dict) -> None:
        super().__init__(server, cfg)

    def load_quotes(self) -> dict[str, str]:
        filename = self.server.path.get_config_file('reviews', 'yaml')
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return {}

        with open(filename, 'rb') as file:
            data = yaml.safe_load(file)

        if data is None:
            return {}

        return data

    def load_thumbnail_content(self) -> dict[str, dict[str, str]]:
        filename = self.server.path.get_config_file('feed')
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return {}

        with open(filename, 'rb') as file:
            data = tomli.load(file)

        # filter out expired posts
        today = datetime.datetime.today().date()
        return {key:  value for key, value in data.items() if value.get('expire', today) >= today}

    def load_from_file(self) -> None:
        self.data = {
            'quotes': self.load_quotes(),
            'links': self.load_thumbnail_content()
        }

    def render(self) -> None:
        self.template = bottle.template('feed/index', module=self)
