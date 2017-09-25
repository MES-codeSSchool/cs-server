from rest_framework import serializers

from . import models

class FieldValueSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Field Value objects.
    """
    pass
    # class Meta:
    #     model = models.FieldValue
    #     fields = (
    #             'fields', 'content', 'user',
    #     )
