from rest_framework import serializers
from .models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('customer_id',
                  'product_id',
                  'quantity',
                  'datetime',
                  'status')
