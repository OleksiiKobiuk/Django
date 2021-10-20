from django.urls import path

from .views import AddCarByUserIdView, UploadPhotoToProfileView, UserListCreateView, UserRetrieveUpdateDelete

urlpatterns = [
    path('', UserListCreateView.as_view(), name = 'user_list_create'),
    # виведення/видалення/оновлення 1 юзера
    path('<int:user_id>', UserRetrieveUpdateDelete.as_view(), name = 'user_retrieve_update_delete'),
    path('<int:pk>/cars', AddCarByUserIdView.as_view(), name = 'car_list_create_by_user_id'),
    path('photo', UploadPhotoToProfileView.as_view(), name = 'user_add_photo')
]