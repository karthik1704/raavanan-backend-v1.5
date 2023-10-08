from django.urls import path

from orders.views import WAOrderCreateView, WAOrderRetrieveView

urlpatterns = [
    path("waorder/", WAOrderCreateView.as_view(), name="WA order create"),
    path(
        "waorder/<str:order_id>/",
        WAOrderRetrieveView.as_view(),
        name="WA order retrieve",
    ),
]
