from rest_framework.routers import DefaultRouter
from .views import CommentModelViewSet, StarsModelViewSet

router = DefaultRouter()


router.register('comments', CommentModelViewSet)
router.register('rating', StarsModelViewSet)


urlpatterns = router.urls