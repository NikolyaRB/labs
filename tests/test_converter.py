import pytest

from toolkit.converter import convert


def test_length_cm_to_m():
    assert convert(100, "cm", "m") == 1.0


def test_length_km_to_m():
    assert convert(1, "km", "m") == 1000.0


def test_mass_kg_to_g():
    assert convert(2, "kg", "g") == 2000.0


def test_celsius_to_kelvin():
    assert convert(0, "c", "k") == 273.15


def test_fahrenheit_to_celsius():
    assert convert(32, "f", "c") == pytest.approx(0.0)


def test_kelvin_to_fahrenheit():
    assert convert(273.15, "k", "f") == pytest.approx(32.0)


def test_unit_case_ignored():
    assert convert(100, "CM", "M") == 1.0


def test_unknown_unit():
    with pytest.raises(ValueError):
        convert(10, "abc", "m")


def test_incompatible_length_and_mass():
    with pytest.raises(ValueError):
        convert(10, "kg", "m")


def test_incompatible_temperature_and_mass():
    with pytest.raises(ValueError):
        convert(10, "c", "kg")


def test_celsius_below_absolute_zero():
    with pytest.raises(ValueError):
        convert(-274, "c", "k")


def test_kelvin_below_absolute_zero():
    with pytest.raises(ValueError):
        convert(-1, "k", "c")


