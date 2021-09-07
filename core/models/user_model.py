from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# import datetime  #Для визначення лише дати нижче в полях created_at & updated_at
from core.manager import CustomUserManager

# class CustomUser(AbstractUser):
#     class Meta:
#         db_table = 'auth_user'
#         app_label = 'core'
#     username = None
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user' # перевизначаємо ім'я таблиці,
        # інакше буде формуватися автоматично: ім'я додатку_ім'я класу моделі
        app_label = 'core' #Если модель определена вне приложения INSTALLED_APPS,
        # она должна объявить, какому приложению она принадлежит

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Визначаємо лише дату
    # created_at = models.DateField(default=datetime.date.today)
    # updated_at = models.DateField(default=datetime.date.today)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
