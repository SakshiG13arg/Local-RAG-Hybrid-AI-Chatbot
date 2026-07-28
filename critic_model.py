from utils.model_router import call_model


from config import CRITIC_MODEL

MODEL = CRITIC_MODEL


def critic(
    prompt: str
) -> str:
    """
    Critic Model
    """

    return call_model(
    "qwen2.5:3b",
    prompt
)