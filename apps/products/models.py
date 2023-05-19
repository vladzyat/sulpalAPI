from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..customers.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  blank=True, null=True)

    @property
    def get_rating(self):
        stars = self.stars.all()
        if not stars:
            return 0
        count_stars = len(stars)
        sum_stars = sum(i.rating for i in stars)
        return sum_stars / count_stars