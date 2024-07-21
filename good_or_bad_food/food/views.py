from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()

    return render(request, 'food/index.html', {'products': products})


def product_detail(request, product_slug):
    pass


def category_product(request, category_slug):
    pass
