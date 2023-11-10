from app.views import TodoViewsSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewsSet)
urlpatterns = router.urls

