from django.db.models import F
from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Basket
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db import connection


@login_required
def baskets_add(request, pk):
    product = Product.objects.get(pk=pk)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        baskets = baskets.first()
        # baskets.quantity += 1
        baskets.quantity = F('quantity') + 1
        baskets.save()

        update_queries = list(filter(lambda x: 'UPDATE' in x['sql'], connection.queries))
        print(f'basket_add {update_queries} ')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    Basket.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(pk=pk)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/baskets.html', context)
        return JsonResponse({'result': result})
