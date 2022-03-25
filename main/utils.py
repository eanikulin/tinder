import os
from django.core.mail import send_mail
from PIL import Image
from django.conf import settings
from math import asin, sqrt, sin, cos, radians

path_watermark = os.path.join(settings.BASE_DIR, "media" + '\watermark.png')


def watermark_photo(input_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(path_watermark)
    base_image.paste(watermark, (0, 0))
    base_image.save(input_image_path)


def send_message(initiator, recipient):
    send_mail('Сообщение', f'Вы понравились: {recipient.last_name} {recipient.first_name}!,'
                           f' почта участника: {recipient.email}', 'mail@mail.com', [initiator.email])


def distance_users(longitude_1, latitude_1, longitude_2, latitude_2):
    longitude_1, latitude_1, longitude_2, latitude_2 = map(radians, [longitude_1, latitude_1, longitude_2, latitude_2])
    deltalon = longitude_2 - longitude_1
    deltalat = latitude_2 - latitude_1
    kilometres = (2 * asin(sqrt(sin(deltalat / 2) ** 2 + cos(latitude_1) * cos(latitude_2) * sin(deltalon / 2) ** 2))) * 6371
    return round(kilometres, 3)

