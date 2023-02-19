from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from animal_api.views import  LocationView, AnimalView


schema_view = get_swagger_view(title="API")
router = DefaultRouter()
router.register(r"locations", LocationView, basename="location")
router.register(r"animals", AnimalView, basename='animal')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("swagger/", schema_view),
    path("accounts/", include('djoser.urls')),
    
]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
