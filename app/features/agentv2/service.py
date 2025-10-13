
from .graph.workflow import app

async def chat_handler(query: str):
    res = await app.ainvoke({"query": query, "messages": []})
    return res["messages"]
