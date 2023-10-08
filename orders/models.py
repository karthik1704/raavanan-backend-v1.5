from django.db import models

from products.models import ProductVariant


# Create your models here.
class WAOrder(models.Model):
    product_id = models.ForeignKey(
        ProductVariant, related_name="order_product", on_delete=models.DO_NOTHING
    )
    order_id = models.CharField(unique=True, max_length=255, editable=False)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=30)
    alternate_phone_number = models.CharField(max_length=30, blank=True, null=True)

    address = models.TextField()
    pincode = models.CharField(max_length=100)
    landmark = models.CharField(max_length=255, blank=True, null=True)

    extra = models.TextField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.order_id


class ExtraInformation(models.Model):
    waorder = models.ForeignKey(
        WAOrder, related_name="extra_info", on_delete=models.CASCADE
    )
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    image = models.ImageField(upload_to="order/", blank=True, null=True)
