import tempfile
from git import Repo
from .common import logger


class DirectoryHandler:
    def __init__(self, identifier):
        self.identifier = identifier

    def prepare(self):
        raise NotImplementedError


class LocalDirectoryHandler(DirectoryHandler):
    def prepare(self):
        self.local_directory = self.identifier


class RemoteRepositoryHandler(DirectoryHandler):
    def prepare(self):
        self.local_directory = tempfile.mkdtemp()
        logger.warning(
            f"Cloning repository from {self.identifier} to {self.local_directory}"
        )
        try:
            Repo.clone_from(self.identifier, self.local_directory)
        except Exception as e:
            self.remove_local_directory()
            raise e

    def remove_local_directory(self):
        import shutil

        shutil.rmtree(self.local_directory)


class DirectoryHandlerFactory:
    @staticmethod
    def get_handler(identifier):
        if (
            identifier.startswith("http://")
            or identifier.startswith("https://")
            or identifier.endswith(".git")
        ):
            return RemoteRepositoryHandler(identifier)
        else:
            return LocalDirectoryHandler(identifier)
