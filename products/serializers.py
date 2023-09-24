from rest_framework import serializers

from products.models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductVariant,
)


class CategoryChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = (
            "path",
            "depth",
            "numchild",
        )


class CategorySerializer(serializers.ModelSerializer):
    children = CategoryChildrenSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = (
            "path",
            "depth",
            "numchild",
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = "__all__"


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    product_spec = ProductSpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductVariantListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = "__all__"
