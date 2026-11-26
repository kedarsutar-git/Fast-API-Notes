'''
1. First: What problem does async solve?
Imagine your FastAPI server receives 3 requests:


Request 1 → Database → waiting 2 sec
Request 2 → API      → waiting 2 sec
Request 3 → Database → waiting 2 sec


Request 1 → wait 2 sec → finish
                         ↓
Request 2 → wait 2 sec → finish
                         ↓
Request 3 → wait 2 sec → finish

Total ≈ 6 seconds


The important point is:
When your program is waiting for something like a database or network response, 
the CPU doesn't need to sit idle doing nothing.


Request A
   ↓
Ask database
   ↓
WAIT ───────────────┐
                    │
                    ▼
              Work on Request B
                    │
                    ▼
              Work on Request C
                    │
                    ▼
          Database A responds
                    │
                    ▼
          Continue Request A

          


2. Synchronous code
Normal Python function:
'''
# def get_user():
#     data = get_data_from_database()
#     return data

# Conceptually:
'''
Start
  ↓
Call database
  ↓
WAIT
  ↓
Database responds
  ↓
Return result
'''
# The function is synchronous.



'''
3. Asynchronous code
Now:
'''
# async def get_user():
#     data = await get_data_from_database()
#     return data

# async def get_user():  "This function can perform asynchronous operations."
# data = await get_data_from_database() : "Wait for this operation, but while waiting, allow other asynchronous work to proceed."



'''
6. Why is this useful for millions of users?
Suppose:

User A → Database → waiting
User B → API       → waiting
User C → Database → waiting
User D → File      → waiting
User E → Database → waiting



Conceptually:

             ┌── User A → DB → WAIT ──┐
Server ──────┼── User B → API → WAIT ─┤
             ├── User C → DB → WAIT ──┤
             └── User D → File → WAIT ┘
                         ↑
                  server can handle
                  other work
'''


# Real life example of asynchronous and synchronous 

# Synchronous approach
# You stand at the kitchen for 10 minutes:

'''
Order burger
     ↓
WAIT
     ↓
WAIT
     ↓
WAIT
     ↓
Burger ready
     ↓
Continue

'''

# Asynchronous approach
# You order:
'''
Order burger
     ↓
Get token #25
     ↓
Go sit down
     ↓
Study
     ↓
Talk
     ↓
Check token
     ↓
Burger ready
'''

# Very Important: async Does NOT Automatically Make Everything Faster
# This is one of the biggest misconceptions.

'''
If the operation is CPU-heavy, async isn't the main solution.

Image processing
Machine learning
Deep learning
Large matrix multiplication
Video processing
Heavy mathematical calculations

These are generally CPU-bound or can be GPU-bound workloads.
'''


'''
8. I/O-bound vs CPU-bound

I/O-bound
The program spends most of its time waiting.

Database
API
Network
File

use:
async def
await
when the library supports asynchronous operations.




CPU-bound

The program spends most of its time calculating.
Image processing
ML inference
Matrix multiplication
Deep learning
'''


'''
7. Concurrency vs Parallelism

1. Concurrency
Multiple tasks make progress by switching while waiting.
Task A → WAIT
Task B → RUN
Task B → WAIT
Task C → RUN
Task A → CONTINUE


2. parallelism
Multiple tasks actually execute at the same time using multiple CPU cores/processes.

CPU Core 1 → Task A
CPU Core 2 → Task B
CPU Core 3 → Task C
CPU Core 4 → Task D
'''



# How FastAPI Uses async def

from fastapi import FastAPI

app = FastAPI()
@app.get("/")

async def home():
    return {"message":"Hello"}


'''
 def vs async def in FastAPI

A useful table:

| Situation                  | Use |

| Async library with await`  | `async def`              |
| Async database driver      | `async def`              |
| Async HTTP client          | `async def`              |
| Async Redis client         | `async def`              |
| Async Qdrant client        | `async def`              |
| Synchronous library        | `def` can be appropriate |
| Don't know                 | `def` is a safe choice   |
| No I/O and simple endpoint | Either can work          |

'''

# What is a Coroutine?
'''
A coroutine is an asynchronous task that can pause while 
waiting and allow other tasks to run.

'''

# 1. Normal function

def get_data():
    return "Data"


result = get_data()
print(result)

# Execution is straightforward:
'''
get_data()
    ↓
execute
    ↓
return "Data"
'''


# 2. Coroutine

# When you use async def:

async def get_data():
    return "Data"

result = get_data()


'''
does not immediately give you "Data".

It creates a coroutine object.
'''


# Why do we use Coroutines?

'''
Coroutines are useful when your application needs to wait for I/O operations.

For Example :

FastAPI
   ↓
Database
   ↓
WAIT
   ↓
Database responds



Instead of blocking while waiting, a coroutine can pause:

Coroutine A
    ↓
await database
    ↓
PAUSE
    ↓
Other coroutine runs
    ↓
Database responds
    ↓
Coroutine A resumes

This is especially useful for:

- Database requests
- HTTP/API requests
- Redis
- Qdrant
- File/network operations
- External AI/LLM APIs
'''
# Code:

import asyncio
async def get_data():
    print("Starting")

    await asyncio.sleep(2)

    print("Data recived")
    return "Hello"

async def main():
    result = await get_data()

    print(result)

asyncio.run(main())

# output:
'''
Starting...
Data received
Hello


means:

Call get_data()
       ↓
Coroutine starts
       ↓
"Starting..." printed
       ↓
await asyncio.sleep(2)
       ↓
Coroutine pauses
       ↓
2 seconds pass
       ↓
Coroutine resumes
       ↓
"Data received"
       ↓
return "Hello"
       ↓
result = "Hello"



'''


# Event Loop:

'''
The event loop is a mechanism that manages and runs asynchronous tasks, 
switching to other tasks when the current task is waiting for I/O.

Think of it as a manager that keeps checking:

"Which task is ready to run?"



Without asynchronous execution, you might think:
Request A
   ↓
Wait for database
   ↓
Finish
   ↓
Request B
   ↓
Wait for API
   ↓
Finish
   ↓
Request C
The server spends a lot of time waiting.





With an event loop:
             EVENT LOOP
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
   Request A  Request B  Request C
       │         │         │
     await     await     await
       │         │         │
       └─────────┼─────────┘
                 ↓
        Run task that is ready




# Real life Example for event loop:

Imagine you are a waiter in a restaurant.
You have three customers:

Customer A → ordered pizza
Customer B → ordered burger
Customer C → ordered pasta


You give the pizza order to the kitchen.

The kitchen says:
"Pizza will take 15 minutes."

A bad waiter would stand next to the kitchen for 15 minutes:

Wait for pizza
     ↓
Wait
     ↓
Wait
     ↓
Wait



A smart waiter:

Give pizza order
       ↓
Go to Customer B
       ↓
Take burger order
       ↓
Go to Customer C
       ↓
Take pasta order
       ↓
Check pizza
       ↓
Serve pizza


The waiter = event loop

The customers = tasks

The kitchen waiting = I/O


'''

