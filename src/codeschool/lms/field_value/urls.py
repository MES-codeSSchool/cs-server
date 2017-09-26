from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.list_of_field_values, name='list'),
    url(r'^field_value/$', FieldValueViewSet.as_view(),
        name='field_value'),
]
