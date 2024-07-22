from django import forms

from .models import Product


class FoodForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #  возможно нужны будут виджеты