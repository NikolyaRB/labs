import pytest

from toolkit.calculator import calculation


def test_addition():
    assert calculation("2 + 3") == 5.0


def test_subtraction():
    assert calculation("10 - 4") == 6.0


def test_multiplication():
    assert calculation("3 * 4") == 12.0


def test_division():
    assert calculation("10 / 4") == 2.5


def test_operator_priority():
    assert calculation("2 + 9 - 3 * 4 / 3") == 7


def test_unary_minus():
    assert calculation("9 * -2") == -18.0


def test_float_numbers():
    assert calculation("1.5 + 2.5") == 4.0


def test_without_spaces():
    assert calculation("2+3*4") == 14.0


def test_many_spaces():
    assert calculation("2     +      3   *    4") == 14.0


def test_unary_operator_at_start():
    assert calculation("- 5 + 3") == -2.0


# negative
def test_empty_expression():
    with pytest.raises(ValueError):
        calculation("")


def test_missing_operand():
    with pytest.raises(ValueError):
        calculation("2 +")


def test_two_binary_operators():
    with pytest.raises(ValueError):
        calculation("2 + * 3")


def test_invalid_character():
    with pytest.raises(ValueError):
        calculation("2 + abc")


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculation("5 / 0")
