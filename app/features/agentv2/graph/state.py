from typing import TypedDict, Annotated, List
from langchain_core.messages import AnyMessage

class GraphState(TypedDict):
    messages: Annotated[List[AnyMessage], lambda x, y: (x + y)[-5:]]
    query: str
    tool: str
