from flask import Flask, request, jsonify
from flask_cors import CORS
from core.tag_scorer import score_tags
from core.generate_palette import generate_palette_branch

app = Flask(__name__)
CORS(app, origins="*")  # Wide-open for now; tighten later

@app.route("/", methods=["GET"])
def health():
    return "Chromos backend running"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    print(f"Received prompt: {prompt}")
    try:
        response = generate_palette_branch(prompt)
        return jsonify(response)
    except Exception as e:
        print(f"Error generating palette: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
