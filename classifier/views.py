from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from classifier.models import Image
from classifier.serializers import ImageSerializer


class ImageModelViewSet(ModelViewSet):
    queryset = Image.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer
