from codeschool.api import router
from . import views

router.register(r'users', views.UserViewSet)
router.register(r'profile', views.ProfileViewSet)
