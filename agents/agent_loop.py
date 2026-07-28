from agents.planner import plan
from agents.retriever import retrieve
from agents.answer import answer
from agents.critic import review
from harness.logger import log_step
from harness.gates import should_continue
from harness.budget import Budget


def run_agent_loop(state, history, index, chunks, bm25):
    budget = Budget()

    while not budget.exceeded():

        print(f"\n========== LOOP {state.iteration + 1} ==========\n")

        # --------------------
        # Planner
        # --------------------

        state.plan = plan(state.question)
        state.logs.append("Planner")

        state.plan = plan(state.question)
        log_step("Planner")
        print(state.plan)

        # --------------------
        # Retrieval
        # --------------------

        state.context, web = retrieve(
            state.question,
            state.plan,
            state.search_mode,
            index,
            chunks,
            bm25
        )
        state.logs.append("Retriever")

        if web:
            state.used_web = True
        log_step("Retriever")

        # --------------------
        # Answer
        # --------------------

        state.answer = answer(
            state.question,
            state.context,
            history
        )
        state.logs.append("Answer")
        history.append({
        "role": "model",
        "parts": [{"text": state.answer}]
})
        log_step("Answer")

        # --------------------
        # Critic
        # --------------------

        state.review = review(state.answer)
        state.critic = state.review
        state.logs.append("Critic")

        log_step("Critic")
        print(state.review)

        # --------------------
        # Stop Condition
        # --------------------

        if not should_continue(state.review):

            break

        state.iteration += 1
        budget.consume()

    return state
