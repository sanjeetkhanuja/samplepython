from flask import Flask, jsonify, request
import json

app = Flask(__name__)

questions = [
  { 'description': 'which is capital of India 3 ?', 'answer': 'DELHI' }
]

@app.route('/question')
def get_question():
  return jsonify(questions)

@app.route('/')
def get_health():
  return 'OK', 200

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=5000, use_reloader=True)