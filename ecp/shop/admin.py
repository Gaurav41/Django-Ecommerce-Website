from django.contrib import admin

# Register your models here.
from .models import Product,User_messages,Order

admin.site.register(Product)
admin.site.register(User_messages)
admin.site.register(Order)