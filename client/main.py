
# FastMCP client with FastAPI integration and Gemini CLI
import asyncio
import httpx
from fastmcp import Client
import subprocess

BASE_URL = "http://localhost:8000"

async def call_ingest_file(file_path: str):
    async with httpx.AsyncClient() as client:
        with open(file_path, "rb") as f:
            files = {"file": (file_path, f, "application/octet-stream")}
            response = await client.post(f"{BASE_URL}/ingest", files=files)
        print("ingest_file result:", response.json())

async def call_answer_query(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/query", data={"query": query})
        print("answer_query result:", response.json())

async def call_switch_model(model_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/switch-model", data={"model_name": model_name})
        print("switch_model result:", response.json())

# Gemini CLI integration
def call_gemini_cli(query: str) -> str:
    try:
        # Replace 'gemini' with the actual CLI command if different
        result = subprocess.run([r"C:\Users\Reejit\npm-global\gemini.cmd", query], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error calling Gemini CLI: {str(e)}"

async def main():
    # Interactive Gemini CLI and MCP routing
    query = input("Enter your query for Gemini CLI: ")
    gemini_result = call_gemini_cli(query)
    print(f"Gemini CLI result: {gemini_result}")

    # Simple routing logic based on keywords
    if "switch model" in query.lower():
        model_name = query.split("switch model",1)[-1].strip() or "gemini"
        await call_switch_model(model_name)
    elif "ingest" in query.lower():
        # Example: 'ingest filename.txt'
        parts = query.split()
        if len(parts) > 1:
            file_path = parts[-1]
            await call_ingest_file(file_path)
        else:
            print("Please specify a file to ingest.")
    else:
        await call_answer_query(query)

if __name__ == "__main__":
    asyncio.run(main())
