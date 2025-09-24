# Minimal FastMCP class for server usage

class FastMCP:
    def __init__(self, name):
        self.name = name
        self.tools = []

    def tool(self, func):
        self.tools.append(func)

    def run(self, transport="http", port=8000):
        print(f"Running {self.name} on {transport}://localhost:{port}")
        print(f"Registered tools: {[t.__name__ for t in self.tools]}")
        # Placeholder for actual server logic
        # You can expand this to start a real HTTP server, etc.
