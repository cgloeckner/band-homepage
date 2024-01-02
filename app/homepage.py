import pathlib

import bottle

from . import base, content, seo


class Homepage:
    def __init__(self, server: base.Server, cfg: dict) -> None:
        # load feed
        self.feed = content.Feed(server=server, cfg=cfg)
        self.feed.load_from_file()
        self.feed.render()

        # load lineup
        self.lineup = content.Lineup(server=server, cfg=cfg)
        self.lineup.load_from_file()
        self.lineup.render()

        # load live shows
        self.shows = content.Shows(server=server, cfg=cfg)
        self.shows.load_from_file()
        self.shows.render()

        # load gallery
        self.gallery = content.Gallery(server=server, cfg=cfg)
        self.gallery.load_from_disc()
        self.gallery.render()

        # load merchandise
        self.merch = content.Merch(server=server, cfg=cfg)
        for category_str in content.MerchCategory:
            self.merch.load_from_file(content.MerchCategory(category_str))
        self.merch.render()

        # load releases
        self.releases = content.Releases(server=server, cfg=cfg)
        self.releases.load_from_merch(self.merch)
        self.releases.render()

        # load imprint
        self.imprint = content.Imprint(server=server, cfg=cfg)
        self.imprint.render()

        # load contact
        self.contact = content.Contact(server=server, cfg=cfg)
        self.contact.render()

        # build presskit (as static file)
        self.presskit = content.Presskit(server=server)
        self.presskit.build()

        # build sitemap.xml
        self.sitemap = seo.Sitemap()
        self.sitemap.append(f'https://www.{server.domain}')
        self.sitemap.append(f'https://www.{server.domain}/')
        self.sitemap.append(f'https://www.{server.domain}/releases')
        self.sitemap.append(f'https://www.{server.domain}/lineup')
        self.sitemap.append(f'https://www.{server.domain}/shows')
        self.sitemap.append(f'https://www.{server.domain}/gallery')
        self.sitemap.append(f'https://www.{server.domain}/merch')
        self.sitemap.append(f'https://www.{server.domain}/contact')
        self.sitemap.append(f'https://www.{server.domain}/imprint')

        # build robots.txt
        self.robots = seo.RobotsTxt(server, f'https://www.{server.domain}/sitemap.xml')

    @staticmethod
    def export_html(html: str, filename: pathlib.Path) -> None:
        with open(filename, 'w') as file:
            file.write(html)
