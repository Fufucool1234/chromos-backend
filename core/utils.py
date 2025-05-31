import re

def clean_string(text):
    return re.sub(r'\s+', ' ', text.strip().lower())