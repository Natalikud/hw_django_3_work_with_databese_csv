from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    objects = None
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

