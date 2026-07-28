import time


class Metrics:

    def __init__(self):

        self.start = 0

        self.end = 0

    def start_timer(self):

        self.start = time.time()

    def stop_timer(self):

        self.end = time.time()

    def total_time(self):

        return self.end - self.start