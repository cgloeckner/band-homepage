import tomli
import bottle
import logging

from typing import Dict, List

from controller.base.module import Module, Server


class Shows(Module):
    def __init__(self, server: Server, cfg: dict) -> None:
        super().__init__(server, cfg)

        self.data = dict()

        self.base_title = 'Live Shows'
        self.location = cfg['location']

    @staticmethod
    def process_shows(shows: Dict[str, Dict]) -> Dict[int, List]:
        """Groups the given dictionary of shows by year and returns a dictionary."""
        # group by years
        years_found = [shows[key]['date'].year for key in shows]
        data = dict()
        for year in years_found:
            shows_that_year = [shows[key] for key in shows if shows[key]['date'].year == year]
            data[year] = shows_that_year

        # sort shows with date (starting with most recent)
        for year in data:
            data[year].sort(key=lambda show: show['date'], reverse=True)

        return data

    def load_from_file(self) -> None:
        filename = self.server.get_model_file('shows')
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return

        with open(filename, 'rb') as file:
            shows = tomli.load(file)

        self.data = self.process_shows(shows)

    def render(self) -> None:
        self.template = bottle.template('shows/index', module=self)
