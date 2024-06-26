from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from site_meta.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)