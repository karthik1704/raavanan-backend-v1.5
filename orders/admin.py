from django.contrib import admin

from orders.models import WAOrder


# Register your models here.
class WAOrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "first_name", "last_name", "phone_number")


admin.site.register(WAOrder, WAOrderAdmin)
