import os

# функція для зміни імені фотографій, які завантажує юзер,
# та завантаження їх у папку під назвою пошти юзера
import uuid


def upload_to(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid1()}.{ext}'
    return os.path.join(instance.user.email, new_filename)