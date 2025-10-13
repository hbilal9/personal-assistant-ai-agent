from langchain_core.output_parsers import PydanticOutputParser
from .chat import generate_response
from .schemas import AnalyzeMessageSchema, SentEmailSchema, GreetMessageSchema
from .templates import ANALYZE_MSG_TEMPLATE, GREETING_TEMPLATE, SENT_EMAIL_TEMPLATE


async def analyze_message_service(query: str) -> AnalyzeMessageSchema:
    parser = PydanticOutputParser(pydantic_object=AnalyzeMessageSchema)
    return await generate_response(ANALYZE_MSG_TEMPLATE, parser, query)

async def greet_service(query: str) -> str:
    parser = PydanticOutputParser(pydantic_object=GreetMessageSchema)
    res = await generate_response(GREETING_TEMPLATE, parser, query)
    return res.message

async def sent_email_service(query: str) -> str:
    parser = PydanticOutputParser(pydantic_object=SentEmailSchema)
    res = await generate_response(SENT_EMAIL_TEMPLATE, parser, query)
    print("email body: ", res.email_body)
    return f"Email to {res.to_email} with subject {res.subject} has been sent."

async def perform_action_service(query: str, action: str):
    if action == "greet":
        return await greet_service(query)
    elif action == "send_email":
        return await sent_email_service(query)


async def chat_handler(query: str):
    action = await analyze_message_service(query)
    return await perform_action_service(query, action.tool)
