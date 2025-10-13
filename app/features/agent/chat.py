from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from config import settings

llm = ChatOpenAI(
  api_key=settings.OPENROUTER_API_KEY,
  base_url="https://openrouter.ai/api/v1",
  model="openai/gpt-oss-20b:free"
)

async def generate_response(template: PromptTemplate, parser: PydanticOutputParser, query: str) -> PydanticOutputParser:
    chain = template | llm | parser
    return await chain.ainvoke({"query": query})
    