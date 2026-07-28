from evaluation.chunking_eval import evaluate_chunking
from retrieval.bm25 import build_bm25

from utils.memory import (
    add_to_history,
    get_history,
    clear_history
)
from harness.pipeline_harness import run_pipeline

print("=" * 50)
print("Hybrid AI Tutor Chatbot")
print("=" * 50)

history = clear_history()

index = None
chunks = None
bm25 = None

choice = input(
    "Do you want to use a PDF? (y/n): "
).lower()

if choice == "y":

    pdf_path = input(
        "Enter PDF path: "
    )

    if not pdf_path.lower().endswith(".pdf"):

        print("Please provide a PDF file.")
        exit()

    try:

        print("\nLoading PDF...\n")

        from ingestion.pipeline import ingest

        result = ingest(pdf_path)

        index = result["index"]
        chunks = result["chunks"]
        text = result["text"]

        if not text.strip():

            print("PDF contains no readable text.")
            exit()

        evaluate_chunking(text)

        print(f"\nTotal Chunks: {len(chunks)}")

        bm25 = build_bm25(chunks)

        print("\nPDF Ready!\n")

    except FileNotFoundError:

        print("PDF not found.")
        exit()

    except Exception as e:

        print(e)
        exit()

else:

    print("\nRunning in General AI Mode.\n")

# ---------------------------------------
# Chat Loop
# ---------------------------------------

while True:

    question = input("You: ")

    if question.lower() == "exit":

        print("\nGoodbye!")
        break

    if not question.strip():

        continue

    add_to_history(
        history,
        "user",
        question
    )


    state = run_pipeline(
        question,
        get_history(history),
        index,
        chunks,
        bm25,
        search_mode="auto",
        mode="multi_agent"
    )

    print("\nBot:", state.answer)

    print()

    add_to_history(
        history,
        "model",
        state.answer
    )
