# class3

### Assignment Problem Statement:
You are tasked with creating a Python class named `AdvancedNumber` that models a custom numerical type with rich functionality using Python's special methods. 

#### Functional Requirements:
1. **Initialization and String Representation**:
   - Initialize an `AdvancedNumber` object with a single integer or float value.
   - Implement `__str__` and `__repr__` to return human-readable and developer-focused representations, respectively.

2. **Arithmetic Operators**:
   - Overload `+`, `-`, `*`, `/`, and `%` to work with another `AdvancedNumber` or a plain integer/float.

3. **Comparison Operators**:
   - Overload `<`, `<=`, `>`, `>=`, `==`, and `!=` to compare the stored value with another `AdvancedNumber` or plain numbers.

4. **Hashing and Boolean Conversion**:
   - Make the `AdvancedNumber` objects hashable and ensure they work in sets and as dictionary keys.
   - Convert an `AdvancedNumber` to a boolean (`True` if non-zero, `False` otherwise).

5. **Callable Behavior**:
   - Make the object callable. When called, it should return the stored value squared.

6. **Custom Formatting**:
   - Support custom string formatting using the `__format__` method:
     - `{obj:.2f}` should format the number with two decimal places.
     - `{obj:#x}` should return the hexadecimal representation if the number is an integer.

7. **Destructor**:
   - Print a message like `"AdvancedNumber with value <value> is being destroyed"` when an object is deleted.

---

### Provided `pytest` File
```python
import pytest
from advanced_number import AdvancedNumber

def test_initialization():
    obj = AdvancedNumber(5)
    assert obj.value == 5

def test_str_repr():
    obj = AdvancedNumber(5)
    assert str(obj) == "Value: 5"
    assert repr(obj) == "AdvancedNumber(5)"

def test_arithmetic_operations():
    obj1 = AdvancedNumber(10)
    obj2 = AdvancedNumber(5)
    assert (obj1 + obj2).value == 15
    assert (obj1 - obj2).value == 5
    assert (obj1 * 2).value == 20
    assert (obj1 / obj2).value == 2.0
    assert (obj1 % obj2).value == 0

def test_comparison_operations():
    obj1 = AdvancedNumber(10)
    obj2 = AdvancedNumber(5)
    assert obj1 > obj2
    assert obj2 < obj1
    assert obj1 != obj2
    assert obj1 >= AdvancedNumber(10)
    assert obj2 <= AdvancedNumber(5)

def test_hashable():
    obj1 = AdvancedNumber(10)
    obj2 = AdvancedNumber(10)
    obj_set = {obj1, obj2}
    assert len(obj_set) == 1

def test_boolean_conversion():
    assert bool(AdvancedNumber(10)) is True
    assert bool(AdvancedNumber(0)) is False

def test_callable():
    obj = AdvancedNumber(4)
    assert obj() == 16

def test_custom_formatting():
    obj = AdvancedNumber(10)
    assert format(obj, ".2f") == "10.00"
    assert format(obj, "#x") == "0xa"

def test_destruction(capsys):
    obj = AdvancedNumber(5)
    del obj
    captured = capsys.readouterr()
    assert "AdvancedNumber with value 5 is being destroyed" in captured.out
```

---

### GitHub Actions Workflow File (`.github/workflows/python-tests.yml`)
```yaml
name: Python Tests

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Run tests
        run: |
          pytest
```

### Instructions for Students:
1. Create a new repository on GitHub and clone it to your local machine.
2. Implement the `AdvancedNumber` class in a file named `advanced_number.py`.
3. Add the provided `pytest` file as `test_advanced_number.py`.
4. Add the provided GitHub Actions workflow file to `.github/workflows/`.
5. Push your implementation to the GitHub repository and verify your tests run automatically.
