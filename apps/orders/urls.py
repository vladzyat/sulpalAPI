from rest_framework.routers import DefaultRouter
from .views import OrdersModelViewSet

router = DefaultRouter()


router.register('orders', OrdersModelViewSet)


urlpatterns = router.urls