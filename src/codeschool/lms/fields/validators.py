from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import URLValidator
from codeschool.lms.fields import models

class ValidateContent(object):
    def __init__(self, field):
        self.field_type = field

    def __call__(self, value):
        # Custom validation for generic type field
        if self.field_type == models.Field.TYPE_INT:
            if not isinstance(value, int):
                raise ValidationError(
                    _('%(value)s is not an Integer'),
                    params={'value': value},
                )
        elif self.field_type == models.Field.TYPE_FLOAT:
            if not isinstance(value, float):
                raise ValidationError(
                    _('%(value)s is not an Float'),
                    params={'value': value},
                )
        elif self.field_type == models.Field.TYPE_URL:
            url_validator = URLValidator()
            try:
                url_validator(value)
            except:
                raise ValidationError(
                    _('%(value)s is not an URL'),
                    params={'value': value},
                )
