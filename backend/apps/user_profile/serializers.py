from rest_framework.serializers import ModelSerializer

from backend.core.models import ProfileModel


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'age', 'born', 'photo')
        extra_kwargs = {
            'photo': {'read_only': True}  # вказуємо фото лише для читання, щоб не вимагалося обов'язково при створенні профайлу
        }

class ProfilePhotoSerializer(ModelSerializer): # серіалайзер для фото
    class Meta:
        model = ProfileModel
        fields = ('photo',)
        extra_kwargs = {
            'photo': {'write_only': True}
        }

