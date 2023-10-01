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
    extra = 1
    inlines = (ProductVariantImageInline,)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1
    fk_name = "product"


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline, ProductSpecificationInline, ProductVariantInline)


class VariantSpecInline(admin.TabularInline):
    model = VariantSpecification
    extra = 0
    fk_name = "variant"


class VariantAdmin(admin.ModelAdmin):
    inlines = (ProductVariantImageInline, VariantSpecInline)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, VariantAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Material)
