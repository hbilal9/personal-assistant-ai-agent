from pydantic import BaseModel

class GreetMessageSchema(BaseModel):
  message: str

class SentEmailSchema(BaseModel):
  to_email: str
  subject: str
  email_body: str


class AnalyzeMessageSchema(BaseModel):
  tool: str