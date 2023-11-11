from rest_framework.routers import DefaultRouter
from app.views.userViews import UserViewsSet

router = DefaultRouter()
router.register(r'', UserViewsSet)

urlpatterns = router.urls