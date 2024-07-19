from django.db import models

from .constant_value import LENGTH_FIELD


class Product(models.Model):
    title = models.CharField("Продукт", max_length=LENGTH_FIELD, unique=True)
    slug = models.SlugField('URL', unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField(  # по этому полю вопрос, ведь мы хотим сравнивать цены за период
        "Цена", max_digits=7, decimal_places=2,
        default=0, blank=True, null=True)
    category = models.ManyToManyField("Категория", "Category")
    element = models.ManyToManyField("Элемент", "Element")
    nutrient = models.OneToOneField("КБЖУ", "Nutrients",
               on_delete=models.SET_NULL)


class Category(models.Model):
    title = models.CharField("Категория", max_length=LENGTH_FIELD, unique=True)
    slug = models.SlugField('URL', unique=True)
    description = models.TextField("Описание", blank=True, null=True)


    