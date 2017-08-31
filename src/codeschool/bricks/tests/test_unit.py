import pytest
from codeschool.bricks.utils import with_class, tag_join, title
from bricks.html5 import p, div

class TitleObject(object):
    title = ""
    def __init__(self, title):
        self.title = title

class NoTitleObject(object):
    def __init__(self):
        print('createad')
    def  __str__(self):
        return 'class description'

def make_title_object(title):
    return TitleObject(title)

def callable_p_tag():
    return p('no-text', class_='no-class')

class TestUtils:
    """
    Unit test for util module methods (with_class, tag_join, title)
    """

    def setup_method(self, test_method):
        self.title_object = make_title_object('no title')
        self.no_title_object = NoTitleObject()

    def test_title_name(self):
        assert title(self.title_object) == 'no title', 'Can\'t get title from object'

    def test_no_title_object(self):
        assert title(self.no_title_object) == 'class description', 'Can\'t get class name as title'

    def test_tag_join(self):
        join_result = tag_join(['p1', 'p2', 'p3'], 'div')
        assert join_result == ['p1', 'div', 'p2', 'div', 'p3']

    def test_with_class_base_component(self):
        pTag = p('hello!', class_="bem-css")
        pTagWithClass = with_class(pTag, 'bem-css--django')

        assert str(pTagWithClass) == '<p class="bem-css--django bem-css">hello!</p>'

    def test_with_class_mapping(self):
        classDict = {'class_': 'cool-class'}
        classDict = with_class(classDict, 'cool-class--modifier')
        assert classDict == {'class_': ['cool-class--modifier', 'cool-class']}

    def test_with_class_none(self):
        assert None == with_class(None, None)

    def test_with_class_callable(self):
        result = with_class(callable_p_tag, 'test-class')
        assert str(result()) == '<p class="test-class no-class">no-text</p>'
