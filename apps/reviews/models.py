from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


from apps.customers.models import CustomUser
from apps.products.models import Product


class Comment(models.Model):
    text = models.CharField(max_length=150, blank=True, null=True)
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)


class Stars(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stars', blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)