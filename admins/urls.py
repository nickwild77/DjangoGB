from django.contrib import admin
from django.urls import path

app_name = 'admins'

from .views import IndexView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryListView, \
    CategoryUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('categories/', CategoryListView.as_view(), name='admin_categories'),
    path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('user-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('category-update/<int:pk>', CategoryUpdateView.as_view(), name='admin_categories_update'),

]
