# Minimal FastMCP Client class

class Client:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def __repr__(self):
        return f"<FastMCP Client: {self.base_url}>"
