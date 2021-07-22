from django.urls import path
from .views import MyView, MyViewSecond
urlpatterns = [
    path('', MyView.as_view()),
    path('<int:id>/', MyViewSecond.as_view())
]