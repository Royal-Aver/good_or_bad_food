"""Application definition for food."""
from django.apps import AppConfig


class FoodConfig(AppConfig):
    """Application definition for food."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food'
    verbose_name = 'Продукты питания'
