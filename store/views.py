from django.shortcuts import render
from .models import Category, Product


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html')

