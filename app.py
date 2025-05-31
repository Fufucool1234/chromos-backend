from flask import Flask, request, jsonify
from flask_cors import CORS
from core.generate_branch_with_reasons import generate_palette_branch

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    result = generate_palette_branch(prompt)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)