from agents.answer import answer
from agents.retriever import retrieve


def run_legacy(
    state,
    history,
    index,
    chunks,
    bm25
):

    state.context, web = retrieve(
        state.question,
        "pdf",
        state.search_mode,
        index,
        chunks,
        bm25
    )

    state.answer = answer(
        state.question,
        state.context,
        history
    )

    return state
