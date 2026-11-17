'''
1. What are Python Types?
Python is dynamically typed, but you can specify what type of data a variable 
or function expects.


'''

name: str = "Kedar"
age: int = 20
height: float = 5.8
is_student: bool = True


# Function Type Hints
def add(a: int, b: int) -> int:
    return a + b

# a → int
# b → int
# return → int

result = add(10, 20)

print(result)



# 3. Why does FastAPI care about types?


from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# The user_id: int tells FastAPI:
# "This parameter should be an integer."

# So if someone requests:
# /users/25
# FastAPI converts and validates 25 as an integer.
# /users/abc

# is invalid because "abc" cannot be interpreted as an int.
# FastAPI uses Python type hints together with Pydantic to provide data validation and 
# uses them to generate OpenAPI documentation automatically.