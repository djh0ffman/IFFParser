# Amiga IFF Parser
# Hoffman
# coded: 2019-07-04, first experience with py

# usage: import the parser and call parseImage with the file name
# it'll return the IFFImage class
from dataclasses import dataclass, field
from typing import List


# IFF Chunk class
# type = 4 character type (FORM etc.)
# size = binary data size
# data = binary data
@dataclass
class Chunk:
    type: str = ""
    size: int = 0
    data: bytes = b""


@dataclass
class Color:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass
class BitmapHeader:
    width: int = 0
    height: int = 0
    left: int = 0
    top: int = 0
    bitplanes: int = 0
    masking: int = 0
    compress: int = 0
    padding: int = 0
    transparency: int = 0
    xAspectRatio: int = 0
    yAspectRatio: int = 0
    pageWidth: int = 0
    pageHeight: int = 0


# IFF Image Class
@dataclass
class IFFImage:
    header: BitmapHeader = BitmapHeader()
    body: bytes = b""
    colorMap: List[Color] = field(default_factory=list)
