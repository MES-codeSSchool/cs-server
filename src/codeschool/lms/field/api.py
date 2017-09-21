from codeschool.api import router
from . import views

router.register('fields', views.FieldViewSet)
