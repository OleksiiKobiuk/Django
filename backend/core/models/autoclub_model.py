from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class AutoClubModel(models.Model):
    class Meta:
        db_table = 'auto_club'
        app_label = 'core' #Если модель определена вне приложения INSTALLED_APPS,
        # она должна объявить, какому приложению она принадлежит
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    users = models.ManyToManyField(UserModel, related_name='auto_clubs', db_table='users_autoclubs')
