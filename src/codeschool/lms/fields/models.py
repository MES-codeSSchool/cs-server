from django.utils.translation import ugettext_lazy as _

from codeschool import models


class Field(models.Model):
    """
    Declaration of an optional field.
    """

    name = models.CharField(
        max_length = 64,
        help_text=_(
            'Field name'
        ),
    )
    field_type = models.CharField(
        max_length = 20
    )
    description = models.CharField(
        max_length = 200
    )

    def __str__(self):
        return '%s (%s)' %(self.name, self.field_type)

class FieldValue(models.Model):
    """
    Content of an optional field associated with an user.
    """

    field = models.ForeignKey('Field')
    user = models.ForeignKey('users.User')
    content = models.CharField(
        max_length = 200,
    )

    class Meta:
        unique_together = [('field', 'user')]
