from django.db.models import Count, F, Max
from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from products.models import Product, ProductVariant, VariantSpecification
from products.serializers import (
    CategorySerializer,
    ProductDetailSerializer,
    ProductSerializer,
    ProductVariantListSerilizer,
    RequestExtraSerializer,
)

# Create your views here


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.all().order_by("created_at")


class CategoryDetailView(RetrieveAPIView):
    serializer_class = CategorySerializer
    model = serializer_class.Meta.model
    lookup_field = "slug"

    def get_queryset(self):
        return self.model.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        slug = self.kwargs["slug"]
        parents_with_variants = self.model.objects.annotate(
            variant_count=Count("variants")
        ).filter(variant_count__gt=0)
        return parents_with_variants.filter(publish=True, category__slug=slug)


# class ProductVariantListView(ListAPIView):
#     serializer_class = ProductVariantListSerilizer
#     model = serializer_class.Meta.model

#     def get_queryset(self):
#         slug = self.kwargs["slug"]
#         return self.model.objects.filter(
#             publish=True, product__category__slug=slug, product__publish=True
#         )


# class ProductVariantTrendingView(ListAPIView):
#     serializer_class = ProductVariantListSerilizer
#     model = serializer_class.Meta.model

#     def get_queryset(self):
#         return self.model.objects.filter(
#             publish=True,
#             product__publish=True,
#         ).order_by("-metrics__views")


# class ProductVariantNewView(ListAPIView):
#     serializer_class = ProductVariantListSerilizer
#     model = serializer_class.Meta.model

#     def get_queryset(self):
#         return self.model.objects.filter(publish=True, product__publish=True).order_by(
#             "-created_at"
#         )[:10]


class ProductVariantListView(ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        slug = self.kwargs["slug"]
        parents_with_variants = self.model.objects.annotate(
            variant_count=Count("variants")
        ).filter(variant_count__gt=0)

        return parents_with_variants.filter(
            publish=True,
            category__slug=slug,
        )


class ProductVariantTrendingView(ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        products = self.model.objects.annotate(
            max_view_count=Max("variants__metrics__views")
        )
        parents_with_variants = products.annotate(
            variant_count=Count("variants")
        ).filter(variant_count__gt=0)

        main_products = parents_with_variants.filter(
            variants__metrics__views=F("max_view_count")
        )

        return main_products


class ProductVariantNewView(ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        parents_with_variants = self.model.objects.annotate(
            variant_count=Count("variants")
        ).filter(variant_count__gt=0)
        return parents_with_variants.filter(publish=True).order_by("-created_at")[:10]


class ProductVariantPopularView(ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(publish=True)


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    model = serializer_class.Meta.model
    lookup_field = "variants__variant_id"

    def get_queryset(self):
        return self.model.objects.filter(publish=True)

    def get_object(self):
        child_id = self.kwargs.get("variants__variant_id")

        try:
            parent = self.model.objects.get(variants__variant_id=child_id)
            selected_child = parent.variants.get(variant_id=child_id)  # type: ignore
            parent.selected = selected_child  # type: ignore
            return parent
        except self.model.DoesNotExist:
            raise Http404

    def retrieve(self, request, *args, **kwargs):
        child_id = self.kwargs.get("variants__variant_id")

        instance = self.get_object()
        variant = instance.variants.get(variant_id=child_id)  # type: ignore
        variant.metrics.views += 1
        variant.metrics.save()
        return super().retrieve(request, *args, **kwargs)


class VariantDetailView(RetrieveAPIView):
    serializer_class = ProductVariantListSerilizer
    model = serializer_class.Meta.model
    lookup_field = "variant_id"

    def get_queryset(self):
        return self.model.objects.filter(publish=True, product__publish=True)


class RequestExtraRetrieveView(ListAPIView):
    serializer_class = RequestExtraSerializer
    model = serializer_class.Meta.model
    lookup_field = "vid"

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self):
        id = self.kwargs.get("vid")
        category = Product.objects.get(variants__variant_id=id).category
        print(category)
        try:
            extras = self.model.objects.filter(category=category)
            return extras
        except self.model.DoesNotExist:
            return Http404
