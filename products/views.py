from django.shortcuts import render

from datetime import datetime

from products.fixtures.extract_data_script import extract_data
from products.models import ProductsCategory, Product


# Create your views here.
# Controller-functions


def index(request):
    context = {
        'page_title': 'geekshop',
        'today': datetime.now(),
    }
    return render(request, 'index.html', context)


def products(request, pk=None):
    show_db_categories = ProductsCategory.objects.all()
    show_db_products = Product.objects.all()
    context = {
        'page_title': 'geekshop - каталог',
        'today': datetime.now(),
        'products': extract_data('products/fixtures/db.json'),
        'category': extract_data('products/fixtures/category.json')
    }
    return render(request, 'products.html', context)
