import re
import zipfile
import os
import shutil
import bottle

from app import base


class Download:
    def __init__(self, server: base.Server, filename: str) -> None:
        self.path = server.path.get_www_path() / 'content' / Download.sanitize(filename)

    @staticmethod
    def sanitize(filename: str) -> str:
        sanitized = re.sub(r'[\\/*?:"<>|\s]+', '_', filename)
        return sanitized.strip()

    def get_filename(self) -> str:
        return self.path.name

    def get_url(self) -> str:
        return f'/content/{self.get_filename()}' 

    def get_size(self) -> str:
        num_bytes = os.path.getsize(self.path)
        num_mb = num_bytes / (1024 ** 2)
        return f'{num_mb:.1f} MB'.replace('.', ',')


class Epk(Download):
    def __init__(self, server: base.Server, filename: str) -> None:
        super().__init__(server, filename)
        
        # create zip archive
        root = server.path.data_root / 'presskit'
        with zipfile.ZipFile(self.path, 'w') as handle:
            for file in root.glob('**/*'):
                handle.write(file, arcname=file.relative_to(root))


class Rider(Download):
    def __init__(self, server: base.Server, filename: str) -> None:
        super().__init__(server, filename)

        # copy pdf to public folder
        shutil.copy(server.path.data_root / 'rider.pdf', self.path)


class Contact(base.Module):
    def __init__(self, server: base.Server, cfg: dict) -> None:
        super().__init__(server, cfg)

        self.contact = cfg['contact']

        prefix = cfg['band_name']
        self.epk = Epk(server, f'{prefix}_Presskit.zip')
        self.rider = Rider(server, f'{prefix}_Stagerider.pdf')

    def render(self) -> None:
        self.template = bottle.template('contact', module=self)
