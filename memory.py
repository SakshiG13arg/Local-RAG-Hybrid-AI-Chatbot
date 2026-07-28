def clear_history():
    return []


def add_to_history(history, role, text):

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

    return history