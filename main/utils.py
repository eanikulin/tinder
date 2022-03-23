import os

from PIL import Image
from django.conf import settings

path_watermark = os.path.join(settings.BASE_DIR, "media" + '\watermark.png')


def watermark_photo(input_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(path_watermark)
    base_image.paste(watermark, (0, 0))
    base_image.save(input_image_path)
