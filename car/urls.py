from django.urls import path

from .views import home, add_car
urlpatterns = [
    path('', home),
    path('/create/<str:model>/<int:year>/', add_car)
]