from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from . import models


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Field objects.
    """

    class Meta:
        model = models.Field
        fields = (
                'name', 'field_type', 'description',
        )

class FieldValueSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Field Value objects.
    """

    def validate(self, data):
        # Custom validation for generic type field
        field = data['field']
        value = data['content']

        if field.field_type == models.Field.TYPE_INT:
            try:
                parsed_value = int(value)
            except:
                raise ValidationError(
                    _('%(value)s is not an Integer'),
                    params={'value': value},
                )
        elif field.field_type == models.Field.TYPE_FLOAT:
            try:
                parsed_value = float(value)
            except:
                raise ValidationError(
                    _('%(value)s is not an Float'),
                    params={'value': value},
                )
        elif field.field_type == models.Field.TYPE_URL:
            url_validator = URLValidator()
            try:
                url_validator(value)
            except:
                raise ValidationError(
                    _('%(value)s is not an URL'),
                    params={'value': value},
                )

        return data

    class Meta:
        model = models.FieldValue
        fields = (
                'content', 'field', 'user'
        )
