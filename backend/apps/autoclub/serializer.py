from rest_framework.serializers import ModelSerializer

from apps.user.user_serializers import UserUpdateSerializer
from core.models.autoclub_model import AutoClubModel


# додавання юзерів в автоклуб
class AutoClubAddUsersSerializer (ModelSerializer):
    class Meta:
        model = AutoClubModel
        fields = '__all__'

    def to_representation(self, instance):   # перевизначення виведення даних, щоб виводилася і вся інфа про юзерів, а не тільки їх id
        representation = super().to_representation(instance)
        representation['users'] = UserUpdateSerializer(instance.users, many=True).data
        return representation