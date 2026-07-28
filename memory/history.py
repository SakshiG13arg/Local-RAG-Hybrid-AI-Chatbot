def add_to_history(history, role, text):
    """
    Adds one message to the conversation history.
    """

    history.append(
        {
            "role": role,
            "parts": [
                {
                    "text": text
                }
            ]
        }
    )


def get_history(history):
    """
    Returns the conversation history.
    """

    return history


def clear_history():
    """
    Creates a new empty conversation.
    """

    return []
