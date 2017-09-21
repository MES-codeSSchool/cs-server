from django.utils.translation import ugettext_lazy as _

from codeschool import models

class FiledValueModel(models.Model):

    content = models.CharField(
        max_length = 200,
        help_text =_(
            'Content'
        ),
    )

    user = model.ManyToManyField(
        models.User
    )
