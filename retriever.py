from utils.tools import (
    search_pdf,
    search_web_tool
)


def retrieve(
    question,
    plan,
    search_mode,
    index,
    chunks,
    bm25
):
    """
    Retriever Agent
    Executes retrieval based on search mode.
    """

    context = ""
    web = None

    # -------------------------
    # Internet Only
    # -------------------------
    if search_mode == "internet_only":

        web = search_web_tool(question)

        return "", web

    # -------------------------
    # RAG Only
    # -------------------------
    if search_mode == "rag":

        context, _ = search_pdf(
            question,
            index,
            chunks,
            bm25
        )

        return context, None

    # -------------------------
    # Always RAG + WEB
    # -------------------------
    if search_mode == "rag_plus_web":

        context, _ = search_pdf(
            question,
            index,
            chunks,
            bm25
        )

        web = search_web_tool(question)

        return context, web

    # -------------------------
    # AUTO (Planner decides)
    # -------------------------

    plan = plan.lower()

    if "pdf" in plan or "both" in plan:

        context, use_web = search_pdf(
            question,
            index,
            chunks,
            bm25
        )

        if use_web:

            web = search_web_tool(question)

    elif "web" in plan:

        web = search_web_tool(question)

    return context, web