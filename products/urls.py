from django.urls import path

from products.views import (
    CategoryDetailView,
    CategoryListView,
    ProductDetailView,
    ProductListView,
    ProductVariantListView,
    ProductVariantNewView,
    ProductVariantPopularView,
    ProductVariantTrendingView,
)

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("category/<str:slug>/", CategoryDetailView.as_view()),
    path("products/new/", ProductVariantNewView.as_view()),
    path("products/popular/", ProductVariantPopularView.as_view()),
    path("products/trending/", ProductVariantTrendingView.as_view()),
    path("products/<str:slug>/", ProductListView.as_view()),
    path("products/variants/<str:slug>/", ProductVariantListView.as_view()),
    path("products/detail/<str:variants__variant_id>/", ProductDetailView.as_view()),
]
