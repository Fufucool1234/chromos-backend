from core.tag_scorer import score_tags
from core.label_clusters import get_label_category

def cluster_and_label_tags(tags):
    """
    Cluster tags using sentence-transformers and KMeans,
    then label each cluster using the get_label_category logic.
    Returns a list of dictionaries with cluster labels and their tags.
    """
    # Score and embed tags
    scored = score_tags(tags)
    vectors = [s['embedding'] for s in scored]
    raw_tags = [s['tag'] for s in scored]

    # Simple KMeans clustering
    from sklearn.cluster import KMeans
    import numpy as np

    k = min(5, len(tags))  # Avoid asking for more clusters than tags
    kmeans = KMeans(n_clusters=k, random_state=0, n_init='auto').fit(vectors)
    labels = kmeans.labels_

    # Group tags by cluster
    clusters = {}
    for idx, cluster_id in enumerate(labels):
        tag = raw_tags[idx]
        clusters.setdefault(cluster_id, []).append(tag)

    # Assign a label to each cluster
    labeled_clusters = []
    for cluster_id, tags in clusters.items():
        label = get_label_category(tags)
        labeled_clusters.append({
            "label": label,
            "tags": tags
        })

    return labeled_clusters