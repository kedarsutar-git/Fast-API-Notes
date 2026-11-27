# FASTAPI LIFESPAN EVENTS
# Official docs: https://fastapi.tiangolo.com/advanced/events/

"""
What is a lifespan event?
-------------------------
Lifespan code runs around the whole life of a FastAPI application:

    server starts
         |
         v
    code BEFORE yield  -> run once before the app accepts requests
         |
         v
    endpoints handle many requests
         |
         v
    code AFTER yield   -> run once while the app is shutting down

Use it for resources shared by many requests, such as:
- a database connection pool
- an HTTP client
- a machine-learning model loaded into memory
- a message-queue connection
   
Do not load an expensive shared resource at module level if it should only be
created when the application actually starts. Lifespan also gives that resource
a matching place to be cleaned up.
"""

# Basic Lifespan code:

# Here's the core pattern:

from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app:FastAPI):

    # Statup 
    print("Application starting..")

    yield

    # Shutdown
    print("Application shutting dewn..")

app = FastAPI(lifespan=lifespan)


# Think of it as the boundary:

@asynccontextmanager
async def lifespan():

    # BEFORE yield
    # ↓
    # Startup code

    yield

    # AFTER yield
    # ↓
    # Shutdown code



# Understand yield
@asynccontextmanager
async def lifespan(app: FastAPI):

    print("START")

    yield

    print("STOP")

'''
FastAPI starts
      ↓
print("START")
      ↓
yield
      ↓
Application runs
      ↓
Handles requests
      ↓
Application stops
      ↓
print("STOP")
'''



# Real machine learning model Example 

from contextlib import asynccontextmanager
from fastapi import FastAPI

ml_model = {}

def load_model():
    print("Loading model..")
    return "MY Ml MODEL"

@asynccontextmanager

async def lifeepen(app:FastAPI):
    # Startup
    ml_model["model"] = load_model()

    yield

    # shutdown
    ml_model.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/predict")

async def predict():
    model = ml_model["model"]

    return {
        "model":model,
        "prediction":"Cat"
    }


# Work flow :
'''
                FastAPI starts
                      │
                      ▼
               lifespan()
                      │
                      ▼
                load_model()
                      │
                      ▼
             Model in memory
                      │
                      ▼
                    yield
                      │
                      ▼
             Application running
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Request 1   Request 2   Request 3
          │           │           │
          └───────────┼───────────┘
                      ▼
               Same ML model
                      │
                      ▼
              Application stops
                      │
                      ▼
             ml_models.clear()
'''

# Database Connection Pool Example

from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup
    app.state.db_pool = await create_db_pool()

    yield

    # Shutdown
    await app.state.db_pool.close()


app = FastAPI(lifespan=lifespan)

# work flow :
'''
START
  ↓
Create DB pool
  ↓
Application handles requests
  ↓
Requests reuse DB pool
  ↓
STOP
  ↓
Close DB pool
'''



# why @asynccontextmanager:
'''
@asynccontextmanager converts your async generator function into an async context manager. 
FastAPI can then use that context manager for the application's lifespan.

@asynccontextmanager
        ↓
Creates async context manager
        ↓
FastAPI uses it
        ↓
Before yield → startup
        ↓
After yield → shutdown


'''


# LifeSpan vs Dependency

# Dependency
# Usually related to a request:
'''
Request
   ↓
Dependency
   ↓
Endpoint
   ↓
Response


Used for:

Authentication
Authorization
Database session
Request-specific resources

'''


# Lifespan
# Related to the entire application:
'''
Application starts
       ↓
Lifespan startup
       ↓
Many requests
       ↓
Lifespan shutdown
       ↓
Application stops

Used for:

ML models
Database pools
Redis clients
Shared resources
Application initialization
Resource cleanup
'''


'''
| Dependency                      | Lifespan                 |

| Request-level                   | Application-level        |
| Runs as needed for requests     | Runs at startup/shutdown |
| `Depends()`                     | `lifespan=`              |
| Current user                    | ML model                 |
| DB session | DB connection pool |
| Request-specific resource       | Shared resource          |
'''



# Old startup and shutdown Events and new startup and shutdown Event

# 1. old
@app.event("startup")
async def startup():
    print("Starting")


@app.event("shutdown")
async def shutdown():
    print("Stopping")


# 2. new Recommended

from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting")

    yield

    print("Stopping")


app = FastAPI(lifespan=lifespan)


# One Important Detail:

# The application doesn't start accepting requests until the startup portion has completed. The official 
# documentation states that lifespan startup code runs before the application starts receiving requests.

'''
So:
Server starts
     ↓
lifespan startup
     ↓
Load model
     ↓
Connect resources
     ↓
yield
     ↓
READY
     ↓
Accept requests
'''


# The Most Important Code to Remember

from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):

    # =========================
    # STARTUP
    # =========================

    print("Application starting...")

    # Load resources
    # model = load_model()
    # db = create_database_pool()
    # redis = create_redis_client()

    yield

    # =========================
    # SHUTDOWN
    # =========================

    print("Application shutting down...")

    # Release resources
    # model = None
    # await db.close()
    # await redis.close()


app = FastAPI(lifespan=lifespan)

'''
                 FASTAPI
                    │
                    ▼
              Application Start
                    │
                    ▼
              lifespan()
                    │
                    ▼
              STARTUP CODE
                    │
              Load resources
                    │
                    ▼
                  yield
                    │
                    ▼
             Application Running
                    │
              ┌─────┼─────┐
              ▼     ▼     ▼
           Request Request Request
              │     │     │
              └─────┼─────┘
                    │
                    ▼
             Application Stop
                    │
                    ▼
             SHUTDOWN CODE
                    │
              Cleanup resources
                    │
                    ▼
                  STOP
'''