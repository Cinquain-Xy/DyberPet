#!/usr/bin/env python3
"""
Generate SHA256 checksums for release artifacts in a directory.

Usage:
  python scripts/release_hash.py dist
"""

from __future__ import annotations
import hashlib
import pathlib
import sys

CHUNK_SIZE = 1024 * 1024


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/release_hash.py <artifact_dir>")
        return 1

    artifact_dir = pathlib.Path(sys.argv[1]).resolve()
    if not artifact_dir.exists() or not artifact_dir.is_dir():
        print(f"Invalid directory: {artifact_dir}")
        return 1

    files = sorted([p for p in artifact_dir.rglob("*") if p.is_file()])
    if not files:
        print("No files found.")
        return 1

    output = artifact_dir / "SHA256SUMS.txt"
    lines = []
    for f in files:
        if f.name == "SHA256SUMS.txt":
            continue
        digest = sha256_file(f)
        rel = f.relative_to(artifact_dir).as_posix()
        lines.append(f"{digest}  {rel}")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
