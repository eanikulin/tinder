import os
from django.core.mail import send_mail
from PIL import Image
from django.conf import settings

path_watermark = os.path.join(settings.BASE_DIR, "media" + '\watermark.png')


def watermark_photo(input_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(path_watermark)
    base_image.paste(watermark, (0, 0))
    base_image.save(input_image_path)


def send_message(initiator, recipient):
    send_mail('Сообщение', f'Вы понравились: {recipient.last_name} {recipient.first_name}!,'
                           f' почта участника: {recipient.email}', 'mail@mail.com', [initiator.email])
