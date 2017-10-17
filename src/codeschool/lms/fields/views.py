from rest_framework import viewsets

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FieldForm

from django.views.generic.edit import FormView
from . import serializers
from .models import Field, FieldValue

class FieldViewSet(FormView):
    """
    List of Fields.
    """
    http_method_names = [u'get', u'post']

    queryset = Field.objects.all()
    serializer_class = serializers.FieldSerializer

    def get(self, request):
        form = FieldForm()
        return render(request, 'template/field_template.html', {'form': form})

    def post(self,request):
        form = FieldForm()
        return render(request, 'template/field_template.html', {'form': form})


    # def post(request):
    #     # if this is a POST request we need to process the form data
    #     if request.method == 'POST':
    #         # create a form instance and populate it with data from the request:
    #         form = FieldForm(request.POST)
    #         # check whether it's valid:
    #         if form.is_valid():
    #             # process the data in form.cleaned_data as required
    #             # ...
    #             # redirect to a new URL:
    #             return HttpResponseRedirect('')
    #
    #     # if a GET (or any other method) we'll create a blank form
    #     else:



class FieldValueViewSet(viewsets.ModelViewSet):
    """
    List of Field Values
    """

    queryset = FieldValue.objects.all()
    serializer_class = serializers.FieldValueSerializer
