import argparse
from os.path import isdir, isfile

from . import __version__, iffparser


def check_isfile(v: str) -> str:
    if not isfile(v):
        raise argparse.ArgumentTypeError("%s is not file" % v)
    else:
        return v


def check_isdir(v: str) -> str:
    if not isdir(v):
        raise argparse.ArgumentTypeError("%s is not file" % v)
    else:
        return v


def parse_args() -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog="iffp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="IFF graphics parser",
    )
    parser.add_argument(
        "iff_file", metavar="FILE", type=check_isfile, help="iff file path"
    )
    parser.add_argument(
        "-o", "--outdir", type=check_isdir, help="output dir", default="."
    )
    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s {}".format(__version__)
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    i = iffparser.parseImage(args.iff_file)
    print(i)


if __name__ == "__main__":
    main()
