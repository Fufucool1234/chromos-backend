
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from core.tag_scorer import score_tags
from core.cluster_logic import cluster_and_label_tags
from core.generate_branch_with_reasons import generate_palette_branch
from core.utils import clean_prompt
import traceback

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    try:
        prompt = request.json.get('prompt', '')
        if not prompt:
            return jsonify({"error": "Prompt is missing."}), 400

        cleaned_prompt = clean_prompt(prompt)

        # Ensure score_tags receives a list of strings
        prompt_list = [cleaned_prompt]
        scored_tags = score_tags(prompt_list)
        clustered = cluster_and_label_tags(scored_tags)

        palette = generate_palette_branch(cleaned_prompt)

        return jsonify(palette), 200

    except Exception as e:
        print("🔥 Exception caught in /generate:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
