'''
1. First understand the problem
Imagine your FastAPI server receives 3 requests:


Request 1 → Database → waiting 2 sec
Request 2 → API      → waiting 3 sec
Request 3 → Database → waiting 1 sec



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


'''
7. Concurrency vs Parallelism

1. Concurrency
Multiple tasks make progress by switching while waiting.
Task A → WAIT
Task B → RUN
Task B → WAIT
Task C → RUN
Task A → CONTINUE


2. arallelism
Multiple tasks actually execute at the same time using multiple CPU cores/processes.

CPU Core 1 → Task A
CPU Core 2 → Task B
CPU Core 3 → Task C
CPU Core 4 → Task D
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