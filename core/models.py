from django.contrib import admin
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from uuid import uuid4

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    last_update = models.DateTimeField(auto_now=True)
    # collection = models.ForeignKey(
    #     Collection, on_delete=models.PROTECT, related_name='products')
    # promotions = models.ManyToManyField(Promotion, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']