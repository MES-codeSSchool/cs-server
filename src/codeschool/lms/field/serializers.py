from rest_framework import serializers

from . import models


class FieldSerializer(serializers.HyperLinkedModelSerializer):
    """
    Serialize Field objects.
    """

    class Meta:
        model = models.Classroom
        fields = (
                'name', 'type_field', 'description', 
        )
