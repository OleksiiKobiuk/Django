from django.urls import path

from .views import calculation

urlpatterns = [
    path('/<int:num1>/<str:sign>/<int:num2>/', calculation)
]