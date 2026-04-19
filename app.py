
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load FAQ data from JSON file
with open('faq.json', 'r') as f:
    faq_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['question'].lower().strip()
    answer = faq_data.get(user_question, "Sorry, I don't know the answer to that question yet.")
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)



