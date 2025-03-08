import pytest
from reverse_string import reverse_string

def test_reverse_string():
    assert reverse_string("World!") == "!dlroW"

def test_reverse_string_with_space():
    assert reverse_string("    h  illo   ") == "olli  h"

def test_reverse_string_blank():
    assert reverse_string("") #AssertionError? -> AssertionError is not the same as bug