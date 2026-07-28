from agents.agent_loop import run_agent_loop
from harness.state import AgentState
from agents.legacy import run_legacy


def run_pipeline(question, history, index, chunks, bm25, search_mode="auto", mode="multi_agent"):

    """
    Runs the complete multi-agent pipeline.
    """
    print("\n========== PIPELINE ==========")
    print("Starting Multi-Agent Pipeline")
    print("==============================\n")
    state = AgentState()
    state.search_mode = search_mode
    state.mode = mode

    state.question = question
    state.mode = mode

    if mode == "legacy":

        state = run_legacy(
            state,
            history,
            index,
            chunks,
            bm25
        )

    else:

        state = run_agent_loop(
            state,
            history,
            index,
            chunks,
            bm25
        )
    print("\n========== PIPELINE ==========")
    print("Pipeline Finished")
    print("==============================\n")

    return state
