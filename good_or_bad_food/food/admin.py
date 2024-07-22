from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product, Category, Price, Nutrient, Element, Type, Rating


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description', 'image', 'price', 'category', 'element', 'nutrient')
    list_display = (
        'title',
        'description',
        'nutrient',
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description')

    list_display = (
        'title',
        'description',
    )

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
    )


@admin.register(Nutrient)
class NutrientAdmin(admin.ModelAdmin):
    pass


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description', 'type', 'rating')

    list_display = (
        'title',
        'description',
        'rating'
    )

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description')

    list_display = (
        'title',
        'description',
    )

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'rating_num', 'description')

    list_display = (
        'title',
        'rating_num',
    )

    prepopulated_fields = {"slug": ("title",)}


admin.site.unregister(Group)
