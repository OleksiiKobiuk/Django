from rest_framework import serializers
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

from apps.user_profile.serializers import ProfileSerializer
from core.models import ProfileModel
from apps.car.serializers import CarSerializer
from core.manager import CustomUserManager

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True, read_only=True) # можна вивести всі авто, що належать юзеру,
    # read_only=True - при запису юзера авто не будемо записувати
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'profile', 'cars')
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
