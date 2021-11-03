from django.urls import include, path

urlpatterns = [
    path('cars', include('apps.car.urls')),
    path('users/', include('apps.user.user_urls')),
    path('auth', include('apps.auth.urls')),
    path('autoclubs', include('apps.autoclub.urls')),
]
