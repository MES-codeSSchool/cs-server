from django import forms


class FieldForm(forms.ModelForm):
    name = forms.CharField(label='Nome da propriedade', max_length=100)
    description = forms.CharField(label='Descrição da propriedade', max_length=300)
