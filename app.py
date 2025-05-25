from flask import Flask, request, render_template, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from agents.tutor_agent import TutorAgent
import markdown
import os
from datetime import datetime
from uuid import uuid4

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conversations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_secret_key')
db = SQLAlchemy(app)
tutor_agent = TutorAgent()

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), index=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def get_user_id():
    if 'user_id' not in session:
        session['user_id'] = str(uuid4())
    return session['user_id']

@app.route('/', methods=['GET', 'POST'])
def index():
    user_id = get_user_id()
    answer = None
    error = None
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if not query:
            error = "Please enter a question."
        else:
            try:
                raw_answer = tutor_agent.route_query(query)
                answer = markdown.markdown(raw_answer, extensions=['fenced_code', 'tables'])
                db.session.add(Conversation(user_id=user_id, question=query, answer=raw_answer))
                db.session.commit()
            except Exception as e:
                error = f"Sorry, something went wrong: {str(e)}"
    history = Conversation.query.filter_by(user_id=user_id).order_by(Conversation.timestamp.desc()).all()
    history_rendered = [(c.question, markdown.markdown(c.answer, extensions=['fenced_code', 'tables'])) for c in history]
    return render_template('index.html', answer=answer, history=history_rendered, error=error)

@app.route('/api/ask', methods=['POST'])
def api_ask():
    user_id = get_user_id()
    data = request.get_json()
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'answer': '<span style="color:red;">Please enter a question.</span>'})
    try:
        raw_answer = tutor_agent.route_query(query)
        answer = markdown.markdown(raw_answer, extensions=['fenced_code', 'tables'])
        db.session.add(Conversation(user_id=user_id, question=query, answer=raw_answer))
        db.session.commit()
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'answer': f'<span style="color:red;">Sorry, something went wrong: {str(e)}</span>'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
