from utils.prompts import load_prompt
from models.planner_model import planner


def plan(question: str) -> str:
    prompt = (
        load_prompt("planner")
        + "\n\nUser Question:\n"
        + question
    )

    return planner(prompt)
