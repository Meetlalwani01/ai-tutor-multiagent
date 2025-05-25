from tools.calculator import calculate
from tools.symbolic_solver import symbolic_solve
from utils.gemini import gemini_answer

def is_math_expression(query: str) -> bool:
    # Simple check for arithmetic expressions
    return any(op in query for op in ['+', '-', '*', '/'])

class MathAgent:
    def handle_query(self, query: str):
        # Symbolic solver for 'solve ... for ...' queries
        symbolic_result = symbolic_solve(query)
        if symbolic_result:
            return symbolic_result
        if is_math_expression(query):
            result = calculate(query)
            return f"Calculator result: {result}"
        # Use Gemini API for non-calculation math queries
        return gemini_answer(query)
