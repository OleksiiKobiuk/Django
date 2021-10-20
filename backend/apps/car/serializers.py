import datetime

from django.core.validators import RegexValidator

from rest_framework import serializers

from backend.core.models import CarModel

# serializer переводить в JSON і назад

class CarSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(min_value=1900, max_value=datetime.date.today().year)
    brand = serializers.CharField(validators=[
        RegexValidator('^[a-zA-Z]{2,20}$', 'only alpha min 2ch max 20ch')
    ])
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year', 'user', 'brand_name')
        extra_kwargs = {
            'user': {"write_only": True}
        }
        # fields = '__all__'  # отримуємо всі поля
        # exclude = ('user', ) # виводить всі поля, крім user

    # def validate_year(self, year):
    #     if year % 2 == 0:
    #         raise serializers.ValidationError('only odd years')
    #     return year

    # def validate(self, attrs):   #приходять через attrs повністю всі дані для валідації
    #     print(attrs)
    #     return attrs

class CarByUserIdSerializer(CarSerializer): #серіалайзер для створення авто по айді юзера
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year', 'brand_name')

