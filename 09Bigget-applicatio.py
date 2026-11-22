# Bigger Applications - Multiple Files


# 1. Why do we need Bigger Applications?
# When you start learning FastAPI, you might write:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello"}

@app.get("/users")
async def users():
    ...

@app.get("/tasks")
async def tasks():
    ...

@app.post("/tasks")
async def create_task():
    ...

@app.post("/login")
async def login():
    ...
    '''
This works.

But imagine your real AI backend has:

100+ API endpoints
Authentication
Users
Tasks
Chat
RAG
Documents
AI models
Payments
Database
Admin

Putting everything into:
main.py

would become extremely difficult to maintain.

So we divide the application into multiple files.
    '''

# Example File structure
'''
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py




.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
'''

'''
What is __init__.py
__init__.py tells Python that the directory should be treated as a Python package.

# You can import the main:

from app import main


# You can import the user
from app.routers import users

'''

# What is APIRouter:
'''
FastAPI() creates your main application. APIRouter() organizes related API 
endpoints into separate groups. include_router() connects those groups to the 
main application.



4.2 Why do we need it?

Imagine building a Task Management application with these APIs:

Feature          API endpoints
------------------------------------------------
Authentication   /auth/login, /auth/register
Users            /users, /users/me
Tasks            /tasks, /tasks/{task_id}
Chat             /chat, /chat/history
Documents        /documents, /documents/upload

We can organize them like this:

backend/
│
├── main.py
│
└── routers/
    ├── auth.py
    ├── users.py
    ├── tasks.py
    ├── chat.py
    └── documents.py

Each router file handles a particular feature.

For example:

- "auth.py" handles login and registration.
- "users.py" handles user-related operations.
- "tasks.py" handles task-related operations.
- "chat.py" handles chatbot operations.


This makes the project easier to maintain, test, debug, and expand.


'''

# Example 

from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_users():
    return {
        "users": ["Kedar", "Rahul", "Amit"]
    }


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id
    }


# We use router.get() instead of app.get() because this 
# file registers routes with an APIRouter object.


# Now connect it to main.py

# from fastapi import FastAPI
# from app.routers import users
# app = FastAPI()

# app.include_router(users.router)

'''

# How it works:

main.py
   │
   │ include_router()
   ▼
users.router
   │
   ├── GET /users
   │
   └── GET /users/{user_id}

SO 
app.include_router(users.router)

means:

"FastAPI, include all the routes from this router in my application."

'''

# 8. Real Task Management project
# For your Task Management backend, I recommend a structure like:
'''
task-management-app/
│
├── app/
│   │
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── tasks.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── auth.py
│       └── task.py
│
├── .env
├── requirements.txt
└── README.md
'''



# 11. prefix

# prefix means a common starting path that FastAPI adds to every 
# endpoint inside a router.

# Suppose your router contains

# Without Prefix:

router = APIRouter()


@router.get("/tasks")
async def get_tasks():
    ...


@router.get("/tasks/{task_id}")
async def get_task(task_id: int):
    return task_id


# with Prefix:
router = APIRouter(prefix="/tasks")


@router.get("/")
async def get_tasks():
    return 


@router.get("/{task_id}")
async def get_task(task_id: int):
    return task_id

    

from fastapi import APIRouter

router = APIRouter(prefix="/tasks")


@router.get("/")
async def get_tasks():
    return {
        "tasks": [
            "Learn FastAPI",
            "Learn PostgreSQL"
        ]
    }


@router.get("/{task_id}")
async def get_task(task_id: int):
    return {
        "task_id": task_id
    }


@router.post("/")
async def create_task():
    return {
        "message": "Task created"
    }



# 13. What does tags do?

'''
We can write:

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

The tags organize your API in Swagger/OpenAPI documentation.


Without tags
Endpoints may appear together without meaningful grouping.


With tags
Open:
http://127.0.0.1:8000/docs
Tasks

GET    /tasks/
GET    /tasks/{task_id}
POST   /tasks/

'''


# responses

router = APIRouter(
    prefix="/tasks",
    responses={
        404: {
            "description": "Task not found"
        }
    }
)

# responses documents the error. It doesn't automatically create the error.


