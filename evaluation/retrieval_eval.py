def evaluate_retrieval(
    questions,
    retriever
):

    hits = 0

    for item in questions:

        question = item["question"]
        expected_keyword = item["expected_keyword"].lower()

        chunks = retriever(question)

        if any(
            expected_keyword in chunk.lower()
            for chunk in chunks
        ):
            hits += 1


    hit_rate = (
        hits / len(questions)
    ) * 100


    return {
        "hit_rate": hit_rate,
        "correct": hits,
        "total": len(questions)
    }
