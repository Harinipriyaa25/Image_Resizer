import os
from PIL import Image, ImageOps, UnidentifiedImageError
import shutil

# -------------------- SETTINGS --------------------
INPUT_FOLDER = "images_input"      # folder with your original images
OUTPUT_FOLDER = "images_output"    # output folder for converted images
MAX_SIZE = (1024, 1024)            # max width, height
JPEG_QUALITY = 80                  # JPEG quality (1–95)
BACKGROUND_COLOR = (255, 255, 255) # background for transparent images (white)
# --------------------------------------------------

# make output folder if missing
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def is_image_file(fname):
    fname = fname.lower()
    return fname.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp'))

def process_image(src_path):
    base_name = os.path.splitext(os.path.basename(src_path))[0]
    dst_path = os.path.join(OUTPUT_FOLDER, base_name + ".jpg")
    temp_path = dst_path + ".tmp"

    try:
        with Image.open(src_path) as im:
            # Fix EXIF rotation
            im = ImageOps.exif_transpose(im)

            # Handle palette
            if im.mode == "P":
                im = im.convert("RGBA")

            # Handle transparency
            if "A" in im.getbands():
                bg = Image.new("RGB", im.size, BACKGROUND_COLOR)
                bg.paste(im, mask=im.split()[-1])
                im = bg
            else:
                im = im.convert("RGB")

            # Resize with aspect ratio
            im.thumbnail(MAX_SIZE, Image.LANCZOS)

            # Save candidate JPEG
            im.save(temp_path, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)

        orig_size = os.path.getsize(src_path)
        new_size = os.path.getsize(temp_path)

        # Keep smaller version
        if new_size < orig_size:
            shutil.move(temp_path, dst_path)
            print(f"✔ Saved optimized: {dst_path} ({im.width}x{im.height}, {new_size/1024:.1f} KB)")
        else:
            os.remove(temp_path)
            shutil.copy2(src_path, dst_path)
            print(f"⚠ Original kept: {dst_path} (smaller than recompressed)")

    except UnidentifiedImageError:
        print(f"✘ Not an image: {src_path}")
    except Exception as e:
        print(f"✘ Error with {src_path}: {e}")

def main():
    if not os.path.exists(INPUT_FOLDER):
        print(f"Input folder '{INPUT_FOLDER}' not found.")
        return

    files = [f for f in os.listdir(INPUT_FOLDER) if is_image_file(f)]
    if not files:
        print(f"No images found in '{INPUT_FOLDER}'.")
        return

    for f in files:
        src = os.path.join(INPUT_FOLDER, f)
        process_image(src)

    print("\n🎉 Done! Check your 'images_output' folder.")

if __name__ == "__main__":
    main()



