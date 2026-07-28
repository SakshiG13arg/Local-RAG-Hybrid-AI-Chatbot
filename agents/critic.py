from models.critic_model import critic


def review(answer: str) -> str:

    prompt = f"""
You are a critic.

Review the following answer.

If it is correct and complete, reply ONLY:

GOOD

Otherwise explain what should be improved.

Answer:
{answer}
"""

    return critic(prompt)
