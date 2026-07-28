from config import MAX_AGENT_LOOPS


class Budget:

    def __init__(self):

        self.max_loops = MAX_AGENT_LOOPS

        self.current_loop = 0

    def consume(self):

        self.current_loop += 1

    def exceeded(self):

        return self.current_loop >= self.max_loops