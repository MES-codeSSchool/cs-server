from rest_framework import viewsets

from django.shortcuts import render
from .forms import FieldForm
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


def get_field(request):
    """
    Function of Field Forms
    """
    form = FieldForm(request.POST)
    response = render(request, 'template/field_template.html', {'form': form})
    return response

def test(request):
    form = FieldForm()
    return render(request, 'codeschool/field_template.html', {'form':form})
