from rest_framework import serializers

from . import models

class FieldValueSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Field Value objects.
    """

    class Meta:
        model = models.FieldValue
        fields = (
                'content', 'fields', 'user',
        )
