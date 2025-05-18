import bottle

from app.base.module import Module, Server


class Cookie(Module):
    def __init__(self, server: Server, cfg: dict) -> None:
        super().__init__(server, cfg)

    def render(self) -> None:
        self.info_template = bottle.template('cookie/info', module=self)
        self.banner_template = bottle.template('cookie/banner', module=self)
