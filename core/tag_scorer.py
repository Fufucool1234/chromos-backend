
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def score_tags(tag_list):
    if not isinstance(tag_list, list):
        raise ValueError("Input must be a list of strings.")

    embeddings = model.encode(tag_list)
    return [
        {
            "tag": tag,
            "embedding": embedding.tolist()
        }
        for tag, embedding in zip(tag_list, embeddings)
    ]
