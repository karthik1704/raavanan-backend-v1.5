from django.db import models


# Create your models here.
class BannerImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="banner/")
    image_webp = models.ImageField(upload_to="banner/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
