"""Render cover.svg to cover.png for the weekly CLO draft. Zero API spend.
Usage: python scripts/render-cover.py assets/cover-template.svg drafts/2026-09-23-slug/cover.png
Tries cairosvg, then rsvg-convert, then Pillow fallback with a flat CLO brand card.
Requires hook text already substituted into the SVG by the visual-builder agent.
"""
import shutil
import subprocess
import sys

INK = (11, 11, 16)
YELLOW = (255, 210, 31)
MAGENTA = (255, 46, 126)
PAPER = (245, 241, 230)


def main(src, dst):
    try:
        import cairosvg
        cairosvg.svg2png(url=src, write_to=dst, output_width=1080, output_height=1350)
        print(f"rendered with cairosvg: {dst}")
        return
    except Exception as e:
        print(f"cairosvg unavailable ({e}), trying rsvg-convert")
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", "1080", "-h", "1350", "-o", dst, src], check=True)
        print(f"rendered with rsvg-convert: {dst}")
        return
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (1080, 1350), INK)
    d = ImageDraw.Draw(img)
    d.rectangle([60, 60, 1020, 480], fill=PAPER)
    d.rectangle([60, 60, 74, 480], fill=YELLOW)
    d.rectangle([60, 1150, 1020, 1290], outline=YELLOW, width=6)
    d.ellipse([964, 64, 1016, 116], fill=MAGENTA)
    d.text((110, 200), "THE CLO JOURNAL", fill=YELLOW)
    d.text((110, 1200), "READ THE ARTICLE. PICK THE SUPERPOWER.", fill=YELLOW)
    img.save(dst)
    print(f"rendered fallback flat card (install cairosvg for full SVG): {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
