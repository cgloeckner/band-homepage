import pathlib

import bottle

from . import base, server, seo
from .content import feed, contact, presskit, imprint, releases, lineup, shows, gallery, merch


class Homepage:
    def __init__(self, cfg: dict, server_impl: base.Server) -> None:
        # load feed
        self.feed = feed.Feed(server=server_impl, cfg=cfg)
        self.feed.load_from_file()
        self.feed.render()

        # load lineup
        self.lineup = lineup.Lineup(server=server_impl, cfg=cfg)
        self.lineup.load_from_file()
        self.lineup.render()

        # load live shows
        self.shows = shows.Shows(server=server_impl, cfg=cfg)
        self.shows.load_from_file()
        self.shows.render()

        # load gallery
        self.gallery = gallery.Gallery(server=server_impl, cfg=cfg)
        self.gallery.load_from_disc()
        self.gallery.render()

        # load merchandise
        self.merch = merch.Merch(server=server_impl, cfg=cfg)
        for category_str in merch.MerchCategory:
            self.merch.load_from_file(merch.MerchCategory(category_str))
        self.merch.render()

        # load releases
        self.releases = releases.Releases(server=server_impl, cfg=cfg)
        self.releases.load_from_merch(self.merch)
        self.releases.render()

        # load imprint
        self.imprint = imprint.Imprint(server=server_impl, cfg=cfg)
        self.imprint.render()

        # load contact
        self.contact = contact.Contact(server=server_impl, cfg=cfg)
        self.contact.render()

        # build presskit (as static file)
        self.presskit = presskit.Presskit(server=server_impl)
        self.presskit.build()

        # build sitemap.xml
        self.sitemap = seo.Sitemap()
        self.sitemap.append(f'https://www.{server_impl.domain}')
        self.sitemap.append(f'https://www.{server_impl.domain}/')
        self.sitemap.append(f'https://www.{server_impl.domain}/releases')
        self.sitemap.append(f'https://www.{server_impl.domain}/lineup')
        self.sitemap.append(f'https://www.{server_impl.domain}/shows')
        self.sitemap.append(f'https://www.{server_impl.domain}/gallery')
        self.sitemap.append(f'https://www.{server_impl.domain}/merch')
        self.sitemap.append(f'https://www.{server_impl.domain}/contact')
        self.sitemap.append(f'https://www.{server_impl.domain}/imprint')

        # build robots.txt
        self.robots = seo.RobotsTxt(server_impl, f'https://www.{server_impl.domain}/sitemap.xml')

    @staticmethod
    def export_html(html: str, filename: pathlib.Path) -> None:
        with open(filename, 'w') as file:
            file.write(html)


def main(data_root: pathlib.Path, cfg: dict, server_kwargs, render_only: bool):
    # setup webserver
    server_impl = server.WebServer(pathlib.Path('.'), data_root, server_kwargs)

    # load homepage
    homepage = Homepage(cfg, server_impl)

    # export html
    root = server_impl.get_build_path()
    root.mkdir(exist_ok=True)

    homepage.export_html(homepage.feed.template, root / 'index.html')
    homepage.export_html(homepage.lineup.template, root / 'lineup.html')
    homepage.export_html(homepage.shows.template, root / 'shows.html')
    homepage.export_html(homepage.gallery.template, root / 'gallery.html')
    homepage.export_html(homepage.merch.template, root / 'merch.html')
    homepage.export_html(homepage.releases.template, root / 'releases.html')
    homepage.export_html(homepage.imprint.template, root / 'imprint.html')
    homepage.export_html(homepage.contact.template, root / 'contact.html')

    # render presskit redirect page
    epk = bottle.template('epk_redirect', url=server_impl.get_static_url('/presskit.zip'))
    homepage.export_html(epk, root / 'presskit.html')

    # render sitemap and robots.txt
    homepage.sitemap.save_to_xml(server_impl.get_build_path() / 'sitemap.xml')
    homepage.robots.save_to_txt(server_impl.get_build_path() / 'robots.txt')

    if render_only:
        return

    if not server_kwargs['reverse_proxy']:
        @server_impl.app.get('/static/<filename>')
        def static_files(filename: str):
            static_root = server_impl.get_static_path()
            return bottle.static_file(filename, root=static_root)

        @server_impl.app.get('/static/content/<path:path>')
        def static_content(path: str):
            static_root = server_impl.get_static_path(True)
            return bottle.static_file(path, root=static_root)

    @server_impl.app.get('/')
    def feed_page():
        return homepage.feed.template

    @server_impl.app.get('/releases')
    def releases_page():
        return homepage.releases.template

    @server_impl.app.get('/lineup')
    def lineup_page():
        return homepage.lineup.template

    @server_impl.app.get('/shows')
    def shows_page():
        return homepage.shows.template

    @server_impl.app.get('/gallery')
    def gallery_page():
        return homepage.gallery.template

    @server_impl.app.get('/merch')
    def merch_page():
        return homepage.merch.template

    @server_impl.app.get('/imprint')
    def impressum_page():
        return homepage.imprint.template

    @server_impl.app.get('/contact')
    def contact_page():
        return homepage.contact.template

    @server_impl.app.get('/presskit')
    def static_presskit():
        path = pathlib.Path(homepage.presskit.zip_file)
        return bottle.static_file(path.name, root=path.parent, download=f'{server_impl.domain} EPK.zip',
                                  mimetype='application/zip')

    @server_impl.app.get('/robots.txt')
    def robots_txt():
        robots_root = server_impl.get_build_path()
        return bottle.static_file('robots.txt', root=robots_root)

    @server_impl.app.get('/sitemap.xml')
    def robots_txt():
        robots_root = server_impl.get_build_path()
        return bottle.static_file('sitemap.xml', root=robots_root)

    server_impl.run()
