from django.contrib import admin

from accounts.models import Customer, MyUser, Seller, Staff

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Staff)
