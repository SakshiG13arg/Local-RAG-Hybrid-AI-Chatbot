import os


PROMPT_DIR = "prompts"


def load_prompt(name: str) -> str:
    """
    Loads a prompt template from prompts/.
    """

    path = os.path.join(
        PROMPT_DIR,
        f"{name}.md"
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def build_prompt(
    context,
    conversation,
    question
):
    """
    Legacy prompt builder.
    """

    return f"""
You are an AI Tutor.

Use ONLY the context below.

Context:
{context}

Conversation:
{conversation}

Question:
{question}

Answer:
"""