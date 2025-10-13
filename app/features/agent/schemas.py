from pydantic import BaseModel

class SentEmailSchema(BaseModel):
  to_email: str
  subject: str
  email_body: str