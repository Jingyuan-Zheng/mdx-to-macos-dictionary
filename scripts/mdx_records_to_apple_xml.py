#!/usr/bin/env python3
"""Turn mdict's extracted HTML records into Apple Dictionary XML."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

VOID_TAGS = re.compile(r"<(?:hr|br|img|meta|link|input)(?:\s+[^<>]*?)?/?>", re.I)
SCRIPT_TAGS = re.compile(r"<script\b[^>]*>.*?</script\s*>", re.I | re.S)
EVENT_ATTRS = re.compile(r"\s+on[a-z]+\s*=\s*(?:\"[^\"]*\"|'[^']*')", re.I)
BARE_AMPS = re.compile(r"&(?!#\d+;|#x[0-9a-fA-F]+;|[a-zA-Z][a-zA-Z0-9]+;)")


def clean(fragment: str) -> str:
    fragment = SCRIPT_TAGS.sub("", fragment)
    fragment = EVENT_ATTRS.sub("", fragment)
    fragment = fragment.replace("</star>", "</span>")
    fragment = VOID_TAGS.sub(lambda m: m.group(0).rstrip("/>").rstrip() + "/>", fragment)
    return BARE_AMPS.sub("&amp;", fragment)


def main(source: Path, destination: Path) -> None:
    records = source.read_text(encoding="utf-8").split("\n</>\n")
    if len(records) < 2:
        raise SystemExit("No MDX record separator found")
    with destination.open("w", encoding="utf-8", newline="\n") as output:
        output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        output.write('<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">\n')
        for number, record in enumerate(records, 1):
            key, separator, body = record.partition("\n")
            if not separator or not key.strip():
                continue
            key = key.strip()
            escaped_key = html.escape(key, quote=True)
            output.write(f'<d:entry id="entry_{number}" d:title="{escaped_key}">\n')
            output.write(f'<d:index d:value="{escaped_key}"/>\n{clean(body)}\n</d:entry>\n')
        output.write("</d:dictionary>\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: mdx_records_to_apple_xml.py INPUT.txt OUTPUT.xml")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
