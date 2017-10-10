import pytest

from codeschool.lms.fields.models import Field

class TestField:

    def create_field(self):
        name = "GitHub"
        field_type = 1
        description = "Insira aqui seu GitHub"

        return Field(name=name, field_type=field_type,
                          description=description)


    def test_create_field(self):
        field = self.create_field()
