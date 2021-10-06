from django.conf.urls.static import static
from django.urls import path, include

from config_project import settings

urlpatterns = [
    path('cars', include('apps.car.urls')),
    path('users', include('apps.user.user_urls')),
    path('auth', include('apps.auth.urls'))
]
