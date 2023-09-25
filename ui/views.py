from django.shortcuts import render
from rest_framework import generics

from ui.serializers import BannerImageSerializer

# Create your views here.


class BannerImageListView(generics.ListAPIView):
    serializer_class = BannerImageSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.all()
