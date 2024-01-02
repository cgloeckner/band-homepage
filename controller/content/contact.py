import bottle

from controller import base


class Contact(base.Module):
    def __init__(self, server: base.Server) -> None:
        super().__init__(server)

        self.contacts = [{
            'title': 'ERR: No contact type was set',
            'name': 'ERR: No contact name was set',
            'email': 'ERR: No context email was set'
        }]

    def render(self) -> None:
        self.template = bottle.template('contact', module=self)
