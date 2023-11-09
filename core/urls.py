
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from core import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manicure.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)