from .structs import Chunk as Chunk  # noqa
from .structs import Color as Color  # noqa
from .structs import IFFImage as IFFImage


def parseImage(filename: str) -> IFFImage: ...
