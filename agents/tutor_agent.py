from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent
from agents.chemistry_agent import ChemistryAgent
from utils.gemini import gemini_answer

class TutorAgent:
    def __init__(self):
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()
        self.chemistry_agent = ChemistryAgent()

    def route_query(self, query: str):
        # Simple keyword-based routing
        math_keywords = ["math", "calculate", "+", "-", "*", "/", "solve", "equation"]
        physics_keywords = ["physics", "speed of light", "gravitational constant", "planck constant", "force", "energy"]
        chemistry_keywords = ["chemistry", "element", "atomic number", "symbol", "periodic table", "molecule", "compound"]

        if any(word in query.lower() for word in math_keywords):
            return self.math_agent.handle_query(query)
        elif any(word in query.lower() for word in physics_keywords):
            return self.physics_agent.handle_query(query)
        elif any(word in query.lower() for word in chemistry_keywords):
            return self.chemistry_agent.handle_query(query)
        else:
            # Use Gemini API for other subjects
            return gemini_answer(query)
