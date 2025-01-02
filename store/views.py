from django.shortcuts import render
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def product_list(request, category_id=None):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})
