from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('products/<int:category_id>/', views.product_list, name='product_list_by_category'),
    path('products/', views.product_list, name='product_list'),
]
