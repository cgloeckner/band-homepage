from dataclasses import dataclass

import pathlib


@dataclass
class PathApi:
    app_root: pathlib.Path
    content_root: pathlib.Path

    domain: str
    debug: bool

    def get_build_path(self) -> pathlib.Path:
        return self.app_root / '.build'

    def get_content_file(self, filename: str) -> pathlib.Path:
        return self.content_root / 'data' / f'{filename}.toml'

    def get_static_url(self, relative_url: str) -> str:
        # FIXME: not needed
        # if not self.debug:
        # return f'https://static.{self.domain}{relative_url}'
        return f'/static{relative_url}'

    def get_static_path(self, use_content: bool = False) -> pathlib.Path:
        """Returns local path to static files (css sheets etc.)"""
        if use_content:
            return self.content_root / 'static'
        else:
            return self.app_root / 'static'
