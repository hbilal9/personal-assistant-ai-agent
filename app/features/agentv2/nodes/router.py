
from langchain_core.output_parsers import PydanticOutputParser
from app.features.agentv2.chat import generate_response
from app.features.agentv2.schemas import AnalyzeMessageSchema
from app.features.agentv2.prompts import ANALYZE_MSG_PROMPT
from langchain.prompts import PromptTemplate

async def router_node(state):
    query = state["query"]
    parser = PydanticOutputParser(pydantic_object=AnalyzeMessageSchema)
    template = PromptTemplate.from_template(ANALYZE_MSG_PROMPT)
    res = await generate_response(template, parser, query)
    return {"tool": res.tool}
