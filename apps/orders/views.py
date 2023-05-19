from rest_framework.viewsets import ModelViewSet
from .models import Orders
from .serializers import OrdersSerializer


class OrdersModelViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
