
from langchain_core.output_parsers import PydanticOutputParser
from app.features.agentv2.chat import generate_response
from app.features.agentv2.schemas import GreetMessageSchema, SentEmailSchema
from app.features.agentv2.prompts import GREETING_PROMPT, SENT_EMAIL_PROMPT
from langchain.prompts import PromptTemplate

async def greet_node(state):
    query = state["query"]
    parser = PydanticOutputParser(pydantic_object=GreetMessageSchema)
    template = PromptTemplate.from_template(GREETING_PROMPT)
    res = await generate_response(template, parser, query)
    return {"messages": [res.message]}

async def send_email_node(state):
    query = state["query"]
    parser = PydanticOutputParser(pydantic_object=SentEmailSchema)
    template = PromptTemplate.from_template(SENT_EMAIL_PROMPT)
    res = await generate_response(template, parser, query)
    print(res.email_body)
    # Here you would add the actual email sending logic
    return {"messages": [f"Email to {res.to_email} with subject '{res.subject}' has been sent."]}
