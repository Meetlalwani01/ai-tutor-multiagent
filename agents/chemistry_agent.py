from tools.periodic_table import lookup_element
from utils.gemini import gemini_answer

def is_element_query(query: str) -> str:
    # Simple keyword-based check for element lookup
    keywords = ["element", "atomic number", "symbol", "periodic table"]
    for word in keywords:
        if word in query.lower():
            return query
    return None

class ChemistryAgent:
    def handle_query(self, query: str):
        if is_element_query(query):
            return lookup_element(query)
        return gemini_answer(query) 