from typing import List


class Chunk:
    type: str
    size: int
    data: bytes


class Color:
    red: int
    green: int
    blue: int


class BitmapHeader:
    width: int
    height: int
    left: int
    top: int
    bitplanes: int
    masking: int
    compress: int
    padding: int
    transparency: int
    xAspectRatio: int
    yAspectRatio: int
    pageWidth: int
    pageHeight: int


class IFFImage:
    header: BitmapHeader
    body: bytes
    colorMap: List[Color]
