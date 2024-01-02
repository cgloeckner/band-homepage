import pathlib

from abc import ABC
from typing import Dict


def concat_email(recipient: str, domain: str) -> str:
    return f'{recipient}@{domain}'


class Server(ABC):
    def __init__(self, domain: str, debug: bool, reverse_proxy: bool, local_root: pathlib.Path,
                 model_root: pathlib.Path):
        self.domain = domain
        self.debug = debug
        self.reverse_proxy = reverse_proxy
        self.local_root = local_root
        self.model_root = model_root

    def get_contact_email(self) -> str:
        return concat_email('kontakt', self.domain)

    def get_merch_email(self) -> str:
        return concat_email('merch', self.domain)

    def get_booking_email(self) -> str:
        return concat_email('booking', self.domain)

    def get_webmaster_email(self) -> str:
        return concat_email('webmaster', self.domain)

    def get_all_emails(self) -> Dict[str, str]:
        return {
            'contact': self.get_contact_email(),
            'merch': self.get_merch_email(),
            'booking': self.get_booking_email(),
            'webmaster': self.get_webmaster_email()
        }

    def get_build_path(self) -> pathlib.Path:
        return self.local_root / '.build'

    def get_model_file(self, filename: str) -> pathlib.Path:
        return self.model_root / 'data' / f'{filename}.toml'

    def get_static_url(self, relative_url: str) -> str:
        if self.reverse_proxy:
            return f'https://static.{self.domain}{relative_url}'

        return f'/static{relative_url}'

    def get_static_path(self, use_model: bool = False) -> pathlib.Path:
        """Returns local path to static files (css sheets etc.)"""
        if use_model:
            return self.model_root / 'static'
        else:
            return self.local_root / 'views' / 'static'

    def get_public_url(self, route: str = '') -> str:
        """Returns the public uri with or without a route. HTTPS is assumed in production mode.
        e.g. https://example.com/foo/bar
        """
        base = 'http'
        if not self.debug:
            base += 's'

        base += '://' + self.domain

        if route != '':
            base += '/' + route
        return base
