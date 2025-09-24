from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Starting server...")
    # Run the server with http transport on port 8000
    mcp.run(transport="http", port=8000)
    print("Server stopped.")

