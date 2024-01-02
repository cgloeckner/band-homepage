import pathlib

from app.base.server import Server


class RobotsTxt:
    def __init__(self, api: Server, path_to_sitemap: str) -> None:
        self.api = api
        self.path_to_sitemap = path_to_sitemap

    def save_to_txt(self, filename: pathlib.Path) -> None:
        content = f'''User-agent: *
Disallow: 
Sitemap: ''' + self.path_to_sitemap

        with open(filename, 'w') as h:
            h.write(content)
