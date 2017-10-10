from rest_framework import serializers

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

    class Meta:
        model = models.FieldValue
        fields = (
                'content', 'field', 'user'
        )
