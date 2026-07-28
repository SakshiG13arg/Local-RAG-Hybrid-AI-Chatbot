def evaluate_answer(
    answer,
    expected_answer
):

    answer = answer.lower()
    expected_answer = expected_answer.lower()


    score = 1 if expected_answer in answer else 0


    return {
        "correct": score,
        "answer_length": len(answer.split())
    }
