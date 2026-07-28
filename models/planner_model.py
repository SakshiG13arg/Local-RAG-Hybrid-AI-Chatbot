from utils.model_router import call_model


from config import PLANNER_MODEL

MODEL = PLANNER_MODEL


def planner(
    prompt: str
) -> str:
    """
    Planner Model
    """

    return call_model(
        MODEL,
        prompt
    )
