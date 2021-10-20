from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import (  # AllowAny - дозвіл доступу для всіх і можна буде створити нового користувача,
    AllowAny,
    IsAdminUser,
)

from apps.car.serializers import CarByUserIdSerializer

from ..user_profile.serializers import ProfilePhotoSerializer
from .user_serializers import UserSerializer, UserUpdateSerializer

# коли вже встановлений JWT. IsAdminUser дозволяє визначені дії лише адмінам (в БД is_staff = 1)


UserModel: User = get_user_model()

class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,) # дозвіл буде діяти на всі запити (і get, і post);
    # обов'язково має бути кортеж з комою
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

# виведення/видалення/оновлення юзера по id
class UserRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializer
    lookup_url_kwarg = 'user_id'
    queryset = UserModel.objects.all()

# створення авто по id юзера
class AddCarByUserIdView(CreateAPIView):
    permission_classes = (IsAdminUser,) # дозвіл тільки адміну створювати авто
    serializer_class = CarByUserIdSerializer
    queryset = UserModel # передаємо дану моделі в кверісет, а потім по кверісету даний клас шукатиме юзера

    # метод для збереження id юзера перед створенням авто
    def perform_create(self, serializer):
        serializer.save(user=self.get_object())

class UploadPhotoToProfileView(UpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    http_method_names = ('put',)   # вказує, що можна використовувати метод put

    def get_object(self):
        return self.request.user.profile # отрмуємо з юзера об'єкт - профайл