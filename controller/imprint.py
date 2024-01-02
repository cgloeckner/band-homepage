import bottle

from .modules import BaseModule, BaseWebServer


class Imprint(BaseModule):
    def __init__(self, api: BaseWebServer) -> None:
        super().__init__(api)

        self.represented_by: str = 'ERR: No representative was set'
        self.phone: str = 'ERR: No phone number was set'

    def render(self) -> None:
        self.template = bottle.template('impressum', module=self,
                                        contact_email=self.server.get_contact_email(),
                                        get_static_url=self.server.get_static_url)
