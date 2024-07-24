from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product, Category, Price, Nutrient, Element, Type, Rating


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'description',
        'image',
        'price',
        'category',
        'element',
        'nutrient'
    )

    list_display = (
        'title',
        'price',
        'get_categories',
        'get_elements',
    )

    def get_categories(self, obj):
        related_categories = obj.category.all()
        categories = [category.title for category in related_categories]
        return ", ".join(categories)

    get_categories.short_description = 'Категории'

    def get_elements(self, obj):
        related_elements = obj.element.all()
        elements = [element.title for element in related_elements]
        return ", ".join(elements)

    get_elements.short_description = 'Элементы'

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description')

    list_display = (
        'title',
        'description',
        'get_products'
    )

    def get_products(self, obj):
        related_products = obj.product_set.all()
        products = [product.title for product in related_products]
        return ", ".join(products)

    get_products.short_description = 'Продукты'

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'product'
    )


@admin.register(Nutrient)
class NutrientAdmin(admin.ModelAdmin):
    pass


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description', 'type', 'rating')

    list_display = (
        'title',
        'rating',
        'get_types',
    )

    def get_types(self, obj):
        related_types = obj.type.all()
        types = [type.title for type in related_types]
        return ", ".join(types)

    get_types.short_description = 'Типы'

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
    fields = ('title', 'slug', 'rating_num')

    list_display = (
        'title',
        'rating_num',
    )

    prepopulated_fields = {"slug": ("title",)}


admin.site.unregister(Group)
