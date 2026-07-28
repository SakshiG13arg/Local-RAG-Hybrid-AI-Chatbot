from utils.model_router import call_model


from config import DEFAULT_MODEL

MODEL = DEFAULT_MODEL


def generate_answer(
    prompt: str
) -> str:
    """
    Main Answer Model
    """

    return call_model(
    "DEFAULT_MODEL",
    prompt
)
