import sys
import yaml
import pathlib

import controller


def main(data_root: pathlib.Path, cfg: dict):
    server_kwargs = {
        'host': '0.0.0.0',
        'server': 'gevent',
        'domain': cfg['domain'],
        'port': 8000,
        'debug': '--debug' in sys.argv,
        'reloader': '--debug' in sys.argv,
        'quiet': '--debug' not in sys.argv,
        'reverse_proxy': '--debug' not in sys.argv
    }

    if '-p' in sys.argv:
        index = sys.argv.index('-p')
        server_kwargs['port'] = int(sys.argv[index + 1])

    if '-h' in sys.argv:
        print('Usage: -p <portnumber>')
        return

    controller.main(data_root, cfg, server_kwargs, '--render' in sys.argv)


if __name__ == '__main__':
    sys.argv.append('--debug')

    # example
    model = pathlib.Path('..') / 'kali-yuga.de' / 'model'

    with open(model / 'settings.yaml', 'r') as handle:
        config = yaml.safe_load(handle)

    with open(model / 'biography.html', 'r') as handle:
        config['biography'] = handle.read()

    main(model, config)
