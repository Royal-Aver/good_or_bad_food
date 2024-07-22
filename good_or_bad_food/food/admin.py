from django.contrib import admin

from .models import Product, Category, Nutrient, Element, Type, Rating

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Nutrient)
admin.site.register(Element)
admin.site.register(Type)
admin.site.register(Rating)
