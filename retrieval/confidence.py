def is_confident(
    distances,
    threshold
):
    """
    Checks whether the retrieved chunks
    are confident enough.
    """

    if len(distances) == 0:
        return False

    best_distance = distances[0]

    return best_distance < threshold
