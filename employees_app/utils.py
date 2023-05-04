import os
import random
import string


def namegen():
    symbols = string.ascii_uppercase + string.ascii_lowercase +  string.digits
    rand_name = ''.join(random.sample(symbols, 10))
    return rand_name


def resize_image(image):
    if image.height > 200 or image.width > 200:
        output_size = (200, 200)
        image.thumbnail(output_size)
    return image

def upload_to(instance, filename):
    new_filename = namegen()
    ext = filename.split('.')[-1]
    filename = f'{new_filename}.{ext}'
    return os.path.join('images/', filename)