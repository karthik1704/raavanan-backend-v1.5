from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from orders.serializers import WAOrderDetailSerializer, WAOrderSerializer
from products.models import ProductVariant

# Create your views here.


class WAOrderCreateView(CreateAPIView):
    serializer_class = WAOrderSerializer
    model = serializer_class.Meta.model

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     quantity = serializer.validated_data.get("quantity")
    #     variant = serializer.validated_data.get("product_id")
    #     price = quantity * variant.price

    #     serializer.save(price=price)

    #     return super().perform_create(serializer)


class WAOrderRetrieveView(RetrieveAPIView):
    serializer_class = WAOrderDetailSerializer
    model = serializer_class.Meta.model
    lookup_field = "order_id"

    def get_queryset(self):
        return self.model.objects.all()
