from rest_framework import routers

from TIS_app.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
