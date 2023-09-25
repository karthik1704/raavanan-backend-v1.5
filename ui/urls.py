from django.urls import path

from ui.views import BannerImageListView

urlpatterns = [
    path("banner/", BannerImageListView.as_view()),
]
