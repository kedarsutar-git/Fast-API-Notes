# FastAPI + AI Backend: 30-Day Zero-to-Advanced Roadmap

A practical, project-first plan for learning **FastAPI from the ground up** and building a production-minded AI backend in 30 days. You’ll progress from Python and HTTP fundamentals to authentication, PostgreSQL, testing, retrieval-augmented generation (RAG), Docker, and deployment.

> **The goal:** finish with a working, documented, tested AI API and a solid understanding of the decisions behind it. “Advanced” is a starting point for continued practice—not a promise of mastery in 30 days. Plan for **2–4 focused hours a day**; adjust the pace to your experience.

## What you’ll build

An AI knowledge assistant API that lets users register and sign in, upload documents, process and search their content, and ask questions with answers grounded in retrieved sources. The project grows throughout the roadmap rather than being discarded for a new tutorial every week.

### Suggested stack

- **API:** Python 3.11+, FastAPI, Pydantic v2, Uvicorn
- **Persistence:** PostgreSQL, SQLAlchemy 2.x, Alembic
- **Testing:** pytest, HTTPX, FastAPI dependency overrides
- **AI and retrieval:** an LLM provider, embeddings, sentence-transformers, and Qdrant (or another vector store)
- **Operations:** Redis, Docker, Docker Compose, environment-based settings

You can substitute equivalent tools. Keep provider credentials in environment variables; never commit secrets.

## Before you begin

1. Install Python, Git, and Docker; create a virtual environment.
2. Review basic Python, functions, classes, type hints, exceptions, and modules. If you’re new to Python, spend extra time on Days 1–3.
3. Clone this repository and use the numbered notes as companion material. Add your own exercises and project code as you go.
4. Keep a learning log. Each day, write down what you built, what failed, and one question to investigate.

A typical project setup:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install fastapi uvicorn[standard] pydantic-settings
```

Start a small app with `uvicorn app.main:app --reload`; explore `/docs` and `/redoc`.

## The 30-day plan

### Week 1 — Python, HTTP, and FastAPI foundations

| Day | Learn | Build / prove it |
|---|---|---|
| **1** | Python types, variables, collections, functions, and virtual environments | Create a small typed Python module; practice running it and using Git. |
| **2** | Modules, classes, exceptions, and clean code | Model a document and write functions to validate and summarize it. |
| **3** | HTTP basics: methods, status codes, headers, JSON, requests, and responses | Use an HTTP client to inspect a public API; explain the difference between `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`. |
| **4** | Create a FastAPI app, path operations, automatic OpenAPI docs | Build `/health` and a simple in-memory resource endpoint. |
| **5** | Path and query parameters, defaults, constraints, and pagination | Add searchable, paginated document routes and validate inputs. |
| **6** | Pydantic request bodies, nested models, field validation | Define create, update, and read schemas; reject malformed requests. |
| **7** | Response models, status codes, error handling, and recap | Add CRUD behavior, useful errors, and a short API usage guide. |

**Week 1 checkpoint:** you can start the app, call its endpoints, explain its schemas, and read the generated API documentation.

### Week 2 — Maintainable APIs and database foundations

| Day | Learn | Build / prove it |
|---|---|---|
| **8** | Routers and bigger application structure | Split routes into versioned modules such as `api/v1` and keep `main.py` focused. |
| **9** | Dependency injection and reusable dependencies | Add shared pagination and a database-session dependency; understand dependency scope. |
| **10** | Settings, environment variables, CORS, and application lifecycle | Load configuration from the environment, configure CORS deliberately, and initialize app resources with lifespan handling. |
| **11** | Async/await and concurrency fundamentals | Identify I/O-bound work; use `async def` appropriately and avoid blocking the event loop. |
| **12** | PostgreSQL, SQL basics, and schema design | Create the local database and design users, documents, and conversations. |
| **13** | SQLAlchemy 2.x models and database sessions | Persist and retrieve application records; keep session lifecycle explicit. |
| **14** | Alembic migrations and transaction basics | Generate and apply a migration; verify a fresh database can be created from migrations. |

**Week 2 checkpoint:** the API has a modular structure, configuration is externalized, and records persist in PostgreSQL.

### Week 3 — Security, tests, files, and AI integration

| Day | Learn | Build / prove it |
|---|---|---|
| **15** | Password hashing, OAuth2 concepts, JWT access tokens | Add registration and login; hash passwords and protect a user-only endpoint. |
| **16** | Authorization, ownership checks, and security pitfalls | Ensure users can access only their own documents; test invalid, expired, and missing credentials. |
| **17** | pytest, HTTPX, fixtures, and testable app design | Test success and failure cases for core endpoints using an isolated test database. |
| **18** | Dependency overrides and integration testing | Replace external services in tests; cover authentication and database behavior without real credentials. |
| **19** | File uploads, validation, and safe storage | Accept supported document types, enforce size/type limits, and avoid trusting client-provided filenames. |
| **20** | Background work and document-processing pipeline | Separate upload from extraction/chunking; make processing status visible to clients. Use a task queue for durable or long-running jobs rather than relying on in-process tasks. |
| **21** | LLM APIs, structured inputs, timeouts, and error handling | Add a provider abstraction and a basic question endpoint; handle rate limits and provider failures safely. |

**Week 3 checkpoint:** protected endpoints are tested, files are handled defensively, and AI-provider failures do not crash the API.

### Week 4 — Retrieval, performance, deployment, and capstone

| Day | Learn | Build / prove it |
|---|---|---|
| **22** | Embeddings, chunking, and semantic search | Generate embeddings for processed documents and compare search results for several queries. |
| **23** | Vector databases and metadata filtering | Store and retrieve vectors in Qdrant (or an alternative); filter results by user and document. |
| **24** | RAG: retrieve, ground, and cite | Build a retrieve-then-answer flow; return relevant source snippets and say when evidence is insufficient. |
| **25** | Redis, caching, and rate limiting concepts | Cache a safe, repeatable operation or add a rate limit; do not cache private data across users. |
| **26** | Observability, structured logging, and health checks | Add request-aware logs, readiness/liveness checks, and actionable error reporting without logging secrets or sensitive content. |
| **27** | Docker and Docker Compose | Containerize the API and run it with PostgreSQL and Redis locally. Document environment variables and startup steps. |
| **28** | Deployment, production settings, and security review | Deploy to a platform of your choice; disable development reload, configure secrets, and verify database migrations and health checks. |
| **29** | End-to-end testing, performance checks, and documentation | Test the main user journey from account creation to a cited AI answer; document limitations and run a basic load check. |
| **30** | Capstone polish and demo | Deliver a clean README, API examples, architecture diagram, setup instructions, and a short demo. Review the checklist below and choose your next improvement. |

**Week 4 checkpoint:** a deployed, containerized application can ingest documents and answer questions with retrieved sources, with tests and operational documentation.

## Capstone acceptance checklist

- [ ] The API starts locally from documented setup instructions.
- [ ] OpenAPI docs are available, and request/response schemas are intentional.
- [ ] Users can register, log in, and access only their own resources.
- [ ] Passwords are hashed; tokens and secrets are handled safely.
- [ ] Database schema changes are managed with migrations.
- [ ] File uploads have size/type checks and predictable processing status.
- [ ] AI answers use retrieved context and expose sources; provider errors are handled.
- [ ] Tests cover happy paths, validation failures, authorization, and important integrations.
- [ ] Docker Compose starts the local services; deployment configuration is documented.
- [ ] Logs and health checks support debugging without exposing credentials or private content.

## Recommended project layout

```text
app/
├── main.py                 # app creation and router registration
├── core/                   # settings, security, logging
├── api/v1/                 # versioned routes
├── schemas/                # Pydantic request/response models
├── models/                 # SQLAlchemy models
├── services/               # business logic, AI and retrieval workflows
├── repositories/           # data access
└── dependencies/           # shared FastAPI dependencies
alembic/                    # database migrations
 tests/                     # unit and integration tests
```

Keep the initial implementation simple. Add layers when they clarify responsibilities, not just to match a diagram.

## How to study effectively

- **Build before you binge:** spend most of each session coding and testing, not watching tutorials.
- **Use a daily loop:** learn one concept → implement it → test edge cases → write a brief note.
- **Commit in small steps:** use meaningful commits and keep working code on the default branch.
- **Prefer official documentation:** verify APIs and security guidance against the current docs, especially as libraries evolve.
- **Review every dependency:** understand what data it receives, where it is stored, and how failures are handled.
- **Don’t skip testing:** a route that works once in Swagger is not a tested feature.

## Learning resources

### FastAPI

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Tutorial — first steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Path parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Query parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Request bodies](https://fastapi.tiangolo.com/tutorial/body/)
- [Response models](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [Bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Async and await](https://fastapi.tiangolo.com/async/)
- [OAuth2 and JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Testing dependencies](https://fastapi.tiangolo.com/advanced/testing-dependencies/)
- [File uploads](https://fastapi.tiangolo.com/tutorial/request-files/)
- [Background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
- [Deployment concepts](https://fastapi.tiangolo.com/deployment/)

### Database, AI, and operations

- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [SQLAlchemy 2.x ORM quick start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [Sentence Transformers](https://sbert.net/)
- [Qdrant quick start](https://qdrant.tech/documentation/quickstart/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Redis documentation](https://redis.io/docs/)
- [Docker Compose documentation](https://docs.docker.com/compose/)

## Repository notes

This repository is a growing collection of FastAPI and Python notes. The numbered Python files are useful companions for foundational topics; use this 30-day plan to organize your learning and add examples as you progress.

## License and attribution

This is a learning roadmap, not a substitute for the linked projects’ documentation. Refer to each resource for its licensing and usage terms.
