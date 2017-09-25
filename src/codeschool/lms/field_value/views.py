from rest_framework import viewsets

from . import serializers
from . import models

class FieldValueViewSet(viewsets.ModelViewSet):
    """
    List of Field Values
    """

    queryset = models.FieldValue.objects.all()
    serializer_class = serializers.FieldValueSerializer
