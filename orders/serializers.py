from rest_framework import serializers

from orders.models import ExtraInformation, WAOrder
from products.serializers import VariantDetailSerializer


class ExtraInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInformation
        exclude = ("waorder",)


class WAOrderSerializer(serializers.ModelSerializer):
    extra_info = ExtraInformationSerializer(many=True)

    class Meta:
        model = WAOrder
        exclude = ("price", "alternate_phone_number")

    def create(self, validated_data):
        extra_info = validated_data.pop("extra_info")
        quantity = validated_data.get("quantity")
        variant = validated_data.get("product_id")
        price = quantity * variant.price
        order = WAOrder.objects.create(price=price, **validated_data)
        for extra in extra_info:
            ExtraInformation.objects.create(waorder=order, **extra)
        return order


class WAOrderDetailSerializer(serializers.ModelSerializer):
    extra_info = ExtraInformationSerializer(many=True, read_only=True)
    product_id = VariantDetailSerializer(read_only=True)

    class Meta:
        model = WAOrder
        fields = "__all__"
