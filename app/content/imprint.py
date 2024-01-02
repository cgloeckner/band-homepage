import bottle

from app.base.module import Module, Server


class Imprint(Module):
    def __init__(self, server: Server, cfg: dict) -> None:
        super().__init__(server, cfg)

        self.represented_by = cfg['imprint']['represented_by']
        self.phone = cfg['imprint']['phone']

    def render(self) -> None:
        self.template = bottle.template('imprint/index', module=self)
