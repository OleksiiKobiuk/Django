from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'car'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user може мати кілька авто (один до багатьох)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.brand


