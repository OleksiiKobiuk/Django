from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CarModel(models.Model):
    class Meta:
        db_table = 'cars' # перевизначаємо ім'я таблиці,
        # інакше буде формуватися автоматично: ім'я додатку_ім'я класу моделі
        verbose_name = 'car' #Удобочитаемое имя для объекта, единственное число

    BRAND_NAME = (
        ('N', 'Nissan'),
        ('B', 'BMW'),
        ('A', 'Audi'),
        ('F', 'Ford'),
    )
    brand_name = models.CharField(max_length=1, choices=BRAND_NAME, default='N') # choices - последовательность (sequence) из 2-х значных кортежей
    # для использования в качестве выбора для этого поля
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user може мати кілька авто (один до багатьох)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.brand


