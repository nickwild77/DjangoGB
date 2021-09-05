from django.contrib import admin

from .models import ProductsCategory, Product

admin.site.register(ProductsCategory)
admin.site.register(Product)