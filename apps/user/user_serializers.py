from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import serializers

from apps.car.serializers import CarSerializer
from apps.user_profile.serializers import ProfileSerializer
from core.manager import CustomUserManager
from core.models import ProfileModel

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True, read_only=True) # можна вивести всі авто, що належать юзеру,
    # read_only=True - при запису юзера авто не будемо записувати
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'profile', 'cars', 'auto_clubs')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(user=user, **profile)
        # password = validated_data.pop('password')
        # model = UserModel(**validated_data)
        # model.set_password(password)
        # model.save()
        return user

class UserUpdateSerializer(UserSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'profile', 'cars', 'auto_clubs')

# визначаємо в методі як будуть оновлятися вкладеності юзера, напр. profile
    def update(self, instance, validated_data):
        profile=validated_data.pop('profile', None) # з validated_data забираємо profile
        if profile:
            ProfileSerializer().update(instance.profile, profile) # отримуємо екземпляр серіалайзеру профайла (ProfileSerializer())
            # update(instance.profile) - витягуємо спершу дані, що є в базі даних
            # другий параметр вказує, чим оновити instance (update(instance.profile, profile) - тим профайлом, що вже вище провалідувався
        return super().update(instance, validated_data)
        # super() - по суті є сам серіалайзер, а від нього обновляємо instance юзера з UcerModel
        # і передаємо validated_data
