from pydantic import BaseModel

class ClassificationRequest(BaseModel):
    text: str