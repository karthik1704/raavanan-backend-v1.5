from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from products.models import Product, ProductVariant


@receiver(post_save, sender=Product)
def add_product_id(sender, instance, created, **kwargs):
    if created:
        year = instance.created_at.strftime("%Y")
        month = instance.created_at.strftime("%m")
        id = str(instance.id)
        product_id = f"RA{year}{month}{id}"
        instance.product_id = product_id
        instance.save()


@receiver(post_save, sender=ProductVariant)
def add_variant_id(sender, instance, created, **kwargs):
    if created:
        year = timezone.now().strftime("%Y")
        month = timezone.now().strftime("%m")
        id = str(instance.id)
        variant_id = f"RA{year}{month}{id}"
        instance.variant_id = variant_id
        instance.save()
