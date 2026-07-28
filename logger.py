from datetime import datetime


def log_step(step):

    print()

    print("=" * 50)

    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] {step}"
    )

    print("=" * 50)


def log_info(message):

    print(message)


def log_error(message):

    print()

    print("ERROR")

    print(message)

    print()