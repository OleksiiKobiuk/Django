from django.urls import path
from .views import CarCreateListView, RetriaveUpdDeleteView
# from .views import MyView, MyViewSecond
urlpatterns = [
    path('', CarCreateListView.as_view(), name = 'car_list_create'), # name = 'car_list_create' потрібно для формування
    # автоматичної документації
    path('<int:id>', RetriaveUpdDeleteView.as_view(), name ='car_retriave_delete'),  #pk - primery key, пишеться замість id

]