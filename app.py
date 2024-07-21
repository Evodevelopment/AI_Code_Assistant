
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import openai
from config import OPENAI_API_KEY

app = Flask(__name__)
socketio = SocketIO(app)
openai.api_key = OPENAI_API_KEY

@app.route('/complete', methods=['POST'])
def complete_code():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return jsonify(response.choices[0].text.strip())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    socketio.run(app, debug=True)
