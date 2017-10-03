from codeschool.api import router
from . import views

router.register('field_values', views.FieldValueViewSet)
