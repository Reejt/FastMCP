# Tool decorator for FastMCP

def tool(func):
    """Decorator to mark a function as an MCP tool."""
    func.is_mcp_tool = True
    return func
