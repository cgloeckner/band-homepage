import bottle

from .modules import BaseModule, BaseWebServer


class Contact(BaseModule):
    def __init__(self, api: BaseWebServer) -> None:
        super().__init__(api)

        self.contacts = [{
            'title': 'ERR: No contact type was set',
            'name': 'ERR: No contact name was set',
            'email': 'ERR: No context email was set'
        }]

    def render(self) -> None:
        self.template = bottle.template('contact', module=self, all_emails=self.server.get_all_emails(),
                                        get_static_url=self.server.get_static_url)
