# 1. First, remember Request Body
# Previously, we created a Pydantic model:

from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


# Then:
app = FastAPI
@app.post("/items")
async def create_item(item: Item):
    return item


# The JSON request could be:
{
    "name": "Laptop",
    "price": 75000,
    "description": "Gaming laptop"
}


# But currently, price: float only tells FastAPI/Pydantic the type.


# What if we want to say:
# Price must be greater than 0.

# That's where Field() comes in.




# What is field()

# Example:

from pydantic import BaseModel, Field
class Item(BaseModel):
    name : str
    price : float = Field(gt=0)


# means: Price must be a floating-point number.and Price must be greater than 0
# SO:

'''
{
    "name": "Laptop",
    "price": 75000
}
Valid



{
    "name": "Laptop",
    "price": -500
}
invalid : becouse of price is less then 0

'''

# 4. Why do we need Field()?

# Think about the diff 

'''
1. withot Field()

'''
class Item(BaseModel):
    price: float

# This says:
'''
price
 ↓
must be a float

'''



'''
2. With field

'''
class Item(BaseModel):
    price: float = Field(gt=0)

# Now :

'''
price
 ↓
must be a float
 ↓
must be > 0

'''

# 5. Important Field() Validation

Field(gt=0) # Greater then
Field(ge=0) # Greater the or equal to
Field(lt=100)  # Less than.
Field(le=100)  # Less than or equal to.


# For Example 
class Product(BaseModel):
    price : float = Field(gt=0)
    discount : float = Field(ge=0,le=100)

'''
price
  > 0

discount
  >= 0
  <= 100
'''


# 6. Field() with String Validation
# You can also use Field with string 

# For example:
class User(BaseModel):
    name : str = Field(min_length=3, max_length=20)

# This means 
'''
        name 
         ↓
 minimum 3 characters
 maximum 20 characters

SO:
{
    "username": "Kedar"
}
Valid

but 
{
    "username": "Ke"
}

invalid : becouse it has fewer then 3 characters

'''

# 7. Field() with Optional Fields

class User(BaseModel):
    description: str | None = Field(
    default=None,
    title="The description of the item",
    max_length=300
)

description: str | None # description can be: str or None

default=None  # makes it optional.

max_length=300 # maximum 300 characters



# 8 Complete Example
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50
    )

    description: str | None = Field(
        default=None,
        max_length=300
    )

    price: float = Field(
        gt=0,
        description="The price must be greater than zero"
    )

    tax: float | None = Field(
        default=None,
        ge=0
    )

'''
Now our rules are:

name
 ├── minimum 3 characters
 └── maximum 50 characters

description
 └── maximum 300 characters

price
 └── must be > 0

tax
 └── must be >= 0
'''





'''
13. Field() vs Query() vs Path() vs Body():

| Function   | Used for |

| Query()    | Query parameters |
| Path()     | Path parameters  |
| Body()     | Request body     |
| Field()    | Fields inside Pydantic models |
'''


# 14. Very Easy Mental Model
'''
URL
│
├── /items/{item_id}
│          │
│          └── Path()
│
├── ?limit=10
│      │
│      └── Query()
│
└── JSON Body
       │
       └── Pydantic Model
                │
                └── Field()

SO:
Field() = validation and metadata for a field inside your Pydantic model.
'''



# 15. Field() with Annotated
# The current FastAPI documentation recommends using Annotated when possible. FastAPI

# For example:
from typing import Annotated
from pydantic import BaseModel, Field

class Item(BaseModel):
    price: Annotated[
        float,
        Field(gt=0)
    ]


# However, you'll commonly see the simpler form:

class Item(BaseModel):
    price:float = Field(gt=0)

# Both express the validation; for your current learning stage, understand the second form first.




# 16. json_schema_extra
# Field() can also provide extra JSON Schema information.

class Item(BaseModel):
    name: str = Field(
        json_schema_extra={
            "example": "Gaming Laptop"
        }
    )

