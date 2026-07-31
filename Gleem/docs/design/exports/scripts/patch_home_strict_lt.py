"""Replace Large Type Strict subtitle 'May affect some sites' with locked copy."""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
PATH = ROOT / "docs/design/exports/phone-preview/11-Home-LargeType.png"
NEW = "Stronger blocking · Use with care"
AFTER = ROOT / "issues/005-cross-screen-consistency/after/home-large-type.png"


def find_font(size: int):
    for p in (r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                pass
    return ImageFont.load_default()


def patch(path: Path) -> None:
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    # Strict row subtitle approx lower third of list
    sx, sy = w / 780.0, h / 1688.0
    box = (int(150 * sx), int(1180 * sy), int(560 * sx), int(1235 * sy))
    px = im.load()
    samples = []
    for y in range(box[1], box[3], 2):
        for x in range(box[0], box[2], 4):
            samples.append(px[x, y][:3])
    samples.sort()
    bg = samples[len(samples) // 2] if samples else (255, 255, 255)
    draw.rectangle(box, fill=bg + (255,))
    font = find_font(max(12, int(22 * min(sx, sy))))
    draw.text((box[0], box[1] + 2), NEW, font=font, fill=(120, 120, 128, 255))
    im.convert("RGB").save(path, "PNG", optimize=True)
    print("OK", path)


def main():
    for p in (PATH, AFTER):
        if p.exists():
            patch(p)


if __name__ == "__main__":
    main()
