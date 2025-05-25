<<<<<<< HEAD
# ai-tutor-multiagent
=======
# AI Tutor Agent (Multi-Agent System)

This project implements a multi-agent AI tutoring assistant based on modular agent design principles. The system features a main Tutor Agent that routes user queries to specialist sub-agents (Math Agent, Physics Agent), each capable of using tools and generating responses (mocked Gemini API).

## Features
- **Tutor Agent**: Main interface, routes queries to sub-agents.
- **Math Agent**: Handles math questions, uses a calculator tool for arithmetic.
- **Physics Agent**: Handles physics questions, uses a constants lookup tool.
- **Web Interface**: Simple HTML form for user queries.
- **API Endpoint**: `/api/ask` for programmatic access.
- **Gemini API**: Mocked for demo; easy to integrate real API.

## Project Structure
```
/agents
    tutor_agent.py
    math_agent.py
    physics_agent.py
/tools
    calculator.py
    constants_lookup.py
/templates
    index.html
app.py
requirements.txt
README.md
```

## Setup & Running Locally
1. **Clone the repo**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   python app.py
   ```
4. **Open in browser**: [http://localhost:5000](http://localhost:5000)

## API Usage
- **POST** `/api/ask` with JSON `{ "query": "your question" }`
- Returns: `{ "answer": "..." }`

## Deployment
- Ready for deployment on Vercel, Railway, or similar platforms.
- Store your Gemini API key securely (if using real API).

## How It Works
- The Tutor Agent uses simple keyword matching to route queries to the Math or Physics Agent.
- Math Agent uses a calculator tool for arithmetic; Physics Agent uses a constants lookup tool.
- All other queries are answered with a mocked Gemini API response.

## Extending
- Add more sub-agents or tools for other subjects.
- Integrate the real Gemini API by replacing the mock responses.
- Improve intent recognition with NLP or Gemini API.

## License
MIT
>>>>>>> 37db167 (Initial commit: Multi-agent AI Tutor)
