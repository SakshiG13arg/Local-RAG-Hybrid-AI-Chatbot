import time


def benchmark(function, *args):

    start = time.time()

    result = function(*args)

    end = time.time()

    print(
        f"Execution Time: {end-start:.2f}s"
    )

    return result
