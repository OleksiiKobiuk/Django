from django.db import models

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'car'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand


