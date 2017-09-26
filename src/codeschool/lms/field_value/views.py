from rest_framework import viewsets

from . import serializers
from . import models
from .forms import FieldValueForm

class FieldValueViewSet(formView):
    """
    List of Field Values
    """
    form = FieldValueForm()
    return render(request, 'field_value.html', {'form': form})
    queryset = FieldValue.objects.all()
    serializer_class = serializers.FieldValueSerializer
