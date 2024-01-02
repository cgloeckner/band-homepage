import bottle

from controller import base


class Contact(base.Module):
    def __init__(self, server: base.Server, cfg: dict) -> None:
        super().__init__(server, cfg)

        self.contact = cfg['contact']

    def render(self) -> None:
        self.template = bottle.template('contact', module=self)
