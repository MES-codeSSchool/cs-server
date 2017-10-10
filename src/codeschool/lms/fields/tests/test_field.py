import pytest

from codeschool.lms.fields.models import Field, FieldValue
from codeschool.core.users.factories import (
FullUserFactory, UserFactory, make_students
)

class TestField:

    def create_field(self):
        name = "GitHub"
        field_type = 1
        description = "Insira aqui seu GitHub"

        return Field(name=name, field_type=field_type,
                          description=description)


    def test_create_field(self):
        field = self.create_field()


class TestFieldValue:

    def setup_class(cls):
        name = "GitHub"
        field_type = 1
        description = "Insira aqui seu GitHub"

        cls.field = Field(name=name, field_type=field_type,
                          description=description)

        students = make_students(1, commit=False)
        cls.student = students[0]
        cls.content = "0123456"


    def create_field_value(self):
        field_value = self.field_value()

        assert self.content == field_value.content
        assert self.field == field_value.fields
        assert self.user == field_value.user


    def field_value(self):
        return FiledValue(content=self.content, fields=self.field, user=self.student)

    def test_field_value_db_insertion(self):
        # field_value = self.field_value()
        pass

    def teardown_class(cls):
        pass
