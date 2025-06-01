
import re

def clean_prompt(prompt: str) -> str:
    """
    Clean the user input by removing special characters, excess whitespace,
    and standardizing the format.
    """
    prompt = re.sub(r"[^\w\s-]", "", prompt)  # Remove punctuation
    prompt = re.sub(r"\s+", " ", prompt)      # Replace multiple spaces with one
    return prompt.strip().lower()
