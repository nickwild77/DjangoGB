from django.contrib import admin
from django.urls import path

app_name = 'baskets'

from baskets.views import baskets_add, basket_remove

urlpatterns = [
    path('baskets_add/<int:id>', baskets_add, name='baskets_add'),
    path('delete/<int:id>', basket_remove, name='basket_remove'),
]
