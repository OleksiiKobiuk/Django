from django.urls import path

from .views import AddUsersView

urlpatterns = [
    path('<int:pk>', AddUsersView.as_view(), name = 'Add users to autoclub')
]