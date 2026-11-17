'''
A request body is data that the client sends to your API, usually as JSON. 
FastAPI uses Pydantic models to define, parse, validate, and document that data.



1. What is a Request Body?
Suppose your frontend wants to create a new product.

It Sends:

{
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 75000,
    "tax": 5000
}
This JSON is the request body



Think of an HTTP request like:

Client
   │
   │  POST /items/
   │
   │  JSON Body
   ▼
FastAPI
   │
   ▼
Pydantic Model
   │
   ▼
Validation
   │
   ▼
Your Python function
'''



# 2. Request Body vs Path vs Query
'''
Suppose we have:
PUT /items/101?q=update

and JSON:

{
    "name": "Laptop",
    "price": 75000
}

There are three different places where data comes from:

PUT /items/101?q=update
     │       │
     │       └── Query parameter
     │
     └── Path parameter

JSON body
{
    "name": "Laptop",
    "price": 75000
}
       ↑
   Request body
'''

# 3. Why do we use Pydantic?

'''
FastAPI recommends using Pydantic models to declare request bodies.

Pydantic is a python library for data validation 
By defining models that inherit from BaseModel, developers can automatically validate, 
parse, and serialize data, ensuring it conforms to specified types and constraints before processing. 
'''
from pydantic import BaseModel
# Then create a model 

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# We're creating a Pydantic model called Item.
# Then:
'''
name: str
name → required → string


description: str | None = None
description → optional → string or None


price: float
price → required → float


tax: float | None = None
tax → optional → float or None
'''


# 4. Complete FastAPI Example 
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description:str|None = None
    price:float
    tax:float|None = None


app = FastAPI()
@app.post("/items/")
def create_item(item:Item):
    return item

'''
Item inherits from Pydantic's BaseModel.

This tells FastAPI:
"Item describes the structure of the request body."

'''
item = Item(name= "Laptop", price=75000)
# item now holds:

Item(
    name="Laptop",
    description=None,
    price=75000.0,
    tax=None
)


# 1. Why inherit BaseModel?

# means: “Create Item with all the normal behavior of a Pydantic model.”
# Inheritance lets Item reuse BaseModel’s capabilities while adding its own fields (name, price, etc.).
# A plain class would only store data:
class Item:
    name: str
    price: float

# It would not automatically validate input, convert types, return useful validation errors, 
# create API documentation, or safely serialize data.

# BaseModel provides those features.


# 2. Client Sends JSON
'''
# The client sends

{
    "name": "Gaming Laptop",
    "description": "RTX 3050 laptop",
    "price": 75000,
    "tax": 5000
}


FastAPI receives it.
JSON
 ↓
Pydantic
 ↓
Item object
 ↓
create_item(item)

item.name
item.description
item.price
item.tax

are available directly.
'''


# 3. FastAPI Automatically validates 
'''
8. FastAPI Automatically Validates
This is one of the biggest advantages.

Suppose the client sends:

{
    "name": "Laptop",
    "price": "hello"
}

But Your models says:
price:float

FastAPI/Pydantic detects that the data doesn't satisfy the declared model and 
returns a validation error rather than giving your function an invalid Item. 
The official docs specifically describe JSON parsing, type conversion when appropriate, 
validation, and clear error reporting.


              Request JSON
                   │
                   ▼
              Parse JSON
                   │
                   ▼
           Convert types if needed
                   │
                   ▼
             Validate data
                   │
          ┌────────┴────────┐
          │                 │
       Valid              Invalid
          │                 │
          ▼                 ▼
    Item object        Validation error
          │
          ▼
    Your function
'''

# 9. Required vs Optional Fields

'''
Required:

name: str
price: float

so this is valid :

{
    "name": "Laptop",
    "price": 75000
}


But this is missing price:
{
    "name": "Laptop"
}

So it doesn't satisfy the model.

Optional:

description: str | None = None 
and 
tax: float | None = None



Therefore this is also valid:
{
    "name": "Laptop",
    "price": 75000
}


'''


# 13. Accessing the Body Inside the Function

from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    name:str
    des : str|None = None
    price: float
    tax:int

app =  FastAPI()
@app.post("/items/")

def create_item(item:Item):
    return {
        "name":item.name,
        "price":item.price

    }

# if Client sends
{
    "name": "RTX Laptop",
    "price": 80000
}

# then 
item.name   # output : RTX Laptop


# 14. model_dump():
# item_dict = item.model_dump()

'''
model_dump() is the primary Pydantic method for converting a validated model 
instance into a standard Python dictionary,

'''
# Example:
from pydantic import BaseModel
class User(BaseModel):
    id : int
    name : str

user = User(id=1, name = "Kedar")
print(user)   # print the validated model instance

print(user.model_dump())  # print the standard Python dictionary


# Request body + path parameters

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


# Request body + path + query parameters
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result