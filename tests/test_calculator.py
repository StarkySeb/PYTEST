import pytest
from src import calculator

def test_add():
    assert calculator.add(5,3) == 8

def test_add2():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(0,0) == 0

def test_addwrong():
    assert calculator.add_wrong(5,3) == 8
    
def test_addwrong2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0,5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(0,0) == 0

def test_subtract():
    assert calculator.subtract(5,3) == 2

def test_multiply():
    assert calculator.multiply(5,3) == 15

def test_multiplywrong():
    assert calculator.multiply_wrong(5,3) == 15

def test_divide():
    assert calculator.divide(8,2) == 4
