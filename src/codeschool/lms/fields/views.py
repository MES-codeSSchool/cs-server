from rest_framework import viewsets

from django.shortcuts import render
from . import serializers
from .models import Field, FieldValue


class FieldViewSet(viewsets.ModelViewSet):
    """
    List of Fields.
    """

    queryset = Field.objects.all()
    serializer_class = serializers.FieldSerializer


class FieldValueViewSet(viewsets.ModelViewSet):
    """
    List of Field Values
    """

    queryset = FieldValue.objects.all()
    serializer_class = serializers.FieldValueSerializer
