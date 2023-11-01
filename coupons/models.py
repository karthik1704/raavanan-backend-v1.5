from django.db import models
from django.utils import timezone


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True)
    discount_type = models.CharField(
        max_length=10,
        choices=[
            ("percentage", "Percentage"),
            ("fixed_amount", "Fixed Amount"),
        ],
    )
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    max_discount_amount = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    max_usage_count = models.PositiveIntegerField(default=1)
    current_usage_count = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField("Product")

    def __str__(self):
        return self.code

    def is_valid(self):
        now = timezone.now()
        return (
            self.active
            and self.start_date <= now <= self.end_date
            and self.current_usage_count < self.max_usage_count
        )

    def calculate_discount(self, cart_total, cart_items):
        if not self.is_valid():
            return 0

        applicable_items = cart_items.filter(product__in=self.products)
        total_price = sum(
            item.product.price * item.quantity for item in applicable_items
        )
        discount_amount = 0
        if self.discount_type == "percentage":
            if self.max_discount_amount:
                discount_amount = min(
                    total_price * (self.discount_value / 100), self.max_discount_amount
                )
        elif self.discount_type == "fixed_amount":
            if self.max_discount_amount:
                discount_amount = min(self.discount_value, self.max_discount_amount)

        return discount_amount
