import pytest

def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 1

def test_type():
    assert type('hello' is str)
    assert type('hello') != int

def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

@pytest.fixture()
def default_student():
    return Student("John", 18)

def test_student_init(default_student):
    assert default_student.name == "John"
    assert default_student.age == 18