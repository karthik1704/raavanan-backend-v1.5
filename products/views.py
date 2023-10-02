from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from products.serializers import (
    CategorySerializer,
    ProductDetailSerializer,
    ProductSerializer,
    ProductVariantListSerilizer,
)

# Create your views here


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.all()


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
        return self.model.objects.filter(publish=True, category__slug=slug)


class ProductVariantListView(ListAPIView):
    serializer_class = ProductVariantListSerilizer
    model = serializer_class.Meta.model

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return self.model.objects.filter(
            publish=True, product__category__slug=slug, product__publish=True
        )


class ProductVariantTrendingView(ListAPIView):
    serializer_class = ProductVariantListSerilizer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(
            publish=True,
            product__publish=True,
        ).order_by("-metrics__views")


class ProductVariantNewView(ListAPIView):
    serializer_class = ProductVariantListSerilizer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(publish=True, product__publish=True).order_by(
            "-created_at"
        )[:10]


class ProductVariantPopularView(ListAPIView):
    serializer_class = ProductVariantListSerilizer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(publish=True, product__publish=True)


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
