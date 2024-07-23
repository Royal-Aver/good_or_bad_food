from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .constant_value import LENGTH_FIELD
from core.models import BaseModel


class Product(BaseModel):
    title = models.CharField(
        "Название продукта",
        max_length=LENGTH_FIELD,
        unique=True)
    image = models.ImageField(
        "Изображение",
        upload_to='product_images/',
        blank=True,
        null=True)
    price = models.OneToOneField(
        "Price",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Цена продукта, ₽")
    category = models.ManyToManyField(
        "Category",
        verbose_name="Категория")
    element = models.ManyToManyField(
        "Element",
        verbose_name="Элемент")
    nutrient = models.OneToOneField(
        "Nutrient",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="КБЖУ",
        related_name="product")

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.title


class Price(models.Model):
    title = models.DecimalField(
        "Цена",
        max_digits=7,
        decimal_places=2,
        default=0,
        blank=True,
        null=True)
    date = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "цену"
        verbose_name_plural = "цены"

    def __str__(self):
        return str(self.title)


class Category(BaseModel):
    title = models.CharField(
        "Название категории",
        max_length=LENGTH_FIELD,
        unique=True)

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.title


class Nutrient(models.Model):
    calories = models.IntegerField(
        "Калории",
        default=0,
        blank=True,
        null=True)
    proteins = models.IntegerField(
        "Белки",
        default=0,
        blank=True,
        null=True)
    fats = models.IntegerField(
        "Жиры",
        default=0,
        blank=True,
        null=True)
    carbohydrates = models.IntegerField(
        "Углеводы",
        default=0,
        blank=True,
        null=True)

    class Meta:
        verbose_name = "КБЖУ"
        verbose_name_plural = "КБЖУ"

    def __str__(self):
        return f"Калории: {str(self.calories)}, Белки: {str(self.proteins)}, Жиры: {str(self.fats)}, Углеводы: {str(self.carbohydrates)} | {str(self.product.title)}"


class Element(BaseModel):
    title = models.CharField(
        "Название элемента",
        max_length=LENGTH_FIELD,
        unique=True)
    type = models.ManyToManyField(
        "Type",
        verbose_name="Тип элемента")
    rating = models.ForeignKey(
        "Rating",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Рейтинг")

    class Meta:
        verbose_name = "элемент"
        verbose_name_plural = "элементы"

    def __str__(self):
        return self.title


class Type(BaseModel):
    title = models.CharField(
        "Название типа элемента",
        max_length=LENGTH_FIELD,
        unique=True)

    class Meta:
        verbose_name = "тип элемента"
        verbose_name_plural = "типы элементов"

    def __str__(self):
        return self.title


class Rating(BaseModel):
    title = models.CharField(
        "Название",
        max_length=LENGTH_FIELD,
        unique=True)
    rating_num = models.IntegerField("Рейтинг", validators=[
            MinValueValidator(1),
            MaxValueValidator(5)],
            default=0,
            help_text='Укажите рейтинг элемента от 1 до 5')

    class Meta:
        verbose_name = "рейтинг элемента"
        verbose_name_plural = "рейтинг элементов"

    def __str__(self):
        return self.title
