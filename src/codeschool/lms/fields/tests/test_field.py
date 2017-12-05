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

# Finalize test.
# class TestField:
#     def test_create_correct_form_field(self, field):
#         field = get_form_field(field)
#         assert type(field) is field.CharField


def setUp(self):
        self.field_attributes = {
            'name': 'GitHub',
            'field_type': Field.TYPE_URL,
            'description': 'GitHub'
        }

        self.serializer_data = {
            'name': 'URI',
            'field_type': Field.TYPE_INT,
            'description': 'URI'
        }

        self.field = Field.objects.create(**self.field_attributes)
        self.serializer = FieldSerializer(instance=self.field)


@pytest.fixture
def test_field_serializer(validate):
    data = validate.serializer.data

    assert (set(data.keys()) == set(['content', 'field', 'user']))


@pytest.fixture
def test_name_field_content(self):
    data = self.serializer.data

    assert (data['name'] == self.field_attributes['name'])


@pytest.fixture
def test_size_lower_bound(self):
    self.serializer_data['field_type'] = Field.TYPE_INT

    serializer = FieldValueSerializer(data=self.serializer_data)

    assert not (serializer.is_valid())
    assert (set(serializer.errors) == set(['field_type']))


class TestFieldValue:
    def create_field_value(self, user):
        field_value = self.value()

        assert self.content == field_value.content
        assert self.field == field_value.fields
        assert self.user == field_value.user

    def field_value(self):
        return FiledValue(content=self.content, fields=self.field, user=self.student)

    def test_field_value_db_insertion(self):
        pass

    def teardown_class(cls):
        pass
