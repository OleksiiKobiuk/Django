from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'
        app_label = 'core'

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    born = models.DateField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')