from codeschool.api import router
from . import views

router.register('fields', views.FieldViewSet)
router.register('field_values', views.FieldValueViewSet)
