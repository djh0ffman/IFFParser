# IFFParser
IFF graphics parser written in Python

To learn Python I wrote a parser for IFF files, a bitmap graphic file format used on the amiga. Currently only supports the following IFF chunks.

BMHD - Bitmap Header
CAMP - Color Map
BODY - Bitmap data

If the body is compressed using run length encoding, the data is uncompressed before being passed back out.

Could be useful for your Amiga demo code tool chains to auto convert IFF's to RAW bitmaps. May add some new features in the future.
