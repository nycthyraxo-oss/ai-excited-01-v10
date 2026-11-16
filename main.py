"""Copy entry.png to output.png after a JPEG magic check."""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(__file__), "entry.png")
DST = os.path.join(os.path.dirname(__file__), "output.png")


def validate(path):
    size = os.path.getsize(path)
    if size > 1048576:
        print(f"entry.png is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return False
    with open(path, "rb") as f:
        data = f.read()
    if data[:2] != b"\xff\xd8":
        print("entry.png is missing the JPEG SOI marker", file=sys.stderr)
        return False
    if data[-2:] != b"\xff\xd9":
        print("entry.png is missing the JPEG EOI marker", file=sys.stderr)
        return False
    i = 2
    width = None
    height = None
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC2):
            height = (data[i + 5] << 8) | data[i + 6]
            width = (data[i + 7] << 8) | data[i + 8]
            break
        if marker == 0xDA:
            break
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        length = (data[i + 2] << 8) | data[i + 3]
        i += 2 + length
    if width is None or height is None:
        print("entry.png has no SOF segment", file=sys.stderr)
        return False
    if width > 1024 or height > 1024:
        print(f"entry.png is {width}x{height}, over the 1024x1024 limit", file=sys.stderr)
        return False
    print(f"validated entry.png: {width}x{height}, {size} bytes")
    return True


def main():
    with open(SRC, "rb") as f:
        head = f.read(2)
    if head != b"\xff\xd8":
        print("entry.png is not a JPEG", file=sys.stderr)
        return 1
    if not validate(SRC):
        return 1
    shutil.copyfile(SRC, DST)
    size = os.path.getsize(DST)
    print(f"copied {SRC} -> {DST} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
