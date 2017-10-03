import pytest

from codeschool.lms.field.models import Field

class TestField:

    def create_field(self):
        name = "GitHub"
        type_field = "String"
        description = "Insira aqui seu GitHub"

        return Field(name=name, type_field=type_field,
                          description=description)


    def test_create_field(self):
        field = self.create_field()
