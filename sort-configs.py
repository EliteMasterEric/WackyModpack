"""
Sort the keys within each section of BepInEx .cfg files, to keep git diffs small.

BepInEx already writes sections in sorted order, but keys are written in the order
each mod binds them, which shifts around between mod updates. Each key is moved
together with the blank and comment lines above it. Section order, values, line
endings, and encoding are left untouched.

Usage: python sort-configs.py <folder or file> [...]
"""

import re
import sys
from pathlib import Path

SECTION_RE = re.compile(r"^\s*\[.*\]\s*$")
KEY_RE = re.compile(r"^\s*([^#=\s][^=]*?)\s*=")
BOM = "\ufeff"


def sort_config(text: str) -> str:
    # Keep each line's own terminator, since some files mix CRLF and LF.
    missing_eol = not text.endswith("\n")
    if missing_eol:
        text += "\n"
    lines = re.findall(r"[^\n]*\n", text)

    out = []
    blocks = []  # (key, lines) for the current section
    pending = []  # blank/comment lines waiting for the key they describe

    def flush_section():
        blocks.sort(key=lambda b: (b[0].casefold(), b[0]))
        for _, block in blocks:
            out.extend(block)
        out.extend(pending)
        blocks.clear()
        pending.clear()

    in_section = False
    for line in lines:
        stripped = line.strip()
        if SECTION_RE.match(stripped):
            flush_section()
            out.append(line)
            in_section = True
        elif not in_section:
            out.append(line)  # File header
        elif (match := KEY_RE.match(stripped)) is not None:
            blocks.append((match.group(1), pending + [line]))
            pending.clear()
        elif stripped == "" or stripped.startswith("#"):
            pending.append(line)
        else:
            raise ValueError(f"Unrecognized line: {stripped!r}")
    flush_section()

    result = "".join(out)
    if missing_eol:
        result = result.rstrip("\r\n")
    return result


def process(path: Path) -> bool:
    raw = path.read_bytes().decode("utf-8")
    has_bom = raw.startswith(BOM)
    text = raw[1:] if has_bom else raw
    try:
        result = sort_config(text)
    except ValueError as e:
        print(f"Skipped {path}: {e}")
        return False
    if result == text:
        return False
    path.write_bytes(((BOM if has_bom else "") + result).encode("utf-8"))
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        sys.exit(1)
    changed = 0
    for arg in sys.argv[1:]:
        root = Path(arg)
        files = [root] if root.is_file() else sorted(root.rglob("*.cfg"))
        for path in files:
            if process(path):
                changed += 1
                print(f"Sorted {path}")
    print(f"{changed} file(s) changed.")


if __name__ == "__main__":
    main()
