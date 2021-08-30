from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .user_serializers import UserSerializer
UserModel: User = get_user_model()

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

# виведення/видалення/оновлення юзера по id
class UserRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'
    queryset = UserModel.objects.all()