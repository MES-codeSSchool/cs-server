from rest_framework import viewsets

from . import serializers
from . import models

class FieldViewSet(viewsets.ModelViewSet):
    """
    List of Fields.
    """

    queryset = models.Field.objects.all()
    serializer_class = serializers.FieldSerializer
