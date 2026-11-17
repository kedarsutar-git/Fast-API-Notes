'''
1. Path Parameters
A path parameter is a value that is part of the URL path.

Ex: 
/users/101

Here, 101 is part of the path and can represent the user's ID.

'''

from fastapi import FastAPI
app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"Userid":user_id}

'''
2. Why use Path Parameters?
Path parameters are normally used when identifying a specific resource.

For example:

/users/101
/products/500
/orders/2001
/videos/123

Think:
"Which exact resource do I want?"
'''



# 3. Multiple Path Parameters

from fastapi import FastAPI
app = FastAPI()
@app.get("/users/{user_id}/Items/{item_id}")
def get_items(user_id:int, item_id:int):
    return {
        "user_id":user_id,
        "item_id":item_id
    }



# 4. Query Parameters
# A query parameter comes after ? in the URL.

# Example:
# /items/?skip=0&limit=10
# are query parameters. Query parameters are key-value pairs separated by &

from fastapi import FastAPI
app = FastAPI()
@app.get("/items/")

def Get_items(Skip:int=0, limit:int = 13):
    return {
        "skip":Skip,
        "limit":limit
    }

# Request:
# GET /items/?skip=20&limit=5




'''
5. How does FastAPI know it's a Query Parameter?

@app.get("/items/{item_id}")
async def get_item(
    item_id: int,
    q: str | None = None
):


FastAPI sees:
item_id

inside:
/items/{item_id}

Therefore:
item_id → Path Parameter

But:
q

is not inside the URL path.


Therefore:
q → Query Parameter
'''



# 6. Path + Query Together

from fastapi import FastAPI
app = FastAPI()
@app.get("/users/{user_id}")

def get_user(user_id:int,q:str|None = None):
    return {
        "user_id":user_id,
        "search":q

    }

'''
Now request:
GET /users/101?q=python

FastAPI interprets it as:
Path parameter:
user_id = 101

Query parameter:
q = "python"

Response:
{
    "user_id": 101,
    "search": "python"
}
'''
from fastapi import FastAPI
from mockData import products

app = FastAPI()

def Products(id:int):
    for oneproduct in products:
        if oneproduct.get("id") == id:
            return oneproduct

    return {"Status":"Product is not found"}

    

    
