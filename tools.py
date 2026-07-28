from retrieval.hybrid import hybrid_search
from utils.web_search import search_web


def search_pdf(
    question,
    index,
    chunks,
    bm25
):
    """
    Searches the local knowledge base.
    """

    return hybrid_search(
        question,
        index,
        chunks,
        bm25
    )


def search_web_tool(question):
    """
    Searches the web.
    """

    return search_web(question)