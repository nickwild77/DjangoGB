from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os
import json

from products.models import Product, ProductsCategory

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Каталог',
               'products': Product.objects.all(),
               'category': ProductsCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
