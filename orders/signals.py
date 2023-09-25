from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from orders.models import WAOrder


@receiver(post_save, sender=WAOrder)
def add_order_id(sender, instance, created, **kwargs):
    if created:
        year = instance.created_at.strftime("%Y")
        month = instance.created_at.strftime("%m")
        id = str(instance.id)
        order_id = f"RAO{year}{month}{id}"
        instance.order_id = order_id
        instance.save()
