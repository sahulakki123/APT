from rest_framework import routers 
from app.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'Student', AccountViewSet)
urlpatterns = router.urls