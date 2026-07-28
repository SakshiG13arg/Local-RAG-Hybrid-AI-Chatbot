class AgentState:

    def __init__(self):

        self.question = ""

        self.plan = ""

        self.context = ""

        self.answer = ""

        self.review = ""

        self.used_web = False

        self.finished = False

        # current loop number
        self.iteration = 0

        # logs
        self.logs = []

        self.sources = []

        self.errors = []

        # optional future fields
        self.sources = []

        self.tool_used = None

        self.error = None

        self.search_mode = "auto"

        self.tool_trace = []

        self.sources = []

        self.mode = "multi_agent"
