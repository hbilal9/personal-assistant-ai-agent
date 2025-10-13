from langchain.prompts import PromptTemplate
from .prompts import GREETING_PROMPT, SENT_EMAIL_PROMPT

GREETING_TEMPLATE = PromptTemplate(
input_variables=["query"],
template=GREETING_PROMPT
)

SENT_EMAIL_TEMPLATE = PromptTemplate(
input_variables=["query"],
template=SENT_EMAIL_PROMPT
)
