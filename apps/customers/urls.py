from rest_framework.routers import DefaultRouter
from .views import CustomUserModelViewSet


router = DefaultRouter()

router.register('customers', CustomUserModelViewSet)

urlpatterns = router.urls