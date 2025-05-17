from dataclasses import dataclass

import pathlib


@dataclass
class PathApi:
    app_root: pathlib.Path
    data_root: pathlib.Path

    domain: str
    debug: bool

    def get_config_file(self, filename: str, ext: str = 'toml') -> pathlib.Path:
        return self.data_root / f'{filename}.{ext}'

    def get_www_path(self) -> pathlib.Path:
        return self.app_root / 'www'

    def get_static_path(self) -> pathlib.Path:
        """Returns local path to static files (css sheets etc.)"""
        return self.app_root / 'static'
