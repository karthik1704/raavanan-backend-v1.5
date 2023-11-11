from typing import Any

from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from products.models import (
    Category,
    Material,
    Product,
    ProductImage,
    ProductSpecification,
    ProductVariant,
    ProductVariantImage,
    RequestExtra,
    VariantSpecification,
    VariantTypes,
)

# Register your models here.


class VariantTypeInline(admin.TabularInline):
    model = VariantTypes
    extra = 0


class RequestExtraInline(admin.StackedInline):
    model = RequestExtra
    extra = 0


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    inlines = (VariantTypeInline, RequestExtraInline)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fk_name = "product"


class ProductVariantImageInline(admin.StackedInline):
    model = ProductVariantImage
    extra = 1
    fk_name = "variant"


class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 0
    inlines = (ProductVariantImageInline,)
    # readonly_fields = ("discount", "price")


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1
    fk_name = "product"


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline, ProductSpecificationInline, ProductVariantInline)
    search_fields = (
        "product_id",
        "product_name",
    )

    # def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None:
    #     super().save_related(request, form, formsets, change)
    #     # Calculate discount amounts for each variant
    #     for variant in form.instance.variants.all():
    #         variant.price = variant.mrp - (
    #             variant.mrp * variant.discount_percentage / 100
    #         )
    #         variant.discount = variant.mrp - variant.price
    #         variant.save()


class VariantSpecInline(admin.TabularInline):
    model = VariantSpecification
    extra = 0
    fk_name = "variant"


class VariantAdmin(admin.ModelAdmin):
    inlines = (ProductVariantImageInline, VariantSpecInline)
    autocomplete_fields = ("product",)
    # readonly_fields = ("discount", "price")

    # def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
    #     obj.price = obj.mrp - (obj.mrp * obj.discount_percentage / 100)
    #     obj.discount = obj.mrp - obj.price

    #     obj.save()
    #     return super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, VariantAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Material)
