from rest_framework.routers import DefaultRouter
from app.views.todoViews import TodoViewsSet

router = DefaultRouter()
router.register(r'', TodoViewsSet)

urlpatterns = router.urls
