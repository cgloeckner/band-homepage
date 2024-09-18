import bottle

from typing import List

from app.base.module import Module, Server


class Gallery(Module):
    def __init__(self, server: Server, cfg: dict) -> None:
        super().__init__(server, cfg)

        self.data = list()

        self.base_title = 'Galerie'

    @staticmethod
    def get_extensions() -> List[str]:
        return ['jpg', 'jpeg', 'png']

    @staticmethod
    def get_extension_wildcards() -> List[str]:
        """Transform into *.<ext> using all extensions in lowercase and uppercase version."""
        ext_list = Gallery.get_extensions()
        out = [f'*.{ext}' for ext in ext_list]
        out.extend([f'*.{ext.upper()}' for ext in ext_list])

        return out

    def load_from_disc(self) -> None:
        extensions = Gallery.get_extension_wildcards()
        root = self.server.path.get_static_path(True) / 'gallery'

        patterns = [root.glob(ext) for ext in extensions]
        self.data = [file.name for pattern in patterns for file in pattern]

        # sort by suffix of fname (e.g. artist-date-number.jpg)
        self.data.sort(key=lambda fname: fname.split('.')[0][-1])

    def render(self) -> None:
        self.template = bottle.template('gallery/index', module=self)
