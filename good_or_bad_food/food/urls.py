"""Food application urls."""

from django.urls import path

from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'category/<slug:category_slug>/',
        views.category_product,
        name='category_product'),
    path(
        'product/<int:product_id>',
        views.product_detail,
        name='product_detail'),
]
