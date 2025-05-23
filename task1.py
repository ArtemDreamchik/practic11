from glob import glob
from PIL import Image, ImageFilter
import os

input_folder = "images"
output_folder = "images/task3editedImages"

os.makedirs(output_folder, exist_ok=True)

image_files = glob("images/[1-5].jpg")

for file in image_files:
    img = Image.open(file)

    filtered_img = img.filter(ImageFilter.DETAIL)

    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)

    save_path = os.path.join(output_folder, f"{name}_filtered{ext}")

    filtered_img.save(save_path)