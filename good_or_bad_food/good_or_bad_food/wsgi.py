import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'good_or_bad_food.settings')

application = get_wsgi_application()
