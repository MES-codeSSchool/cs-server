from rest_framework import viewsets

from . import serializers
from .models import Field

class FieldViewSet(viewsets.ModelViewSet):
    """
    List of Fields.
    """

    queryset = Field.objects.all()
    serializer_class = serializers.FieldSerializer
