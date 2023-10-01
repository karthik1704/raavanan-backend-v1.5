from django.urls import path

from products.views import (
    CategoryDetailView,
    CategoryListView,
    ProductDetailView,
    ProductListView,
    ProductVariantListView,
)

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("category/<str:slug>/", CategoryDetailView.as_view()),
    path("products/<str:slug>/", ProductListView.as_view()),
    path("products/variants/<str:slug>/", ProductVariantListView.as_view()),
    path("products/detail/<str:variants__variant_id>/", ProductDetailView.as_view()),
]
