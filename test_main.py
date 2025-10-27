import pytest 

from rest_api import Person 

@pytest.fixture(scope='function')
def add_person():
    p = Person()
    p.name = "ali"
    yield p  
    del p 


def test_check_object_person(add_person):
    p = add_person
    
    assert p.name == "ali"
    
