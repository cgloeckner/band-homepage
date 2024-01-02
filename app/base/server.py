import pathlib
import bottle

from .email import EmailApi
from .path import PathApi
from .ip import IpApi


class Server:
    def __init__(self, app_root: pathlib.Path, content_root: pathlib.Path, domain: str, debug: bool, host: str,
                 port: int, server):
        self.email = EmailApi(domain)
        self.path = PathApi(app_root, content_root, domain, debug)
        self.ip = IpApi(debug)

        self.domain = domain
        self.debug = debug
        self.host = host
        self.port = port
        self.server = server

        self.app = bottle.default_app()
        self.app.catchall = self.debug

    def get_presskit_url(self) -> str:
        return self.path.get_static_url('/presskit.zip')

    def run(self) -> None:
        bottle.run(host=self.host, port=self.port, debug=self.debug, reloader=self.debug, quiet=not self.debug,
                   server=self.server)
