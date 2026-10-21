
from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None



class CustomerUpdate(BaseModel):
    name: str
    email: str
    phone: str | None = None

