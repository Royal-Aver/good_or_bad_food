import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'good_or_bad_food.settings')

application = get_asgi_application()
