from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^field_test/', views.FieldViewSet, name='field_form')
]
