from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont

PROJECT = Path(r"D:\cropdoc-ai")

# Use the exact dataset you already prepared for CropDoc AI.
SEARCH_DIRS = [
    PROJECT / "data",
    PROJECT / "PlantVillage",
]

CLASSES = [
    ("healthy", ["healthy", "Potato___healthy"]),
    ("early_blight", ["early_blight", "Potato___Early_blight"]),
    ("late_blight", ["late_blight", "Potato___Late_blight"]),
]

OUT_DIR = PROJECT / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

A4_W, A4_H = 2480, 3508   # A4 at 300 DPI
MARGIN = 120
GAP = 70
HEADER_H = 300
CELL_W = (A4_W - 2*MARGIN - GAP) // 2
CELL_H = (A4_H - 2*MARGIN - HEADER_H - 2*GAP) // 3
IMAGE_H = CELL_H - 110

def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

title_font = font(82, True)
subtitle_font = font(36)
label_font = font(42, True)
small_font = font(28)

def find_class_dir(names):
    for base in SEARCH_DIRS:
        if not base.exists():
            continue
        for name in names:
            p = base / name
            if p.exists() and p.is_dir():
                return p
    return None

def get_images(folder):
    if folder is None:
        return []
    exts = {".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"}
    return sorted([p for p in folder.rglob("*") if p.suffix in exts])

# Select two deterministic samples from each class.
selected = []
for label, names in CLASSES:
    folder = find_class_dir(names)
    imgs = get_images(folder)
    if len(imgs) < 2:
        raise RuntimeError(f"Could not find 2 images for {label}. Checked: {names}")
    # Spread the two samples through the class rather than taking adjacent files.
    picks = [imgs[0], imgs[len(imgs)//2]]
    selected.extend([(label, p) for p in picks])

sheet = Image.new("RGB", (A4_W, A4_H), "white")
draw = ImageDraw.Draw(sheet)

draw.text((MARGIN, 70), "CropDoc AI — Potato Leaf Test Sheet",
          fill="black", font=title_font)
draw.text((MARGIN, 175),
          "Print at 100% scale • Use the camera to test Healthy / Early Blight / Late Blight",
          fill="black", font=subtitle_font)

positions = []
for row in range(3):
    for col in range(2):
        x = MARGIN + col * (CELL_W + GAP)
        y = MARGIN + HEADER_H + row * (CELL_H + GAP)
        positions.append((x, y))

for (label, path), (x, y) in zip(selected, positions):
    draw.rounded_rectangle(
        (x, y, x + CELL_W, y + CELL_H),
        radius=25, outline="black", width=5
    )

    img = Image.open(path).convert("RGB")
    img = ImageOps.contain(img, (CELL_W - 40, IMAGE_H - 20))

    ix = x + (CELL_W - img.width)//2
    iy = y + 20
    sheet.paste(img, (ix, iy))

    display_label = {
        "healthy": "HEALTHY",
        "early_blight": "EARLY BLIGHT",
        "late_blight": "LATE BLIGHT",
    }[label]

    draw.text((x + 30, y + CELL_H - 75),
              display_label, fill="black", font=label_font)

sheet_path = OUT_DIR / "potato_leaf_print_sheet.png"
pdf_path = OUT_DIR / "potato_leaf_print_sheet.pdf"

sheet.save(sheet_path, dpi=(300, 300))
sheet.save(pdf_path, "PDF", resolution=300.0)

print("Created:")
print(sheet_path)
print(pdf_path)
print()
print("6 samples: 2 Healthy + 2 Early Blight + 2 Late Blight")
