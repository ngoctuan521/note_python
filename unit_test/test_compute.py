"""
pip install pytest

- create file with begin test_....py
- create functions begin def test_...()

run code: pytest
"""

from add import add

def test_case_negative():
    assert add(1,2) == -1

def test_case_positive():
    assert add(2,1) == 1

def test_case_zero():
    assert add(2,2) == 0