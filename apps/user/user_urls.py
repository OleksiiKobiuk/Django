from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateDelete
from apps.car.views import CarCreateListView

urlpatterns = [
    path('', UserListCreateView.as_view(), name = 'user_list_create'),
    # виведення/видалення/оновлення 1 юзера
    path('/<int:user_id>', UserRetrieveUpdateDelete.as_view(), name = 'retrieve_user'),
    # path('/cars', CarCreateListView.as_view(), name = 'car_list_create_by_user_id'')
]