# What is a Response body 
'''
When the client sends a request your FastAPI server processes it and 
sends data back to the client
That return data is the response body


'''

from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")

def Hello():
    return {
        "message":"Hello Kedar"
    }

# The client receives :
{
    "message":"Hello Kedar" 
}

# SO:
'''
                Client
                │
                │ GET /hello
                ▼
                FastAPI
                │
                │ process
                ▼
                Response Body
                {
                    "message": "Hello Kedar"
                }
'''

# What is Response Model:

'''
A response model tells FastAPI:

"This is the structure of data that my API should return."

FastAPI can use a Pydantic model as the response model. 
It uses that model to validate, document, serialize, and 
importantly filter the returned data.


'''

# Example 

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name : str
    age: int


app = FastAPI()
@app.get("/User",response_model=User)

def get_user():
    return {
        "id":1,
        "name":"kedar",
        "age":21

    }

# The Response will be:

{
    "id":1,
    "name":"kedar",
    "age":21
}

# 3. Why do we need a Response Model?

# Suppose your database contains:

'''
username
email
age
password
credit_card
internal_id

'''

# But you only want to send:

'''
username
email
age
'''
# You can create 
class Userout(BaseModel):
    username : str
    emial : str
    age : int

app = FastAPI()

@app.get("/User",response_model=Userout)

def UserInfo():
    return {
        "username" : "Kedar",
        "email" : "kedar.sutar400@gmail.com",
        "age": 22,
        "password":"pass@20043",
        "credit_card":"1234"

    }

# FastAPI filters the response according to UserOut.

# Client receives only:

{
    "username": "kedar",
    "email": "kedar.sutar400@gmial.com",
    "age": 22
}


# 5. Response Model with a List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Users(BaseModel):
    username : str
    email : str

@app.get("/user",response_model=Users)
def Userinfo():
    return [{
            "username":"kedar",
            "emial":"kedar.sutar400@gmail.com"
 },
 {
    "username":"kishor",
    "emial":"kishorsutar552003@gmail.com"
}]



# 8. Security Example — Password

# Suppose your input model is:

class UserIn(BaseModel):
    username: str
    emial: str
    password: str

# You shouldn't return the password.

# Create a separate output model:

class UserOut(BaseModel):
    username: str
    email: str

@app.post("/users", response_model=UserOut)
async def create_user(user: UserIn):
    return user

# input:

{
    "username": "kedar",
    "email": "kedar@example.com",
    "password": "secret123"
}

# Your Python function receives the password.

# But the API response becomes:

{
    "username": "kedar",
    "email": "kedar@example.com"
}


# 9. Response Model = API Contract
# This is a very useful way to think about it.

'''
             Backend
                │
                │
        ┌───────▼────────┐
        │ response_model │
        │     UserOut    │
        └───────┬────────┘
                │
                ▼
             Client
'''
'''
It tells the frontend:

"This is the structure of the data you can expect from this API."

FastAPI also uses the response model to generate the response schema in OpenAPI, 
which appears in the automatic API documentation and can be used by client-generation tools. 

'''

# 10. What happens internally?

@app.get("/user", response_model=UserOut)
async def get_user():
    return {
        "username": "Kedar",
        "email": "kedar@example.com",
        "password": "secret"
    }

'''
Function returns data
        ↓
FastAPI
        ↓
Pydantic / response model
        ↓
Validate + serialize + filter
        ↓
JSON Response
        ↓
Client

'''

# Client gets:
{
    "username": "Kedar",
    "emial":"kedar.sutar400@gmail.com"

}




# HTTP Status code

'''
A status code tells the client what happened with the request.

'''
# FastAPI lets you specify the status code using:
status_code = 201
# in the path operation decorator


# 1. Default Status Code — 200
# For many successful requests, FastAPI uses:

# 200 ok

app = FastAPI()
@app.get("/")
def get_user():
    return {"message":"Users found"}

# Response:
# HTTP 200 OK



# 2. Created 201
# When you're creating a new resource, 201 is commonly used.

from fastapi import FastAPI

app = FastAPI()
@app.post("/Creates",status_code=201)

def create_user():
    return {"message":"Users found"}

# Response:
# HTTP 201 Created



# Better way — status.HTTP_201_CREATED

# You can use

from fastapi import FastAPI, status

app = FastAPI()


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user():
    return {
        "message": "User created"
    }



# Status code

'''
| Code | Meaning | Common use |

| `200` | OK                    | Successful GET |
| `201` | Created               | Successful POST |
| `204` | No Content            | Successful DELETE/update with no body |
| `400` | Bad Request           | Invalid client request |
| `401` | Unauthorized          | Authentication required/failed |
| `403` | Forbidden             | Authenticated but not allowed |
| `404` | Not Found             | Resource doesn't exist |
| `409` | Conflict              | Duplicate/conflicting resource |
| `422` | Unprocessable Content | Validation error |
| `500` | Internal Server Error | Server-side failure |
'''



# Real Task Management API

from fastapi import FastAPI
from pydantic import BaseModel

app  = FastAPI()

class Taskcreate(BaseModel):
    title : str
    description: str |None = None

class Taskout(BaseModel):
    id :int
    title: str
    description: str |None = None

@app.post("/createuser",response_model=Taskout, status_code = status.HTTP_201_CREATED)
def create_task(task:Taskcreate):
    new_task = {
        "id": 1,
        "title": task.title,
        "description": task.description
    }

    return new_task


'''
Client sends:

{
    "title": "Learn FastAPI",
    "description": "Study response models"
}

# Fast API:
Request Body
     ↓
TaskCreate
     ↓
Your function
     ↓
new_task
     ↓
TaskOut
     ↓
JSON Response



Response:
HTTP 201 Created

{
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Study response models"
}
'''

# The complete picture

'''
                    CLIENT
                       │
                       │ POST /tasks
                       │
                       │ JSON
                       ▼
              ┌─────────────────┐
              │  Request Body   │
              │   TaskCreate    │
              └────────┬────────┘
                       │
                       ▼
                  FastAPI
                       │
                       ▼
                 Your Function
                       │
                       ▼
                TaskOut Model
                       │
                       ▼
              Response Filtering
                       │
                       ▼
             HTTP 201 Created
                       │
                       ▼
                    CLIENT
'''

