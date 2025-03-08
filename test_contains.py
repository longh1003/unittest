import pytest
from contains import contains

def test_contains():
    with pytest.raises(ValueError, match="Khong phai so!"):
        contains([1, 2, "and", "#"], "#")