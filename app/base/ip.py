from dataclasses import dataclass

import bottle
import requests


@dataclass
class IpApi:
    debug: bool

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
