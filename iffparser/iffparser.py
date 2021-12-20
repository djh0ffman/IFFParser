# Amiga IFF Parser
# Hoffman
# coded: 2019-07-04, first experience with py

# usage: import the parser and call parseImage with the file name
# it'll return the IFFImage class

import io
from typing import IO

from .structs import Chunk, Color, IFFImage

# IFF Chunk class
# type = 4 character type (FORM etc.)
# size = binary data size
# data = binary data


# Parse Image
# Provide file name and it returns the IFF Image
def parseImage(filename: str) -> IFFImage:
    image = IFFImage()
    with open(filename, "rb") as f:
        __isiff(f)
        # read all chunks into array till end of file
        chunks = []
        while f.read(1):
            f.seek(-1, 1)
            chunkType = f.read(4).decode("ascii")
            chunkSize = __readLong(f)
            chunkData = f.read(chunkSize)
            if chunkSize > 0:
                chunks.append(Chunk(chunkType, chunkSize, chunkData))

    # parse each chunk
    for c in chunks:
        __parseChunk(c, image)

    return image


def __isiff(f: IO) -> None:
    # check FORM
    if f.read(4) != b"FORM":
        raise Exception("not an IFF")

    # check size
    filesize = __readLong(f)
    if len(f.read(filesize)) != filesize:
        raise Exception("IFF corrupt")

    # seek back to start
    f.seek(8, 0)
    if f.read(4) != b"ILBM":
        raise Exception("not an IFF")


def __parseChunk(chunk: Chunk, image: IFFImage) -> None:
    if chunk.type == "BMHD":
        __parseBitmapHeader(chunk, image)
    elif chunk.type == "BODY":
        __parseBody(chunk, image)
    elif chunk.type == "CMAP":
        __parseColorMap(chunk, image)
    return None


def __parseColorMap(chunk: Chunk, image: IFFImage) -> None:
    if chunk.size / 3 != pow(2, image.header.bitplanes):
        raise Exception("Color map is corrupt")

    c = chunk.size / 3
    f = io.BytesIO(chunk.data)
    while c > 0:
        color = Color(__readByte(f), __readByte(f), __readByte(f))
        image.colorMap.append(color)
        c -= 1
    return None


def __parseBody(chunk: Chunk, image: IFFImage) -> None:
    c = image.header.compress
    if c == 0:
        image.body = chunk.data
    elif c == 1:
        image.body = __runLengthUnpack(chunk.data)
    else:
        raise Exception("Unknown compression method")

    if image.header.width / 8 * image.header.height * image.header.bitplanes != len(
        image.body
    ):
        raise Exception("Uncompressed data not correct size")
    return None


def __parseBitmapHeader(chunk: Chunk, image: IFFImage) -> None:
    f = io.BytesIO(chunk.data)
    image.header.width = __readWord(f)
    image.header.height = __readWord(f)
    image.header.left = __readWord(f)
    image.header.top = __readWord(f)
    image.header.bitplanes = __readByte(f)
    image.header.masking = __readByte(f)
    image.header.compress = __readByte(f)
    image.header.padding = __readByte(f)
    image.header.transparency = __readWord(f)
    image.header.xAspectRatio = __readByte(f)
    image.header.yAspectRatio = __readByte(f)
    image.header.pageWidth = __readWord(f)
    image.header.pageHeight = __readWord(f)
    return None


# run length unpacker
def __runLengthUnpack(data: bytes) -> bytes:
    source = io.BytesIO(data)
    output = io.BytesIO()
    current = source.read(1)

    while current != b"":
        value = int.from_bytes(current, "big", signed=True)
        if 0 <= value <= 127:  # literal copy
            output.write(source.read(value + 1))
        elif -127 <= value <= -1:  # byte copy
            value = -value + 1
            dupe = source.read(1)
            while value > 0:
                output.write(dupe)
                value = value - 1

        current = source.read(1)

    output.seek(0, 0)
    data = output.read()
    return data


# function for reading byte as int
def __readByte(f: IO) -> int:
    return int.from_bytes(f.read(1), "big")


# function for reading byte as int
def __readByteS(f: IO) -> int:
    return int.from_bytes(f.read(1), "big", signed=True)


# function for reading big endian word
def __readWord(f: IO) -> int:
    return int.from_bytes(f.read(2), "big")


# function for reading big endian long word
def __readLong(f: IO) -> int:
    return int.from_bytes(f.read(4), "big")
