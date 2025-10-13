from langchain.prompts import PromptTemplate
from .prompts import ANALYZE_MSG_PROMPT, GREETING_PROMPT, SENT_EMAIL_PROMPT

ANALYZE_MSG_TEMPLATE = PromptTemplate(
input_variables=["query"],
template=ANALYZE_MSG_PROMPT
)

GREETING_TEMPLATE = PromptTemplate(
input_variables=["query"],
template=GREETING_PROMPT
)

SENT_EMAIL_TEMPLATE = PromptTemplate(
input_variables=["query"],
template=SENT_EMAIL_PROMPT
)
