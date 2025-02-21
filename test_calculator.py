import pytest # type: ignore
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5

def test_subtract():
    assert calc.subtract(5, 2) == 3

def test_multiply():
    assert calc.multiply(3, 4) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
