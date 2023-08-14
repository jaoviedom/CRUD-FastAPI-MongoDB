from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = 0
    status: str = 'Pending'