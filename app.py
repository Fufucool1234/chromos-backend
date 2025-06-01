from flask import Flask, request, jsonify
from flask_cors import CORS
from core.generate_branch_with_reasons import generate_palette_branch

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        output = generate_palette_branch(prompt)
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)