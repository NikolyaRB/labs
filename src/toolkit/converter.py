import json


def load_conversions() -> dict:
    with open("src/toolkit/conversions.json", "r") as file:
        return json.load(file)


# Verification that units of the same quantity
def unit_validation(from_unit: str, to_unit: str) -> None:
    lenght_unit = ("mm", "cm", "m", "km")
    mass_unit = ("g", "kg")
    temp_unit = ("c", "f", "k")
    if  from_unit in lenght_unit and to_unit in lenght_unit or\
        from_unit in mass_unit and to_unit in mass_unit or\
        from_unit in temp_unit and to_unit in temp_unit:
        pass
    else:
        raise ValueError("Conversion of measurement units of different classes or use of non-existent units")


# lenght convertion
def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    tables = load_conversions()["length"]
    result = value * tables[from_unit]
    result = result / tables[to_unit]
    return result


# mass conversion
def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    tables = load_conversions()["mass"]
    result = value * tables[from_unit]
    result = result / tables[to_unit]
    return result


# temperature convertion
def celsius_to_kelvin(value: float) -> float:
    return value + 273.15


def fahrenheit_to_kelvin(value: float) -> float:
    return (value - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(value: float) -> float:
    return value - 273.15 


def kelvin_to_fahrenheit(value: float) -> float:
    return (value - 273.15) * 9 / 5 + 32


# general translation function
def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    unit_validation(from_unit, to_unit)
    

    lenght_unit = ("mm", "cm", "m", "km")
    mass_unit = ("g", "kg")
    temp_unit = ("c", "f", "k")

    if from_unit in lenght_unit:
        return convert_length(value, from_unit, to_unit)
    
    elif from_unit in mass_unit:
        return convert_mass(value, from_unit, to_unit)

    elif from_unit in temp_unit:
        if from_unit == "c":
            kelvin_value = celsius_to_kelvin(value)
        elif from_unit == "f":
            kelvin_value = fahrenheit_to_kelvin(value)
        elif from_unit == "k":
            kelvin_value = value

        if kelvin_value < 0:
            raise ValueError("Temperature below absolute zero")
        if to_unit == "c":
            return kelvin_to_celsius(kelvin_value)
        if to_unit == "f":
            return kelvin_to_fahrenheit(kelvin_value)
        if to_unit == "k":
            return kelvin_value

    
