from rest_framework.serializers import ModelSerializer

from core.models import ProfileModel

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'age', 'born')


