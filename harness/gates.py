def should_continue(review: str) -> bool:

    if not review:
        return True

    review = review.upper().strip()

    return "GOOD" not in review
