from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .constant_value import LENGTH_FIELD
from core.models import BaseModel


class Product(BaseModel):
    title = models.CharField("Продукт", max_length=LENGTH_FIELD, unique=True)
    price = models.DecimalField(  # по этому полю вопрос, ведь мы хотим сравнивать цены за период
        "Цена", max_digits=7, decimal_places=2,
        default=0, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to='product/', blank=True, null=True)
    category = models.ManyToManyField("Category", verbose_name="Категория")
    element = models.ManyToManyField("Element", verbose_name="Элемент")
    nutrient = models.OneToOneField("Nutrient", on_delete=models.SET_NULL, null=True, verbose_name="КБЖУ")  # ???


class Category(BaseModel):
    title = models.CharField("Категория", max_length=LENGTH_FIELD, unique=True)


class Nutrient(models.Model):
    calories = models.IntegerField("Калории", default=0, blank=True, null=True)
    proteins = models.IntegerField("Белки", default=0, blank=True, null=True)
    fats = models.IntegerField("Жиры", default=0, blank=True, null=True)
    carbohydrates = models.IntegerField("Углеводы", default=0, blank=True, null=True)


class Element(BaseModel):
    title = models.CharField("Элемент", max_length=LENGTH_FIELD, unique=True)
    type = models.ManyToManyField("Type", verbose_name="Тип элемента")
    rating = models.OneToOneField("Rating", on_delete=models.SET_NULL, null=True, verbose_name="Рейтинг")  # ???


class Type(BaseModel):
    title = models.CharField("Тип элемента", max_length=LENGTH_FIELD, unique=True)


class Rating(BaseModel):
    title = models.CharField("Рейтинг", max_length=LENGTH_FIELD, unique=True)
    rating_num = models.IntegerField("Рейтинг", validators=[
            MinValueValidator(0),
            MaxValueValidator(100)],  # нужно определиться со значениями
            default=0,
            help_text='Укажите рейтинг элемента от 0 до 100')
