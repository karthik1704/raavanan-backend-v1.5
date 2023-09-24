from django.shortcuts import render
from rest_framework.generics import ListAPIView

from products.serializers import CategorySerializer, ProductSerializer

# Create your views here


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(publish=True)
