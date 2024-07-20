from django.db import models


class BaseModel(models.Model):
    slug = models.SlugField('URL', unique=True)
    description = models.TextField("Описание", blank=True, null=True)

    class Meta:
        abstract = True
