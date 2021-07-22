from django.db import models

# Create your models here.

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'car'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.brand


