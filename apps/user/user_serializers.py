from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # password = validated_data.pop('password')
        # model = UserModel(**validated_data)
        # model.set_password(password)
        # model.save()
        return UserModel.objects.create_user(**validated_data)
