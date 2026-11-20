# Error Handling

'''
In FastAPI, error handling means deciding what your API should return when 
something goes wrong—such as a resource not existing, invalid input, unauthorized 
access, or an internal problem.

'''

# 1. Why do we need error handling?
'''
GET /tasks/100
But task 100 doesn't exist.


Instead of returning:
null


you should tell the frontend:

{
    "detail": "Task not found"
}

with HTTP status:
404 Not Found

'''

# 2. HTTPException
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    if task_id != 1:
        raise HTTPException(status_code=404,detail="Task is not found")

    return {
        "Task_id":1,
        "title":"Learn Fastapi"

    }


# 3. What happens internally

'''
Suppose the user sends
GET /tasks/50

but task_id ==50 

The client receives:

404 Not Found

and 

{
    "detail": "Task not found"
}
'''

# 4. Important HTTP status codes

'''
| Status | Meaning | Example |

| `400` | Bad Request      | Invalid request              |
| `401` | Unauthorized     | Login/token required         |
| `403` | Forbidden        | User doesn't have permission |
| `404` | Not Found        | Task doesn't exist           |
| `409` | Conflict         | Email already exists         |
| `422` | Validation Error | Invalid request data         |
| `500` | Internal Server Error | Server-side problem     |
'''

# 5. detail can contain more than a string

raise HTTPException(
    status_code=400,
    detail={
        "field": "priority",
        "message": "Priority must be between 1 and 5"
    }
)

# Response:

{
    "detail": {
        "field": "priority",
        "message": "Priority must be between 1 and 5"
    }
}



# 7. RequestValidationError

# Suppose you have:

from pydantic import BaseModel

class Task(BaseModel):
    title: str
    priority: int

@app.post("/tasks")
async def create_task(task: Task):
    return task

# The frontend sends:
{
    "title": "Learn FastAPI",
    "priority": "HIGH"
}
# But 
priority: int

# expects an integer.

# So FastAPI detects invalid request data and internally raises:

RequestValidationError


# 15. Error handling flow

'''
                Client
                   │
                   ▼
             FastAPI Request
                   │
                   ▼
          ┌─────────────────┐
          │ Validate Request│
          └────────┬────────┘
                   │
          ┌────────┴─────────┐
          │                  │
       Valid              Invalid
          │                  │
          ▼                  ▼
     Your Endpoint    RequestValidationError
          │                  │
          │                  ▼
          │            Exception Handler
          │                  │
          ▼                  ▼
       Response          Error Response


And inside your endpoints:

Your endpoint
     │
     ├── Everything OK ──► 200
     │
     ├── Task missing ───► HTTPException 404
     │
     ├── Unauthorized ───► HTTPException 401
     │
     └── Forbidden ──────► HTTPException 403
'''