import argparse

from . import iffparser as iffparser  # noqa


def check_isfile(v: str) -> str: ...
def check_isdir(v: str) -> str: ...
def parse_args() -> argparse.Namespace: ...
def main() -> None: ...