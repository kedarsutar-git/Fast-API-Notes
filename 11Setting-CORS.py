# 1. What are Settings?
# Imagine you have this code:
DATABASE_URL = "postgresql://postgres:password@localhost/mydb"

SECRET_KEY = "my-super-secret-key"


# This is problem 
# Why ?

# Because configuration and secrets are now directly inside your source code.

# Instead, we want:

'''
Python code
     │
     ▼
Settings object
     │
     ▼
Environment variables
     │
     ├── DATABASE_URL
     ├── SECRET_KEY
     ├── API_KEY
     └── DEBUG


'''

# 2. What is an Environment Variable?
# An environment variable is a value stored outside your Python code and made available to your 
# application through the operating system.

# For Example 
'''
APP_NAME=Task Management API
ADMIN_EMAIL=admin@example.com
DATABASE_URL=postgresql://...
SECRET_KEY=abc123

'''

# Why use environment variables?

# Suppose you have three environments:
'''
Development
Testing
Production


Development:
DATABASE_URL=postgresql://localhost/dev_db

Testing:
DATABASE_URL=postgresql://localhost/test_db

Production:
DATABASE_URL=postgresql://production-server/prod_db



Your Python code doesn't need to change.

Only the environment variables change.

'''

# 4. Why do we need Pydantic Settings?

# Without Pydantic Settings, you could manually read environment variables:

import os

database_url = os.getenv("DATABASE_URL")
'''
But then you have to manually handle:

1.Type conversion
2.Validation
3.Default values
4.Missing values
5.Configuration organization

Pydantic Settings makes this much cleaner.

'''
# You define:

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url : str
    port : int = 8000
    debug : bool = False

# and Pydantic handles the conversion and validation.



# Example:
class settings(BaseSettings):
    app_name : str = "Task managment API"
    admin_email : str
    item_per_user : int = 50

settings = settings()

# Using settings inside FastAPI

from fastapi import FastAPI 
from pydantic_settings import BaseSettings

class settings(BaseSettings):
    app_name : str = "Task mangment API"
    admin_email : str
    item_per_user : int = 50

settings = settings()

app = FastAPI()

@app.get("/user",response_model=settings)

def info():
    return {
        "app_name" : settings.app_name,
        "admin_email" : settings.admin_email,
        "item_per_user" : settings.item_per_user

    }


# 12. Settings in another module

# For a larger application, you shouldn't put your settings class inside main.py.

# Instead:

'''
app/
│
├── __init__.py
├── main.py
└── config.py

'''

# config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Management API"
    admin_email: str
    items_per_user: int = 50


settings = Settings()

# main.py
from fastapi import FastAPI

# from .config import settings


app = FastAPI()


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user
    }




# 21. What is .env?
# Now we reach one of the most useful parts of this FastAPI topic.

# Instead of manually setting:

APP_NAME="Task Management API"
ADMIN_EMAIL="admin@example.com"
ITEMS_PER_USER=50



# 23. Create .env
# Project:

'''
task-management/
│
├── app/
│   ├── main.py
│   └── config.py
│
├── .env
└── requirements.txt
'''

APP_NAME="Task Management API"
ADMIN_EMAIL="admin@example.com"
ITEMS_PER_USER=100

# Tell Pydantic to read .env

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50

    model_config = SettingsConfigDict(
        env_file=".env"
    )



# The important part is:

model_config = SettingsConfigDict(
    env_file=".env"
)

# This tells Pydantic:

# "Read configuration values from the .env file."




# 26. Complete .env example for your project
# For your Task Management + AI backend, you might eventually have:

APP_NAME="AI Task Management API"
ENVIRONMENT="development"

DATABASE_URL="postgresql://postgres:password@localhost/task_db"

SECRET_KEY="your-secret-key"

JWT_ALGORITHM="HS256"

ACCESS_TOKEN_EXPIRE_MINUTES=30

REDIS_URL="redis://localhost:6379"

QDRANT_URL="http://localhost:6333"

OPENAI_API_KEY="your-api-key"



# Then your settings models could be

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "AI Task Management API"

    environment: str = "development"

    database_url: str

    secret_key: str

    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int = 30

    redis_url: str

    qdrant_url: str

    openai_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()


# 34. Complete recommended FastAPI settings architecture

# For your projects, I recommend understanding this structure:
'''
task-management/
│
├── app/
│   │
│   ├── __init__.py
│   │
│   ├── main.py
│   │
│   ├── config.py
│   │
│   ├── dependencies.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       ├── users.py
│       └── tasks.py
│
├── .env
│
├── .gitignore
│
└── requirements.txt

'''

# config.py :

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "Task Management API"

    environment: str = "development"

    database_url: str

    secret_key: str

    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env"
    )


# main.py:

from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI

# from .config import Settings


app = FastAPI(
    title="Task Management API"
)


@lru_cache
def get_settings():
    return Settings()


@app.get("/info")
async def info(
    settings: Annotated[
        Settings,
        Depends(get_settings)
    ]
):
    return {
        "app_name": settings.app_name,
        "environment": settings.environment
    }


# .env :

APP_NAME="AI Task Management API"
ENVIRONMENT="development"

DATABASE_URL="postgresql://postgres:password@localhost/task_db"

SECRET_KEY="change-this-secret"

JWT_ALGORITHM="HS256"

ACCESS_TOKEN_EXPIRE_MINUTES=30

# Complete flow
'''
                    .env
                      │
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
   APP_NAME                  DATABASE_URL
   SECRET_KEY                JWT_ALGORITHM
        │                           │
        └─────────────┬─────────────┘
                      │
                      ▼
               BaseSettings
                      │
                      ▼
                 Settings()
                      │
                      ▼
                get_settings()
                      │
                 @lru_cache
                      │
                      ▼
               FastAPI Depends
                      │
                      ▼
                 API endpoint

'''




