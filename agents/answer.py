from utils.prompts import build_prompt
from models.answer_model import generate_answer


def answer(question:str, context:str, history) -> str:
    """
    Answer Agent
    """

    conversation = ""

    for message in history[-10:]:

        role = message["role"]
        text = message["parts"][0]["text"]

        conversation += f"{role}: {text}\n"

    prompt = build_prompt(
        context=context,
        conversation=conversation,
        question=question
    )

    return generate_answer(prompt)
