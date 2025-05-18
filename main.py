from gevent import monkey; monkey.patch_all()

import sys
import yaml
import pathlib
import bottle

import app


"""
def run(server: app.Server, homepage: app.Homepage) -> None:
    if server.debug:
        @server.app.get('/static/<filename>')
        def static_files(filename: str):
            static_root = server.path.get_static_path()
            return bottle.static_file(filename, root=static_root)

        @server.app.get('/static/content/<path:path>')
        def static_content(path: str):
            static_root = server.path.get_static_path()
            return bottle.static_file(path, root=static_root)

    @server.app.get('/')
    def feed_page():
        return homepage.feed.template

    @server.app.get('/releases')
    def releases_page():
        return homepage.releases.template

    @server.app.get('/lineup')
    def lineup_page():
        return homepage.lineup.template

    @server.app.get('/shows')
    def shows_page():
        return homepage.shows.template

    @server.app.get('/gallery')
    def gallery_page():
        return homepage.gallery.template

    @server.app.get('/merch')
    def merch_page():
        return homepage.merch.template

    @server.app.get('/imprint')
    def impressum_page():
        return homepage.imprint.template

    @server.app.get('/contact')
    def contact_page():
        return homepage.contact.template

    @server.app.get('/presskit')
    def static_presskit():
        path = pathlib.Path(homepage.presskit.zip_file)
        return bottle.static_file(path.name, root=path.parent, download=f'{homepage.cfg["band_name"]} EPK.zip',
                                  mimetype='application/zip')

    @server.app.get('/robots.txt')
    def robots_txt():
        robots_root = server.path.get_www_path()
        return bottle.static_file('robots.txt', root=robots_root)

    @server.app.get('/sitemap.xml')
    def robots_txt():
        robots_root = server.path.get_www_path()
        return bottle.static_file('sitemap.xml', root=robots_root)

    server.run()
"""


def export_html(server: app.Server, homepage: app.Homepage) -> None:
    # export html
    root = server.path.get_www_path()
    root.mkdir(exist_ok=True)

    homepage.export_html(homepage.feed.template, root / 'index.html')
    homepage.export_html(homepage.lineup.template, root / 'lineup.html')
    homepage.export_html(homepage.shows.template, root / 'shows.html')
    homepage.export_html(homepage.gallery.template, root / 'gallery.html')
    homepage.export_html(homepage.merch.template, root / 'merch.html')
    homepage.export_html(homepage.releases.template, root / 'releases.html')
    homepage.export_html(homepage.imprint.template, root / 'imprint.html')
    homepage.export_html(homepage.contact.template, root / 'contact.html')

    # render sitemap and robots.txt
    homepage.sitemap.save_to_xml(server.path.get_www_path() / 'sitemap.xml')
    homepage.robots.save_to_txt(server.path.get_www_path() / 'robots.txt')


def main() -> None:
    content_root = pathlib.Path('data')
    
    with open(content_root / 'settings.yaml', 'r') as handle:
        config = yaml.safe_load(handle)

    with open(content_root / 'biography.html', 'r') as handle:
        config['biography'] = handle.read()

    port = 8080
    debug = '--debug' in sys.argv

    if '-p' in sys.argv:
        index = sys.argv.index('-p')
        port = int(sys.argv[index + 1])

    # load server and homepage
    server = app.Server(app_root=pathlib.Path('.'), content_root=content_root, domain=config['domain'],
                        debug=debug, host='0.0.0.0', port=port, server='gevent')

    homepage = app.Homepage(server, config)
    export_html(server, homepage)


if __name__ == '__main__':
    main()
