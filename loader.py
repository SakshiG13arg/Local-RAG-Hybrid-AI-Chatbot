import pdfplumber


def load_pdf(file_path: str) -> str:
    """
    Reads a PDF file and returns extracted text.
    """

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()