import sys
from .commands import invoker, Context
from .commands import FlatFilesCommand, HelpCommand


def main():
    ctx = Context()

    if len(sys.argv) < 3:
        invoker.invoke(HelpCommand(ctx))

    identifier = sys.argv[1]
    output_file = sys.argv[2]
    ignore_file = sys.argv[3] if len(sys.argv) > 3 else None  # Optional

    invoker.invoke(FlatFilesCommand(ctx, identifier, output_file, ignore_file))


if __name__ == "__main__":
    main()
