from gevent import monkey; monkey.patch_all()

import requests
import pathlib
import bottle

from typing import Dict

from controller.base.module import Server


class WebServer(Server):

    def __init__(self, local_root: pathlib.Path, model_root: pathlib.Path, args: Dict) -> None:
        super().__init__(args['domain'], args['debug'], args['reverse_proxy'], local_root=local_root,
                         model_root=model_root)
        self.args = args

        self.app = bottle.default_app()
        self.app.catchall = self.debug

    def get_client_ip(self, request: bottle.Request) -> str:
        """Returns client's ip address based on the given request."""
        if self.debug:
            return request.environ.get('REMOTE_ADDR')

        # default: app runs behind reverse proxy
        return request.environ.get('HTTP_X_FORWARDED_FOR')

    @staticmethod
    def get_client_agent(request: bottle.Request) -> str:
        """Returns the client's browser agent based on the given request."""
        return request.environ.get('HTTP_USER_AGENT')

    @staticmethod
    def get_public_ip():
        try:
            return requests.get('https://api.ipify.org').text
        except requests.exceptions.ReadTimeout as e:
            return 'localhost'

    def run(self) -> None:
        bottle.run(
            host=self.args['host'],
            port=self.args['port'],
            debug=self.args['debug'],
            reloader=self.args['reloader'],
            quiet=self.args['quiet'],
            server=self.args['server']
        )
