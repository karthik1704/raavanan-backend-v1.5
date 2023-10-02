from collections.abc import Iterable

from django.db import models
from django.utils.text import slugify
from treebeard.mp_tree import MP_Node

# Create your models here.


class Category(MP_Node):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    imageurl = models.ImageField(upload_to=f"categories/", blank=True, null=True)

    decription = models.TextField(blank=True, default="")
    keywords = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    node_order_by = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "categories"


class VariantTypes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


FIELD_TYPES = (
    ("TEXT", "Text"),
    ("IMAGE", "Image"),
    ("RADIO", "Radio"),
    ("SELECT", "Select"),
)


class RequestExtra(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    request = models.CharField(max_length=255)
    option = models.CharField(max_length=255, blank=True, null=True)
    field_type = models.CharField(choices=FIELD_TYPES, default="TEXT")


class Material(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class GST(models.Model):
    pass


class Product(models.Model):
    product_id = models.CharField(unique=True, max_length=255, editable=False)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    brand = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    publish = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class ProductSpecification(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_spec", on_delete=models.CASCADE
    )
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.key}: {self.value}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/", null=True, blank=True)


# Product Variant


class ProductVariant(models.Model):
    variant_id = models.CharField(unique=True, max_length=255, editable=False)
    product = models.ForeignKey(
        Product,
        related_name="variants",
        on_delete=models.CASCADE,
    )
    type = models.ForeignKey(
        VariantTypes, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    variant_name = models.CharField(max_length=255, blank=True, null=True)

    image = models.ImageField(upload_to="products/", null=True, blank=True)

    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    publish = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.variant_id


# Product Variant Images
class ProductVariantImage(models.Model):
    variant = models.ForeignKey(
        ProductVariant, related_name="variant_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/", null=True, blank=True)


class VariantSpecification(models.Model):
    variant = models.ForeignKey(
        ProductVariant, related_name="variant_spec", on_delete=models.CASCADE
    )
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.key}: {self.value}"


class Metric(models.Model):
    variant = models.OneToOneField(
        ProductVariant, related_name="metrics", on_delete=models.CASCADE
    )
    views = models.PositiveBigIntegerField(default=0)
    buy_count = models.PositiveBigIntegerField(default=0)
