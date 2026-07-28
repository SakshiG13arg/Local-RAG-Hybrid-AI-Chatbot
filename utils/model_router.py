from ollama import chat


def call_model(model:str, prompt:str) -> str:
    """
    Generic Model Router

    Parameters
    ----------
    model : str
        Name of the Ollama model
        Examples:
            - "llama3"
            - "qwen2.5:3b"
            - "mistral"

    prompt : str
        Prompt sent to the model.

    Returns
    -------
    str
        Model response.
    """

    try:

        response = chat(
        model=model,
        messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
        options={
        "temperature": 0.2
    }
)

        return response["message"]["content"]

    except Exception as e:

        print("\n========== MODEL ERROR ==========")
        print(type(e).__name__)
        print(e)
        print("=================================\n")

        return "Sorry, the model could not generate a response."
