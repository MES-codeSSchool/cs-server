from django import forms
from codeschool.lms.fields.models import Field, FieldValue

class FieldForm(forms.ModelForm):
    field_name = forms.CharField(label='Nome da propriedade', max_length=100)
    field_description = forms.CharField(label='Descrição da propriedade', max_length=300)
