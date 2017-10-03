from rest_framework import viewsets

from . import serializers
from .models import FieldValue

class FieldValueViewSet(viewsets.ModelViewSet):
    """
    List of Field Values
    """

    queryset = FieldValue.objects.all()
    serializer_class = serializers.FieldValueSerializer
