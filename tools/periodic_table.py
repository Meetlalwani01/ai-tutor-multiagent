PERIODIC_TABLE = {
    "H": {"name": "Hydrogen", "atomic_number": 1},
    "He": {"name": "Helium", "atomic_number": 2},
    "Li": {"name": "Lithium", "atomic_number": 3},
    "C": {"name": "Carbon", "atomic_number": 6},
    "O": {"name": "Oxygen", "atomic_number": 8},
    "N": {"name": "Nitrogen", "atomic_number": 7},
    "Na": {"name": "Sodium", "atomic_number": 11},
    "Cl": {"name": "Chlorine", "atomic_number": 17},
    # ... add more as needed
}

def lookup_element(query: str):
    q = query.strip().lower()
    for symbol, data in PERIODIC_TABLE.items():
        if symbol.lower() in q or data["name"].lower() in q or str(data["atomic_number"]) in q:
            return f"Element: {data['name']} (Symbol: {symbol}, Atomic Number: {data['atomic_number']})"
    return "Element not found in periodic table." 