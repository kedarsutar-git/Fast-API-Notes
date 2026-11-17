from pydantic import BaseModel

class productsDTO(BaseModel):
    id: int
    name: str
    count: int
    price: int

