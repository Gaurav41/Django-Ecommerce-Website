from django.contrib import admin

# Register your models here.
from .models import Product,User_messages

admin.site.register(Product)
admin.site.register(User_messages)