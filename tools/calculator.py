def calculate(expression: str) -> float:
    """
    Evaluates a basic arithmetic expression (addition, subtraction, multiplication, division).
    Only supports numbers and +, -, *, / operators.
    """
    try:
        # WARNING: eval is dangerous in production! Here, we use it for simplicity and mock/demo purposes only.
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error: {str(e)}"
