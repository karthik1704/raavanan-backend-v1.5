from django.urls import path

from products.views import CategoryListView, ProductListView

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("products/", ProductListView.as_view()),
]
