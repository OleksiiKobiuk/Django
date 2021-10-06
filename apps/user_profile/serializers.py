from rest_framework.serializers import ModelSerializer

from core.models import ProfileModel

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'age', 'born', 'photo')

class ProfilePhotoSerializer(ModelSerializer): # серіалайзер для фото
    class Meta:
        model = ProfileModel
        fields = ('photo',)
        extra_kwargs = {
            'photo': {'write_only': True}
        }

