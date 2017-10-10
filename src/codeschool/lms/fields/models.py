from django.utils.translation import ugettext_lazy as _
from codeschool import models

class Field(models.Model):
    """
    Declaration of an optional field.
    """
    TYPE_INT, TYPE_FLOAT, TYPE_STRING, TYPE_URL = range(4)

    TYPE_CHOICES = [
        (TYPE_INT, _('Integer')),
        (TYPE_FLOAT, _('Float')),
        (TYPE_STRING, _('String')),
        (TYPE_URL, _('URL'))
    ]

    name = models.CharField(
        max_length = 64,
        help_text=_(
            'Field name'
        ),
    )
    field_type = models.SmallIntegerField(
        choices=TYPE_CHOICES,
    )
    description = models.CharField(
        max_length = 200
    )

    def __str__(self):
        return '%s (%s)' %(self.name, self.TYPE_CHOICES[int(self.field_type)][1])



class FieldValue(models.Model):
    """
    Content of an optional field associated with an user.
    """

    field = models.ForeignKey('Field')
    user = models.ForeignKey('users.User')
    content = models.CharField(
        max_length = 200
    )

    class Meta:
        unique_together = [('field', 'user')]

    # Le a string e converte pro tipo certo.
    def value(self):
        if self.field.field_type == Field.TYPE_INT:
            return int(self.content)
        elif self.field.field_type == Field.TYPE_FLOAT:
            return float(self.content)
        elif self.field.field_type == Field.TYPE_STRING:
            return self.content
        elif self.field.field_type == Field.TYPE_URL:
            return self.content
