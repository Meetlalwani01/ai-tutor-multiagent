from pint import UnitRegistry
import re
ureg = UnitRegistry()

def convert_units(query: str):
    match = re.search(r'convert ([\d\.]+) ([a-zA-Z]+) to ([a-zA-Z]+)', query.lower())
    if not match:
        return None
    value, from_unit, to_unit = match.groups()
    try:
        quantity = ureg.Quantity(float(value), from_unit)
        converted = quantity.to(to_unit)
        return f"{value} {from_unit} = {converted:.4g} {to_unit}"
    except Exception as e:
        return f"Error converting units: {str(e)}" 