import tomli
import bottle
import logging

from typing import Dict, List

from controller.base.module import Module, Server


class Gigs(Module):
    def __init__(self, server: Server) -> None:
        super().__init__(server)

        self.data = dict()

        self.base_title = 'Live Shows'
        self.location = 'ERR: No location was set'

    @staticmethod
    def process_gigs(gigs: Dict[str, Dict]) -> Dict[int, List]:
        """Groups the given dictionary of gigs by year and returns a dictionary."""
        # group by years
        years_found = [gigs[key]['date'].year for key in gigs]
        data = dict()
        for year in years_found:
            gigs_that_year = [gigs[key] for key in gigs if gigs[key]['date'].year == year]
            data[year] = gigs_that_year

        # sort gigs with date (starting with most recent)
        for year in data:
            data[year].sort(key=lambda gig: gig['date'], reverse=True)

        return data

    def load_from_file(self) -> None:
        filename = self.server.local_root / 'model' / 'data' / 'gigs.toml'
        if not filename.exists():
            logging.warning(f'File not found: {filename}')
            return

        with open(filename, 'rb') as file:
            gigs = tomli.load(file)

        self.data = self.process_gigs(gigs)

    def render(self) -> None:
        self.template = bottle.template('gigs/index', module=self)
