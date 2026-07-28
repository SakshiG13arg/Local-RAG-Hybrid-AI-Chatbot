import re


def clean_text(text: str) -> str:
    """
    Cleans extracted PDF text.
    """

    # Remove multiple spaces/newlines
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text