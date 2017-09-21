from rest_framework import serializers

from . import models


class FieldSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize Field objects.
    """

    class Meta:
        model = models.Fields
        fields = (
                'name', 'type_field', 'description',
        )
