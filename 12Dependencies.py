'''
Think of a dependency as a reusable helper function (without an @app.get(...) 
decorator) that can accept the exact same request parameters (query params, headers, cookies, etc.)
 as a normal route
'''

# How it work:
'''
Instead of repeating the same parameters and logic across multiple endpoints, 
you define a dependency once and wire it in with Depends()

'''

from typing import Annotated
from fastapi import Depends,FastAPI

app = FastAPI()

def commen_parameters(q:str | None = None, skip: int = 0, limit: int = 100):
    return {"q":q, "skip":skip, "limit":limit}

CommonsDep = Annotated[dict, Depends(commen_parameters)]

@app.get("/users/")
def getuser(commons:CommonsDep):
    return commons

@app.get("/item/")

def get_items(commons:CommonsDep):
    return commons

'''
And it has the same shape and structure that all your path operation functions have.
You can think of it as a path operation function without the "decorator" 
(without the @app.get("/some-path")).
And it can return anything you want.

In this case, this dependency expects:

An optional query parameter q that is a str.
An optional query parameter skip that is an int, and by default is 0.
An optional query parameter limit that is an int, and by default is 100.
'''

# Example:

from fastapi import Depends,FastAPI
from typing import Annotated

def Commonproperty(id:int, name:str, price:int):
    return {
        "id":id,
        "name":str,
        "price":int
    }

CommonDep = Annotated[dict, Depends(Commonproperty)]

app = FastAPI()

@app.get("/user/")
async def get_user(common:CommonsDep):
    return common
# /user/?q=kedar&skip=10&limit=202


@app.get("/item/")
async def get_product(common:CommonsDep):
    return common

# /item/?q=python&skip=10&limit=20


# Notice you pass common_parameters to Depends() without parentheses—you do not call it yourself
# When a request hits /items/ or /users/, FastAPI extracts q, skip, and limit from the URL query string and calls


# Very Important: Don't Call the Function Yourself
'''

1.Wrong:

Depends(Commonproperty())  # call the function now 


2.correct:
Depends(Commonproperty)

'''

'''
Depends(Commonproperty)
             │
             ▼
        FastAPI gets
        the function
             │
             ▼
     Request arrives
             │
             ▼
 FastAPI calls function
             │
             ▼
       Gets result
             │
             ▼
 Gives result to endpoint
'''





# Request Flow:
'''
uppose the client sends:

GET /items/?q=python&skip=10&limit=20



Client
  │
  │ GET /items/?q=python&skip=10&limit=20
  ▼
FastAPI
  │
  ▼
Sees Depends(common_parameters)
  │
  ▼
Calls common_parameters()
  │
  ├── q = "python"
  ├── skip = 10
  └── limit = 20
  │
  ▼
Returns dictionary
  │
  ▼
commons = {
    "q": "python",
    "skip": 10,
    "limit": 20
}
  │
  ▼
read_items(commons)
  |
  ▼
Response
'''


#  Annotated — What Is It?

from typing import Annotated

commons: Annotated[dict, Depends(Commonproperty)]

'''
Think of Annotated as:
"This variable has this type, plus some additional information."


# For example 1:

name: Annotated[str, something]

means:

name
 │
 ├── Type = str
 │
 └── Extra metadata = something

 

# For example 2:

commons: Annotated[dict, Depends(common_parameters)]

Means:

commons
 │
 ├── type → dict
 │
 └── dependency → common_parameters
'''


# Old Style vs Annotated


# 1. Older/non-`Annotated` style

from fastapi import FastAPI

app = FastAPI()

async def read_item(common:dict = Depends(commen_parameters)):
    return common


# New Style (Annotated)

from fastapi import Depends,FastAPI
from typing import Annotated

app = FastAPI()

async def Commoninfo(id:int, name: str ,price: int):
    return {
        "id":id,
        "name":name ,
        "price":price

    }

commonDep = Annotated[dict, Depends(Commoninfo)]

@app.get("/user/")

async def get_user(common: commonDep):
    return common

async def get_product(common: commonDep):
    return common




