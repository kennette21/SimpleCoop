from django.contrib import admin

from .models import Product, Producer, Order

admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(Order)
