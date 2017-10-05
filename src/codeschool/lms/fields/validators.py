from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import URLValidator

def validate_content(self):
    # Custom validation for generic type field
    if self.field.field_type == Field.TYPE_INT:
        if not isinstance(self.content, int):
            raise ValidationError(_('Content must be a Int'), code='error1')
    elif self.field.field_type == Field.TYPE_FLOAT:
        if not isinstance(self.content, float):
            raise ValidationError(_('Content must be a float'), code='error1')
    elif self.field.field_type == Field.TYPE_URL:
        url_validator = URLValidator()
        try:
            url_validator(self.content)
        except:
            ValidationError(_('Content must be a URL'),code='error1')
