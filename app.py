from flask import Flask, request, jsonify
from flask_cors import CORS
from core.generate_branch_with_reasons import generate_palette_branch
from core.utils import clean_prompt

app = Flask(__name__)
CORS(app, origins="*")  # You can replace "*" with your frontend URL in production

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        cleaned_prompt = clean_prompt(prompt)

        # Generate the palette using your backend engine
        output = generate_palette_branch(cleaned_prompt)

        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
