#!/usr/bin/env python3
"""Create an .icns from a cover image and assign it to a .dictionary bundle."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ICON_SIZES = ((16, "16x16"), (32, "16x16@2x"), (32, "32x32"), (64, "32x32@2x"),
              (128, "128x128"), (256, "128x128@2x"), (256, "256x256"), (512, "256x256@2x"),
              (512, "512x512"), (1024, "512x512@2x"))


def run(*command: str) -> None:
    subprocess.run(command, check=True)


def main(bundle: Path, image: Path) -> None:
    resources = bundle / "Contents" / "Resources"
    info_plist = bundle / "Contents" / "Info.plist"
    if not bundle.is_dir() or not resources.is_dir() or not info_plist.is_file():
        raise SystemExit("Expected a complete .dictionary bundle")
    if not image.is_file():
        raise SystemExit("Cover image not found")

    with tempfile.TemporaryDirectory() as temporary:
        iconset = Path(temporary) / "DictionaryIcon.iconset"
        iconset.mkdir()
        for pixels, name in ICON_SIZES:
            target = iconset / f"icon_{name}.png"
            run("sips", "-z", str(pixels), str(pixels), str(image), "--out", str(target))
        icon = resources / "DictionaryIcon.icns"
        run("iconutil", "-c", "icns", str(iconset), "-o", str(icon))
    run("plutil", "-replace", "CFBundleIconFile", "-string", "DictionaryIcon.icns", str(info_plist))
    print(icon)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: set_dictionary_icon.py DICTIONARY.dictionary COVER_IMAGE")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
