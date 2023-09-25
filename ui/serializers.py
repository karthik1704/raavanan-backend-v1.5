from rest_framework import serializers

from ui.models import BannerImage


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = "__all__"
