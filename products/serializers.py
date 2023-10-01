from rest_framework import serializers

from products.models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductVariant,
    ProductVariantImage,
    VariantSpecification,
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
    # product = ProductSerializer(read_only=True)
    title = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = "__all__"

    def get_title(self, obj):
        p_name = obj.product.product_name
        v_name = obj.variant_name if obj.variant_name else ""
        type = obj.type.name if obj.type else ""
        _name = f"{p_name} {v_name} {type}".rstrip()
        return _name

    def get_product_image(self, obj):
        request = self.context.get("request")
        product_image = (
            obj.product.image.url
            if obj.product.image
            else obj.product.product_images.all().first().image.url
            if obj.product.product_images.all().first()
            else None
        )
        return request.build_absolute_uri(product_image)  # type: ignore


class ProductVariantImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    original = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariantImage
        fields = "__all__"

    def get_thumbnail(self, obj):
        request = self.context.get("request")
        image = obj.image.url

        return request.build_absolute_uri(image)  # type: ignore

    def get_original(self, obj):
        request = self.context.get("request")
        image = obj.image.url

        return request.build_absolute_uri(image)  # type: ignore


class VariantSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantSpecification
        fields = "__all__"


class ProductVariantDetailSerializer(serializers.ModelSerializer):
    variant_images = ProductVariantImageSerializer(many=True, read_only=True)
    variant_spec = VariantSpecificationSerializer(many=True, read_only=True)
    title = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = "__all__"

    def get_title(self, obj):
        p_name = obj.product.product_name
        v_name = obj.variant_name if obj.variant_name else ""
        type = obj.type.name if obj.type else ""
        _name = f"{p_name} {v_name} {type}".rstrip()
        return _name


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)
    variants = ProductVariantDetailSerializer(many=True, read_only=True)
    selected = ProductVariantDetailSerializer(read_only=True)
    product_spec = ProductSpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
