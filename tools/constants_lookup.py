PHYSICS_CONSTANTS = {
    "speed_of_light": {
        "value": 299792458,
        "unit": "m/s",
        "description": "Speed of light in vacuum"
    },
    "gravitational_constant": {
        "value": 6.67430e-11,
        "unit": "m^3 kg^-1 s^-2",
        "description": "Universal gravitational constant"
    },
    "planck_constant": {
        "value": 6.62607015e-34,
        "unit": "J s",
        "description": "Planck constant"
    },
    # Add more constants as needed
}

def lookup_constant(name: str):
    key = name.lower().replace(" ", "_")
    return PHYSICS_CONSTANTS.get(key, f"Constant '{name}' not found.")
