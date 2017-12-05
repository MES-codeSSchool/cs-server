import pytest

from codeschool.lms.fields.models import (Field, get_form_class, FieldValue)
from codeschool.lms.fields.serializers import (FieldSerializer, FieldValueSerializer)


@pytest.fixture
def char_field():
    name = "github"
    field_type = Field.TYPE_URL
    description = "Insira aqui seu GitHub"
    return Field(id=0, name=name, field_type=field_type, description=description)


@pytest.fixture
def int_field():
    name = "age"
    field_type = Field.TYPE_INT
    description = "Insira aqui sua idade"
    return Field(id=1, name=name, field_type=field_type, description=description)


@pytest.fixture
def db_char_field(char_field):
    char_field.save()
    return char_field


@pytest.fixture
def form_class(char_field, int_field):
    return get_form_class((char_field, int_field))


def test_api_module_imports_without_errors():
    import codeschool.lms.fields.api
    import codeschool.lms.fields.serializers
    import codeschool.lms.fields.views


def test_form_validates(form_class):
    form = form_class({'github': 'https://github.com/someone', 'age': '42'})
    assert form.is_valid()

    form = form_class({'github': 'https://github.com/someone', 'age': '0'})
    assert form.is_valid()


def test_form_do_not_validates(form_class):
    form = form_class({'github': 'https://github.com/someone', 'age': ' '})
    assert not form.is_valid()

    form = form_class({'github': 'https://github.com/someone', 'age': 'bad'})
    assert not form.is_valid()
    

class TestFieldValue:
    pass
