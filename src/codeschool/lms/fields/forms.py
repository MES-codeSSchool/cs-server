from django import forms


class FieldValueForm(forms.ModelForm):
    content = forms.CharField(label='Content', max_length=200)
