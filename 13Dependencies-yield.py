# What problem does yield solve?
'''
Suppose you need a database connection.

You want to:

1.Open database connection
2.Give that connection to your API endpoint
3.Execute database operations
4.Close the connection afterward


OPEN DATABASE
      ↓
Give DB to endpoint
      ↓
Endpoint uses DB
      ↓
Endpoint finishes
      ↓
CLOSE DATABASE

'''


# return vs yield

# 1. Using return 
def get_data():
    print("Start")
    return "Hello"

    print("End")

# End will never execute. because return 

# 2. Using yield

def get_data():
    print("Start")

    yield "Hello"

    print("End")

print(get_data())


# Now FastAPi can execute:

'''
Start
 ↓
yield "Hello"
 ↓
Endpoint executes
 ↓
Endpoint finishes
 ↓
End

'''

# The most important example: Database

from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    db = "Database Connection"

    print("Database opend")

    try:
        yield db

    finally:
        print("Database closed")

@app.get("/user/")

def get_users(db = Depends(get_db)):

    print("Using database")

    return {
        "message": "Users fetched"
    }


# FastApi does:
'''
             CLIENT
                │
                │ GET /users
                ▼
          FastAPI receives
                │
                ▼
        Depends(get_db)
                │
                ▼
           get_db()
                │
                ├── Database opened
                │
                ▼
             yield db
                │
                ▼
       get_users(db)
                │
                ├── Using database
                │
                ▼
          Return response
                │
                ▼
        finally executes
                │
                ├── Database closed
                │
                ▼
             CLIENT
'''


# Why try + finally
from dtos import DBSession

def get_db():

    db = DBSession()

    try:
        yield db

    finally:
        db.close()

# Why?

# Because we want:

'''
Open DB
   ↓
Use DB
   ↓
Close DB

'''

# Even if something goes wrong.

# For example:

def get_db():

    db = DBSession()

    try:
        yield db

    finally:
        db.close()

# Suppose your endpoint does

@app.get("/user/")
def get_user(db = Depends(get_db)):
    raise Exception("Something went wrong")

# Even though the endpoint raises an exception:
'''
get_db()
   ↓
open DB
   ↓
yield db
   ↓
get_users()
   ↓
ERROR ❌
   ↓
finally
   ↓
db.close()
'''
# The finally block is designed for cleanup.

# Before yield = preparation
# yield = give resource to endpoint
# After yield = cleanup



# Annotated version

from typing import Annotated
from fastapi import FastAPI,Depends

app = FastAPI()

def get_db():
    db = DBSession()

    try:
        yield db

    finally:
        db.close()

dbDepd = Annotated[dict,Depends(get_db)]
@app.get("/user")
def get_user(db:dbDepd):
    return {
        "Status":"Uset Fetched"
    }

'''
db
 │
 ├── Type = DBSession
 │
 └── Dependency = get_db
'''


# What exactly happens around yield?

def get_db():

    print("1. Open DB")

    db = DBSession()

    try:

        print("2. Before yield")

        yield db

        print("4. After yield")

    finally:

        print("5. Close DB")


@app.get("/users")
def users(db = Depends(get_db)):

    print("3. Endpoint")

    return {"message": "success"}


# Execution order:

'''

1. Open DB
       ↓
2. Before yield
       ↓
yield db
       ↓
3. Endpoint
       ↓
Response generated
       ↓
4. After yield
       ↓
5. Close DB

'''
