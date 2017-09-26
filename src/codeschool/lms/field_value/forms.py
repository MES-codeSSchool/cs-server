from django import forms

form .models import FieldValue

class FieldValueForm(forms.ModelForm):

    class Meta:
        model = FieldValue
        fields = ('content')
