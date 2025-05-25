from tools.constants_lookup import lookup_constant
from tools.unit_converter import convert_units
from utils.gemini import gemini_answer

def is_constant_query(query: str) -> str:
    # Simple keyword-based check for known constants
    constants = ["speed of light", "gravitational constant", "planck constant"]
    for const in constants:
        if const in query.lower():
            return const
    return None

class PhysicsAgent:
    def handle_query(self, query: str):
        # Unit converter for 'convert ... to ...' queries
        conversion_result = convert_units(query)
        if conversion_result:
            return conversion_result
        const = is_constant_query(query)
        if const:
            result = lookup_constant(const)
            if isinstance(result, dict):
                return f"{const.title()}: {result['value']} {result['unit']} ({result['description']})"
            else:
                return result
        # Use Gemini API for non-constant queries
        return gemini_answer(query)
