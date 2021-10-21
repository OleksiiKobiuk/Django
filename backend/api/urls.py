from django.conf.urls.static import static
from django.urls import path, include

from backend.config_project import settings

urlpatterns = [
    path('api/v1/', include('api.api_v1'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # вказуємо статичні папки, куди зберігатимуться файли.
# MEDIA_URL та MEDIA_ROOT треба прописати у файлі settings.py