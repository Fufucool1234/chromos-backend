from flask import Flask, request, jsonify
from flask_cors import CORS

from core.tag_scorer import score_tags
from core.utils import clean_string
from core.luma_engine import LumaEngine
from core.label_clusters import get_label_category
from core.cluster_logic import cluster_and_label_tags

app = Flask(__name__)

# Allow only your frontend domain in production
CORS(app, resources={r"/generate": {"origins": "https://chromos-nextjs.vercel.app"}})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    cleaned_prompt = clean_string(prompt)
    scored_tags = score_tags(cleaned_prompt)
    clustered = cluster_and_label_tags(scored_tags)
    labels = [t["label"] for t in clustered]
    
    engine = LumaEngine(prompt, override_tags=labels)
    engine.run_all()

    return jsonify(engine.output_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
