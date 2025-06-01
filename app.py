from flask import Flask, request, jsonify
from flask_cors import CORS
from core.tag_scorer import score_tags
from core.generate_branch_with_reasons import generate_palette_branch
from core.cluster_logic import cluster_and_label_tags

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "No prompt provided."}), 400

        cleaned_prompt = prompt.strip()
        scored_tags = score_tags([cleaned_prompt])  # FIXED: wrapped in list
        clustered = cluster_and_label_tags(scored_tags)
        result = generate_palette_branch(prompt, clustered)

        return jsonify(result)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)