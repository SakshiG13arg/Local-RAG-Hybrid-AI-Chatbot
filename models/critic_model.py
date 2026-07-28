from utils.model_router import call_model


from config import DEFAULT_MODEL

MODEL = DEFAULT_MODEL


def critic(
    prompt: str
) -> str:
    """
    Critic Model
    """

    return call_model(
    "DEFAULT_MODEL",
    prompt
)
