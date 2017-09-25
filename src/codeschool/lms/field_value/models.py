from django.utils.translation import ugettext_lazy as _

from codeschool import models

class FiledValueModel(models.Model):

    # Field created in class FieldModel
    fields = models.ManyToManyField(
        models.Field,
        verbose_name=_('fields'),
        blank=True,
    )

    content = models.CharField(
        max_length = 200,
        help_text =_(
            'Content'
        ),
    )

    user = model.ManyToManyField(
        models.User,
        verbose_name=_('user'),
        related_name='classrooms_as_student',
        blank=True,
    )

    class Meta:
        abstract = True

class FieldValue(FiledValueModel):
    """
    Class for Field Value
    """
