"""Patch Welcome primary CTA text on Stillwall PNG exports (D-510)."""
from __future__ import annotations

import glob
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]  # Gleem/
NEW_TEXT = "Set Up in Safari"
BRAND = (0x2F, 0x6A, 0x58)


def find_font(size: int) -> ImageFont.ImageFont:
    for p in (
        r"C:\Windows\Fonts\seguisb.ttf",
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                pass
    return ImageFont.load_default()


def is_cta(c, tol: int = 32) -> bool:
    r, g, b, a = c
    if a < 200:
        return False
    if abs(r - BRAND[0]) <= tol and abs(g - BRAND[1]) <= tol and abs(b - BRAND[2]) <= tol:
        return True
    # Dark-mode mint CTA
    if 40 <= r <= 130 and 140 <= g <= 220 and 100 <= b <= 190 and g > r and g > b:
        return True
    return False


def patch(path: Path) -> bool:
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    px = im.load()

    ys = []
    for y in range(int(h * 0.52), h):
        cnt = sum(1 for x in range(int(w * 0.08), int(w * 0.92)) if is_cta(px[x, y]))
        if cnt > w * 0.22:
            ys.append(y)
    if not ys:
        print("SKIP no button", path)
        return False

    y0, y1 = min(ys), max(ys)
    mid = (y0 + y1) // 2
    xs = [x for x in range(w) if is_cta(px[x, mid])]
    if not xs:
        print("SKIP no xs", path)
        return False
    x0, x1 = min(xs), max(xs)

    samples = []
    for y in range(y0, y1 + 1, 2):
        for x in range(x0, x1 + 1, 4):
            c = px[x, y]
            if is_cta(c):
                samples.append(c[:3])
    fill = samples[len(samples) // 2] if samples else BRAND

    draw = ImageDraw.Draw(im)
    radius = max(10, (y1 - y0) // 3)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill + (255,))

    bh = max(1, y1 - y0)
    fs = max(14, int(bh * 0.36))
    font = find_font(fs)
    bbox = draw.textbbox((0, 0), NEW_TEXT, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = x0 + (x1 - x0 - tw) // 2
    ty = y0 + (y1 - y0 - th) // 2 - bbox[1]
    draw.text((tx, ty), NEW_TEXT, font=font, fill=(255, 255, 255, 255))

    im.convert("RGB").save(path, "PNG", optimize=True)
    print("OK", path.relative_to(ROOT), f"box=({x0},{y0},{x1},{y1})", f"fs={fs}")
    return True


def main() -> None:
    patterns = [
        str(ROOT / "docs/design/exports/phone-preview/*Welcome*.png"),
        str(ROOT / "docs/release/app-store-assets/screenshots/**/02-Welcome.png"),
        str(ROOT / "website/shared/assets/screenshots/01-Welcome.png"),
        str(ROOT / "issues/005-cross-screen-consistency/after/welcome.png"),
    ]
    paths: list[Path] = []
    for pat in patterns:
        paths.extend(Path(p) for p in glob.glob(pat, recursive=True))
    paths = sorted(set(paths))
    ok = sum(1 for p in paths if patch(p))
    print(f"patched {ok}/{len(paths)}")


if __name__ == "__main__":
    main()
