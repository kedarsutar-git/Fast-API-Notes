# 1. What are we trying to solve?
# Imagine your API has:
'''
1. What is Security in an API?
When we build an API, we need to answer questions like:
- Who is this user?
- Is this user logged in?
- What is this user allowed to access?
- Is the request coming from an authenticated user?
- How do we protect passwords and tokens?



GET /products
POST /products
DELETE /products
GET /profile

You don't want everyone to access everything.

For example:
                    FastAPI
                       │
          ┌────────────┴────────────┐
          │                         │
       Public                    Protected
          │                         │
      /products                /profile
                                  │
                             🔐 Login required


The user first logs in:     
 Username + Password
        │
        ▼
   POST /token
        │
        ▼
   Verify user
        │
        ▼
     Token
        │
        ▼
Frontend stores token
        │
        ▼
Request protected API
        │
        ▼
Authorization: Bearer <token>
'''


# 2. Authentication vs Authorization

# 1. Authentication:
'''
Authentication verifies the identity of a user, service, or device before granting access to a system.

Who are you?

Example:

Username: kedar
Password: ********

The server checks:
Are these credentials valid?
        ↓
      YES
        ↓
User = Kedar

So authentication identifies the user.


Common Authentication method :

1. Username and Password: Verifies a user's identity by requiring a registered username or email address and a password. 
Access is granted when the provided credentials match the stored information

2. Multi-Factor Authentication (MFA): Adds an extra layer of security by requiring two or more different authentication 
factors, such as a password and a fingerprint or verification code.

3. Biometric Authentication: Uses unique physical characteristics, such as fingerprints, facial recognition, or iris patterns, 
to verify a user's identity and provide secure access to a system.

4. One-Time Password (OTP): Uses a temporary verification code sent through SMS, email, or an authenticator app. 
The code is valid for a limited time or a single use.


'''

# 2.Authorization
'''
authorization determines what that authenticated user is allowed to access or do within a system.

Example:
In an online banking application, authentication verifies the user's identity, 
while authorization determines whether the user can transfer money or access account information.


What are you allowed to do?

For example:

Kedar → normal user
Admin → administrator

Maybe:

Kedar:
GET /profile       ✅
GET /posts         ✅
DELETE /users/10   ❌

Admin:
GET /profile       ✅
GET /posts         ✅
DELETE /users/10   ✅

'''

# OAuth2 :
# OAuth 2.0 is an authorization framework

'''
OAuth2 is a specification that defines several ways of handling authentication and authorization.

You will commonly encounter OAuth2 when using:
Google Login
GitHub Login
Facebook Login
X Login


Simplified idea
Suppose your application has:

Your App
   |
   | "Login with Google"
   ↓
Google
   |
   | verifies user
   ↓
Google gives authorization information
   |
   ↓
Your App


'''

# oAuth1 
'''
Older specification.

It was more complicated and included specifications related to signing/encrypting communication.

The FastAPI documentation says OAuth 1 is very different from OAuth2 and is not commonly used nowadays.


'''

# 5. OpenID Connect

# OpenID Connect (OIDC) is an authentication layer built on top of OAuth 2.0 
# that adds identity information via an ID token
# OpenID Connect (OIDC) is built on top of OAuth2. FastAPI

# Think:
'''
OAuth2
   ↓
Authorization
   ↓
OpenID Connect
   ↓
Authentication / identity information


Simple distinction:

OAuth2
"What is this application allowed to access?"

OIDC
"Who is this user?"
'''

# 6 .OpenAPI
# OpenAPI is an open specification for describing APIs. FastAPI is based on OpenAPI. 
'''
Swagger UI
ReDoc
OpenAPI schema


For example:

FastAPI Application
       ↓
     OpenAPI
       ↓
┌─────────────────┐
│ Swagger UI      │
│ /docs           │
└─────────────────┘
'''



# 9. API Key
# An API key is basically a secret value used to identify/authorize an application or client.

'''
Example:
X-API-Key: abc123xyz

The API receives:
Client
  |
  | X-API-Key: abc123xyz
  ↓
FastAPI
  |
  | Check API key
  ↓
Database / service
'''


# HTTP Authentication
# OpenAPI also supports HTTP authentication mechanisms.

'''
For example:
HTTP Basic
HTTP Bearer
HTTP Digest

The one you'll encounter frequently in modern APIs is:

Bearer Authentication
'''


# 11. Bearer Token
# A bearer token is commonly sent through the HTTP Authorization header.

'''
Example:
Authorization: Bearer eyJhbGciOi...

The structure is:
Authorization:
    Bearer
       +
    TOKEN

So:
Authorization: Bearer abc123

The word Bearer tells the server what authentication scheme is being used.
'''


# Why is it called "Bearer"?
# Think about a physical ticket.
'''
If you possess the ticket:
Ticket
  ↓
Bearer
  ↓
Allowed

Similarly:
Token
  ↓
Bearer
  ↓
Can access protected resource

'''


# Complete Authentication Flow

'''
                 USER
                  │
                  │ username + password
                  ↓
          ┌─────────────────┐
          │    FastAPI      │
          │  /token         │
          └────────┬────────┘
                   │
                   │ Verify credentials
                   ↓
             ┌─────────────┐
             │   Database  │
             └──────┬──────┘
                    │
                    │ Valid
                    ↓
              Create Token
                    │
                    ↓
          ┌─────────────────┐
          │ Access Token    │
          └────────┬────────┘
                   │
                   │ Authorization:
                   │ Bearer TOKEN
                   ↓
          ┌─────────────────┐
          │ Protected API   │
          │ /users/me       │
          └────────┬────────┘
                   │
                   ↓
                Response

'''

# FastAPI Security Utilities:

# You'll commonly see things such as:
from fastapi.security import OAuth2PasswordBearer

# and later:

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



# What does OAuth2PasswordBearer do?

'''
Suppose the client sends:

GET /users/me
Authorization: Bearer abc123

FastAPI needs to extract:
abc123

OAuth2PasswordBearer helps define this bearer-token security scheme.

HTTP Request
     │
     │ Authorization: Bearer abc123
     ↓
OAuth2PasswordBearer
     │
     │ extracts token
     ↓
"abc123"
'''

# Example 

from fastapi import Depends ,FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme =OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")

async def read_user_me(token:str = Depends(oauth2_scheme)):
    return {"token":token}


# 24. The Most Important Mental Model
# Don't try to memorize all the terminology.

'''
                    SECURITY
                       │
        ┌──────────────┴──────────────┐
        │                             │
 Authentication                 Authorization
        │                             │
 "Who are you?"                "What can you do?"
        │                             │
        ↓                             ↓
 Username/password                 Roles
 OAuth2                            Permissions
 OIDC                              Scopes
        │
        ↓
     TOKEN
        │
        ↓
 Authorization: Bearer <token>
        │
        ↓
     FastAPI
        │
        ↓
 Protected endpoint
'''
