from django.urls import path

from products.views import CategoryDetailView, CategoryListView, ProductListView

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("category/<str:slug>/", CategoryDetailView.as_view()),
    path("products/<str:slug>/", ProductListView.as_view()),
]
