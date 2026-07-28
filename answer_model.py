from utils.model_router import call_model


from config import ANSWER_MODEL

MODEL = ANSWER_MODEL


def generate_answer(
    prompt: str
) -> str:
    """
    Main Answer Model
    """

    return call_model(
    "qwen2.5:3b",
    prompt
)