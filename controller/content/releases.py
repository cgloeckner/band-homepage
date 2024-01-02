import bottle

from controller.base.module import Module, Server
from .merch import Merch


class Releases(Module):
    def __init__(self, server: Server) -> None:
        super().__init__(server)
        self.data = dict()
        self.base_title = 'Releases'

    def load_from_merch(self, merch: Merch) -> None:
        self.data = merch.get_cds()

    def render(self) -> None:
        self.template = bottle.template('releases/index', module=self)
