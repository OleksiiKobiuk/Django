from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .user_serializers import UserSerializer, UserUpdateSerializer
from apps.car.serializers import CarByUserIdSerializer

UserModel: User = get_user_model()

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

# виведення/видалення/оновлення юзера по id
class UserRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializer
    lookup_url_kwarg = 'user_id'
    queryset = UserModel.objects.all()

# створення авто по id юзера
class AddCarByUserIdView(CreateAPIView):
    serializer_class = CarByUserIdSerializer
    queryset = UserModel # передаємо дану моделі в кверісет, а потім по кверісету даний клас шукатиме юзера

    # метод для збереження id юзера перед створенням авто
    def perform_create(self, serializer):
        serializer.save(user=self.get_object())
