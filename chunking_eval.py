def evaluate_chunking(
    text,
    chunks
):

    print()

    print("=" * 40)

    print("Chunking Evaluation")

    print("=" * 40)

    print(f"Characters : {len(text)}")

    print(f"Chunks     : {len(chunks)}")

    if len(chunks):

        avg = sum(
            len(c)
            for c in chunks
        ) / len(chunks)

        print(f"Average Chunk Size : {avg:.2f}")

    print("=" * 40)