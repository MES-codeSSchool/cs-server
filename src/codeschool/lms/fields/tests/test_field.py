import pytest

from codeschool.lms.fields.models import (Field, FieldValue, get_form_class, get_form_field)
from codeschool.core.users.factories import (FullUserFactory, UserFactory, make_students)


@pytest.fixture
def char_field():
    name = "github"
    field_type = Field.TYPE_URL
    description = "Insira aqui seu GitHub"
    return Field(id=0, name=name, field_type=field_type, description=description)


@pytest.fixture
def db_char_field(char_field):
    char_field.save()
    return char_field


@pytest.fixture
def form_class(char_field):
    return get_form_class((char_field,))


def test_form_validates(form_class):
    form = form_class({'github': 'https://github.com/someone', 'age': '42'})
    assert form.is_valid()

    form = form_class({'github': 'https://github.com/someone', 'age': '0'})
    assert form.is_valid()


def test_form_do_not_validates(form_class):
    form = form_class({'github': 'https://github.com/someone', 'age': 'bad'})
    assert form.is_valid()

    form = form_class({'github': 'https://github.com/someone', 'age': ''})
    assert form.is_valid()

# Finalize test.
# class TestField:
#     def test_create_correct_form_field(self, field):
#         field = get_form_field(field)
#         assert type(field) is field.CharField


class TestFieldValue:
    def create_field_value(self, user):
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
