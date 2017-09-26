from codeschool import models
from codeschool.lms.field.models import Field
from codeschool.core.users.models import User

class FiledValue(models.Model):

    content = models.CharField(
        max_length = 200,
    )

    # Field created in class FieldModel
    fields = models.ManyToManyField(Field)

    user = models.ManyToManyField(User)
