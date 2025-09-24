from fastapi import FastAPI, UploadFile, File, Form
from fastmcp import FastMCP
from server.document_ingestion import ingest_file
from server.query_handler import answer_query  
from server.model_manager import switch_model

app = FastAPI(title="FastMCP Document-Aware Query Assistant")
mcp = FastMCP("FastMCP Document-Aware Query Assistant")

# Register MCP tools
tools = [ingest_file, answer_query, switch_model]
for tool in tools:
    mcp.tool(tool)

@app.post("/ingest")
async def ingest_endpoint(file: UploadFile = File(...)):
    # You may need to adapt ingest_file to accept file-like objects
    content = await file.read()
    result = ingest_file(content, filename=file.filename)
    return {"result": result}

@app.post("/query")
async def query_endpoint(query: str = Form(...)):
    result = answer_query(query)
    return {"result": result}

@app.post("/switch-model")
async def switch_model_endpoint(model_name: str = Form(...)):
    result = switch_model(model_name)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    print("Starting FastMCP FastAPI server...")
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)

    
