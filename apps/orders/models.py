from django.db import models

from ..customers.models import CustomUser
from ..products.models import Product


class Orders(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)