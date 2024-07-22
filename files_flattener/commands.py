import sys
from .core import list_files, write_files_to_output
from .common import logger, print_usage
from abc import ABC, abstractmethod


class Invoker:
    def invoke(self, command):
        command._execute()


class Context:
    def flat_files(self, identifier, output_file, ignore_file=None):
        try:
            files_list, handler = list_files(identifier, ignore_file)
            for file in files_list:
                logger.info(file)
            write_files_to_output(handler, output_file, files_list)
            logger.success(f"All files have been successfully written to {output_file}")
            sys.exit(0)
        except Exception:
            sys.exit(1)

    def help(self):
        print_usage()
        sys.exit(1)


class Command(ABC):
    def __init__(self, ctx: Context):
        self.ctx = ctx

    @abstractmethod
    def _execute(self):
        pass


class FlatFilesCommand(Command):
    def __init__(self, ctx, identifier, output_file, ignore_file=None):
        super().__init__(ctx)
        self.identifier = identifier
        self.output_file = output_file
        self.ignore_file = ignore_file

    def _execute(self):
        self.ctx.flat_files(self.identifier, self.output_file, self.ignore_file)


class HelpCommand(Command):
    def __init__(self, ctx):
        super().__init__(ctx)

    def _execute(self):
        self.ctx.help()


invoker = Invoker()

__all__ = ["invoker", "Context"]
