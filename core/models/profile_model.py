from django.contrib.auth import get_user_model
from django.db import models

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
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')