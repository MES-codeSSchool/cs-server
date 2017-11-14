from django import forms
from .models import Field

class FieldForm(forms.ModelForm):
    content = forms.CharField(label='Content', max_length=200)

    class Meta:
        model = Field
        fields = ('name',)
