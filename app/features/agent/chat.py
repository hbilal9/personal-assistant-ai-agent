from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from config import settings

template = PromptTemplate(
    template="""
    "You are a helpful assistant"
    """,

    input_variables=["query"]
    )
parser = StrOutputParser()

llm = ChatOpenAI(
  api_key=settings.OPENROUTER_API_KEY,
  base_url="https://openrouter.ai/api/v1",
  model="openai/gpt-oss-20b:free"
)

async def generate_response(query: str):
    chain = template | llm | parser
    return await chain.ainvoke({"query": query})
    