from rest_framework.routers import DefaultRouter
from .views import VerificationEmailModelViewSet, CodeVerificationModelViewSet

router = DefaultRouter()


router.register('send_code', VerificationEmailModelViewSet)
router.register('verify_code', CodeVerificationModelViewSet)


urlpatterns = router.urls