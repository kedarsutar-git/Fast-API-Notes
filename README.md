# FastAPI + AI Backend: Complete 30-Day Zero-to-Advanced Roadmap

A complete, hands-on roadmap for learning **FastAPI from zero** and building a production-minded AI backend in 30 days. It moves from Python and HTTP fundamentals through API design, databases, security, testing, file processing, LLMs, retrieval-augmented generation (RAG), and deployment.

> **Outcome:** build and document a tested AI knowledge-assistant API. Thirty days can provide a strong foundation and a working portfolio project; advanced engineering skills continue to grow through practice. Aim for **2–4 focused hours per day** and adjust the pace to your experience.

## Project you’ll build

An AI knowledge assistant API where users can register and sign in, upload documents, process and search their own content, and ask questions answered using retrieved sources. You will evolve the same project throughout the month.

### Suggested stack

- **API:** Python 3.11+, FastAPI, Pydantic v2, Uvicorn
- **Database:** PostgreSQL, SQLAlchemy 2.x, Alembic
- **Tests:** pytest, HTTPX, FastAPI dependency overrides
- **AI and retrieval:** an LLM provider, embeddings, sentence-transformers, and Qdrant (or an equivalent vector store)
- **Operations:** Redis, Docker, Docker Compose, environment-based settings

Equivalent tools are fine. Keep credentials in environment variables; never commit secrets.

## Getting started

1. Install Python, Git, and Docker, then create a virtual environment.
2. Review Python functions, collections, classes, type hints, exceptions, and modules. If you are new to Python, take extra time on Days 1–3.
3. Clone this repository and use its numbered notes alongside the roadmap. Add project code and exercises as you learn.
4. Keep a learning log: what you built, what failed, and what you want to understand next.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install fastapi 'uvicorn[standard]' pydantic-settings
```

Once you create `app/main.py` with a FastAPI application named `app`, run:

```bash
uvicorn app.main:app --reload
```

Explore the interactive API docs at `http://127.0.0.1:8000/docs` and `http://127.0.0.1:8000/redoc`.

## Complete day-by-day roadmap

### Week 1 — Python, HTTP, and FastAPI foundations

| Day | Study | Build and verify |
|---|---|---|
| **1 — Python basics** | Variables, built-in types, collections, functions, virtual environments, and running Python. | Create a typed module for documents; practice the Python REPL, scripts, and Git commits. |
| **2 — Python structure** | Modules, imports, classes, exceptions, and readable code. | Model a document and write functions to validate and summarize it. Handle invalid input with clear exceptions. |
| **3 — HTTP essentials** | Client/server model, URLs, methods, status codes, headers, JSON, requests, and responses. | Call a public API with an HTTP client. Explain when to use `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`. |
| **4 — First FastAPI app** | App instance, path operations, route functions, Uvicorn, and generated OpenAPI docs. | Create `/health` and a simple in-memory resource endpoint; inspect `/docs` and `/redoc`. |
| **5 — Parameters** | Path and query parameters, defaults, types, validation, constraints, and pagination. | Add document lookup, search, sorting, and bounded pagination. Try valid and invalid requests. |
| **6 — Request models** | Pydantic models, nested request bodies, field constraints, and validation errors. | Create request schemas for document creation and updates. Verify malformed payloads receive useful validation responses. |
| **7 — Responses and CRUD** | Response models, HTTP status codes, error handling, and CRUD conventions. | Implement create/read/update/delete routes, deliberate response schemas, and helpful not-found errors. Review Week 1. |

**Week 1 checkpoint:** you can run a FastAPI app, call its endpoints, explain its request and response schemas, and use the generated API documentation.

### Week 2 — Maintainable APIs and database foundations

| Day | Study | Build and verify |
|---|---|---|
| **8 — Application structure** | Routers, tags, prefixes, and larger application organization. | Split routes into modules such as `api/v1`; keep application creation and router registration in `main.py`. |
| **9 — Dependency injection** | FastAPI dependencies, reusable components, and dependency lifetimes. | Add shared pagination and a database-session dependency. Trace how dependencies are resolved. |
| **10 — Configuration and lifecycle** | Settings, environment variables, CORS, and application lifespan. | Load configuration from environment variables, allow only required CORS origins, and manage app resources with lifespan handling. |
| **11 — Async and concurrency** | `async`/`await`, concurrency, I/O-bound work, and blocking operations. | Identify which operations are async. Avoid blocking the event loop; use synchronous handlers or offloading appropriately for blocking work. |
| **12 — PostgreSQL and SQL** | Relational modeling, tables, keys, constraints, and basic SQL queries. | Run PostgreSQL locally. Design users, documents, and conversations; write basic create/read/update/delete queries. |
| **13 — SQLAlchemy** | SQLAlchemy 2.x models, queries, sessions, and transaction boundaries. | Persist and retrieve application records. Keep session creation and cleanup explicit. |
| **14 — Migrations** | Alembic revisions, schema evolution, and transaction basics. | Generate and apply a migration. Confirm a fresh database can be created from migrations and existing data is not casually discarded. |

**Week 2 checkpoint:** the API has a modular structure, externalized configuration, and database-backed records managed by migrations.

### Week 3 — Security, tests, files, and AI integration

| Day | Study | Build and verify |
|---|---|---|
| **15 — Authentication** | Password hashing, OAuth2 concepts, bearer tokens, and JWT access tokens. | Add registration and login. Hash passwords, issue tokens, and protect a user-only endpoint. Never store plaintext passwords. |
| **16 — Authorization** | Ownership checks, least privilege, token validation, and common security mistakes. | Scope document queries to the authenticated user. Test missing, invalid, and expired credentials and cross-user access attempts. |
| **17 — Automated testing** | pytest, HTTPX, fixtures, isolated test configuration, and test design. | Test successful requests, validation failures, not-found behavior, and core CRUD routes using an isolated test database. |
| **18 — Integration testing** | Dependency overrides, test doubles, and external-service boundaries. | Override authentication, database, and AI dependencies where appropriate. Test important integrations without real credentials. |
| **19 — File uploads** | Multipart uploads, validation, storage choices, and safe file handling. | Accept supported document types, enforce size/type limits, generate safe storage names, and never trust client-provided filenames. |
| **20 — Background processing** | Document extraction, chunking, job status, retries, and task queues. | Separate upload from extraction and indexing; expose processing status. Use a durable task queue for long-running work rather than relying on in-process background tasks. |
| **21 — LLM integration** | Provider APIs, prompts, structured inputs, timeouts, rate limits, and error handling. | Add a provider abstraction and a basic question endpoint. Keep keys out of source control and handle provider failures without leaking sensitive details. |

**Week 3 checkpoint:** protected endpoints have tests, uploads are handled defensively, and AI-provider failures are controlled.

### Week 4 — Retrieval, operations, deployment, and capstone

| Day | Study | Build and verify |
|---|---|---|
| **22 — Embeddings and chunks** | Embeddings, chunk size/overlap, metadata, and semantic search. | Chunk processed documents, generate embeddings, and compare search results for representative questions. |
| **23 — Vector database** | Collections, vector storage, similarity search, and metadata filters. | Store and retrieve vectors in Qdrant or another vector database. Filter every query by the correct user/document scope. |
| **24 — RAG** | Retrieval-augmented generation, grounding, source attribution, and insufficient evidence. | Retrieve relevant chunks before generating an answer. Return source references and make the API say when retrieved evidence is insufficient. |
| **25 — Redis and performance** | Caching, cache invalidation, rate-limiting concepts, and performance trade-offs. | Cache a safe, repeatable operation or add rate limiting. Ensure private results cannot be shared across users via cache keys. |
| **26 — Observability** | Structured logs, request IDs, health checks, and actionable error reporting. | Add liveness/readiness checks and useful logs. Do not log secrets, tokens, or sensitive document content. |
| **27 — Docker** | Dockerfiles, images, environment configuration, and Docker Compose. | Containerize the API and run it with PostgreSQL and Redis. Document required environment variables and startup steps. |
| **28 — Deployment** | Production settings, secrets, migrations, process startup, and security review. | Deploy to a platform of your choice. Disable development reload, configure secrets, apply migrations safely, and verify health checks. |
| **29 — End-to-end quality** | Integration and end-to-end testing, performance checks, and known limitations. | Test the journey from registration through upload to a cited AI answer. Run a basic load check and document limitations. |
| **30 — Capstone and demo** | Review, polish, technical communication, and next steps. | Finalize setup instructions, API examples, architecture diagram, and demo. Run the acceptance checklist and choose one next improvement. |

**Week 4 checkpoint:** a containerized, deployable app can ingest documents and answer questions with retrieved sources, backed by tests and operational documentation.

## Capstone acceptance checklist

- [ ] The API starts locally from the documented setup instructions.
- [ ] OpenAPI documentation is available and request/response schemas are intentional.
- [ ] Users can register, log in, and access only their own resources.
- [ ] Passwords are hashed; tokens and secrets are handled safely.
- [ ] Database changes are managed with migrations.
- [ ] Uploads have size/type checks and visible processing status.
- [ ] AI answers use retrieved context and expose sources; provider errors are handled.
- [ ] Tests cover happy paths, validation failures, authorization, and important integrations.
- [ ] Docker Compose starts local services; deployment configuration is documented.
- [ ] Logs and health checks support debugging without exposing credentials or private content.

## Suggested project structure

```text
app/
├── main.py                 # app creation and router registration
├── core/                   # settings, security, and logging
├── api/v1/                 # versioned routes
├── schemas/                # Pydantic request/response models
├── models/                 # SQLAlchemy models
├── services/               # business logic and AI/retrieval workflows
├── repositories/           # data access
└── dependencies/           # shared FastAPI dependencies
alembic/                    # database migrations
 tests/                     # unit and integration tests
```

Start simple and add layers when they make responsibilities clearer. Rename the ` tests/` example to `tests/` when creating the directory (without a leading space).

## A repeatable daily study routine

1. **Learn (30–45 min):** read the relevant documentation and write down key ideas.
2. **Implement (60–120 min):** add the day’s feature to the same project.
3. **Verify (30–45 min):** exercise success, failure, and edge cases; add automated tests where relevant.
4. **Reflect (10 min):** commit a small change and record one takeaway and one open question.

## Recommended learning resources

### FastAPI

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [First steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Path parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Query parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Request bodies](https://fastapi.tiangolo.com/tutorial/body/)
- [Response models](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Response status codes](https://fastapi.tiangolo.com/tutorial/response-status-code/)
- [Body fields](https://fastapi.tiangolo.com/tutorial/body-fields/)
- [Error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [Bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Settings](https://fastapi.tiangolo.com/advanced/settings/)
- [CORS](https://fastapi.tiangolo.com/tutorial/cors/)
- [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)
- [Async and await](https://fastapi.tiangolo.com/async/)
- [Application events and lifespan](https://fastapi.tiangolo.com/advanced/events/)
- [Security](https://fastapi.tiangolo.com/tutorial/security/)
- [OAuth2 and JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Testing dependencies](https://fastapi.tiangolo.com/advanced/testing-dependencies/)
- [File uploads](https://fastapi.tiangolo.com/tutorial/request-files/)
- [Custom responses and streaming](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse)
- [Background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
- [Deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker deployment](https://fastapi.tiangolo.com/deployment/docker/)

### Databases, AI, and operations

- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [SQLAlchemy 2.x ORM quick start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [Sentence Transformers](https://sbert.net/)
- [Qdrant quick start](https://qdrant.tech/documentation/quickstart/)
- [Qdrant documentation](https://qdrant.tech/documentation/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Redis documentation](https://redis.io/docs/)
- [Redis Python client](https://redis.readthedocs.io/en/stable/)
- [Docker Compose documentation](https://docs.docker.com/compose/)
- [Anthropic documentation](https://docs.anthropic.com/)

## Repository notes

This repository is a growing collection of FastAPI and Python notes. The numbered Python files are useful companions for foundational topics; use this roadmap to organize your learning and add examples as you progress.

## License and attribution

This is a learning roadmap, not a substitute for the linked projects’ documentation. Refer to each resource for its licensing and usage terms.
