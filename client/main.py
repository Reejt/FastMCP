
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
        result = subprocess.run(["gemini", query], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error calling Gemini CLI: {str(e)}"

async def main():
    await call_ingest_file("example.txt")
    await call_answer_query("What is in the document?")
    await call_switch_model("gemini")
    # Example Gemini CLI usage
    gemini_result = call_gemini_cli("What is in the document?")
    print(f"Gemini CLI result: {gemini_result}")

if __name__ == "__main__":
    asyncio.run(main())
