import argparse
from os.path import isdir, isfile

from . import __version__, iffparser


# type: (str) -> str
def check_isfile(v):
    if not isfile(v):
        raise argparse.ArgumentTypeError("%s is not file" % v)
    else:
        return v


# type: (str) -> str
def check_isdir(v):
    if not isdir(v):
        raise argparse.ArgumentTypeError("%s is not file" % v)
    else:
        return v


# type: (None) -> argparse.Namespace
def parse_args():
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


# type: (None) -> None
def main():
    args = parse_args()
    i = iffparser.parseImage(args.iff_file)
    print(i)


if __name__ == "__main__":
    main()
