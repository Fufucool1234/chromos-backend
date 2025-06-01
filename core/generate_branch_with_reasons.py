from core.luma_engine import generate_palette
from core.tag_scorer import score_tags
from core.cluster_logic import cluster_and_label_tags

def generate_palette_branch(prompt: str):
    tags = prompt.split()
    scored_tags = score_tags(tags)
    clustered_tags = cluster_and_label_tags(scored_tags)
    palette_output = generate_palette(prompt, clustered_tags)
    return palette_output