from rest_framework.serializers import ModelSerializer

from car.models import CarModel

# serializer переводить в JSON і назад

class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'  # отримуємо всі поля
