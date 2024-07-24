from django.shortcuts import render, get_object_or_404

from .models import Product, Category
from .constant_value import NUMS_OF_POSTS_MAIN


def index(request):
    for i in range(1, 4):
        categories = get_object_or_404(Category, id=i)
        products = categories.product_set.all()[1:4]

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'food/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.prefetch_related(
            'category',
            'element',
            'nutrient'
    ).get(pk=product_id)


    related_categories = product.category.all()
    categories = [category.title for category in related_categories]


    related_elements = product.element.all()
    elements = {element.title: element.rating.rating_num for element in related_elements}


    sum_ratings = 0

    for value in elements.values():
        sum_ratings += int(value)
    avg_rating_product = sum_ratings / len(elements)

    context = {
        'product': product,
        'categories': categories,
        'elements': elements,
        'rating': avg_rating_product
    }

    return render(request, 'food/product.html', context)


def category_product(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug
    )
    product_list = Product.objects.values(
        'id',
        'title',
        'price',
        'description'
    )

    # product_list = Product.objects.all()

    return render(
        request,
        'food/product_list.html',
        {'category': category, 'product_list': product_list})
