from django.urls import path, include
from rest_framework.routers import DefaultRouter

from classifier.views import ImageModelViewSet

app_name = 'images-api'
router = DefaultRouter()
router.register('images', ImageModelViewSet)
urlpatterns = [
    path('', include(router.urls))
]
