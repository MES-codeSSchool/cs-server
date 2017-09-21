from django.utils.translation import ugettext_lazy as _

from codeschool import models


class FieldModel(models.Model):
    """
    One dinamic field used in user forms.
    """

    name = models.CharField(
        max_length = 64,
        help_text=_(
            'Field name'
        ),
    )

    type_field = models.CharField(
        max_length = 20
    )

    description = models.CharField(
        max_length = 200
    )

    class Meta:
        abstract = True

class Fields(FieldModel):
    """
    eaeae
    """
