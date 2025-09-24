# Handles document ingestion and parsing
from fastmcp import tool
from utils.file_parser import extract_text_from_file

documents = []

@tool
def ingest_file(file_path: str) -> str:
    try:
        content = extract_text_from_file(file_path)
        documents.append(content)
        return f"File '{file_path}' ingested successfully."
    except Exception as e:
        return f"Error ingesting file: {str(e)}"
