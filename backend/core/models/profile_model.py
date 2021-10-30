from django.contrib.auth import get_user_model
from django.db import models

from core.services.upload_photo import upload_to

UserModel = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile' # перевизначаємо ім'я таблиці,
        # інакше буде формуватися автоматично: ім'я додатку_ім'я класу моделі
        app_label = 'core' #Если модель определена вне приложения INSTALLED_APPS,
        # она должна объявить, какому приложению она принадлежит

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    born = models.DateField()
    photo = models.ImageField(upload_to=upload_to) # upload_to= вказує, в якій папці будуть зберігатися картинки. Передаємо функцію upload_to
    # photo = models.ImageField(upload_to='images') # upload_to= вказує, в якій папці будуть зберігатися картинки
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')