from langchain_core.output_parsers import PydanticOutputParser
from .chat import generate_response
from .schemas import AnalyzeMessageSchema
from .templates import ANALYZE_MSG_TEMPLATE


async def analyze_message_service(query: str) -> AnalyzeMessageSchema:
    parser = PydanticOutputParser(pydantic_object=AnalyzeMessageSchema)
    return await generate_response(ANALYZE_MSG_TEMPLATE, parser, query)
    