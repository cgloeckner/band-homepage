import zipfile

from controller.base.module import Server


class Presskit:
    def __init__(self, server: Server) -> None:
        self.server = server
        self.root = server.model_root / 'presskit'
        self.zip_file = server.model_root / 'presskit.zip'

    def build(self) -> None:
        """Zips all files and folders."""
        with zipfile.ZipFile(self.zip_file, 'w') as handle:
            for file in self.root.glob('**/*'):
                handle.write(file, arcname=file.relative_to(self.root))
