from django.contrib import admin
from .model.product import Product
from .model.categories import Categories
from .model.register import Register
from .model.orders import Order


# Register your models here.
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Register)
admin.site.register(Order)
