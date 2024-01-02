import bottle

from controller.base.module import Module, Server


class Imprint(Module):
    def __init__(self, server: Server) -> None:
        super().__init__(server)

        self.represented_by: str = 'ERR: No representative was set'
        self.phone: str = 'ERR: No phone number was set'

    def render(self) -> None:
        self.template = bottle.template('impressum', module=self)
