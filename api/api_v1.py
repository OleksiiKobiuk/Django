from django.conf.urls.static import static
from django.urls import include, path

from config_project import settings

urlpatterns = [
    path('cars', include('apps.car.urls')),
    path('users', include('apps.user.user_urls')),
    path('auth', include('apps.auth.urls')),
    path('autoclubs', include('apps.autoclub.urls')),
]
