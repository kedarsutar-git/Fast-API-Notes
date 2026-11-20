# 🚀 30-Day FastAPI + AI Backend Roadmap

> From "Hello FastAPI" to a production-style **RAG Knowledge Assistant** in 30 days.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-vector%20DB-DC244C)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/progress-0%2F30-blue)

---

## 📌 About

This repository documents my 30-day journey to learn the FastAPI topics that matter most for **AI Engineering** and **Backend Development**, while building one production-style RAG backend step by step.

**Rules I follow**

- ❌ Don't read the FastAPI docs front to back.
- ✅ For each day: study the linked section → code the examples → finish the daily task **without looking at a solution**.
- ✅ Write tests as I go, starting **Day 14**.
- ✅ Commit every day (`day-XX: short description`).

---

## 🗺️ Roadmap at a Glance

| Phase | Days | Focus |
|:-----:|:----:|-------|
| 1 | 1–5 | FastAPI Fundamentals |
| 2 | 6–10 | Validation, Backend Structure, Settings & CORS |
| 3 | 11–16 | Async, Authentication & Database |
| 4 | 17–21 | AI APIs & File Processing |
| 5 | 22–25 | RAG Backend |
| 6 | 26–28 | Production Backend |
| 7 | 29–30 | Final AI Backend Project |

**Skill progression**

```
Day 1  Hello FastAPI
  ↓
Day 10 Professional REST API
  ↓
Day 16 Authenticated Database Backend
  ↓
Day 21 AI API
  ↓
Day 25 RAG Backend
  ↓
Day 28 Production Backend
  ↓
Day 30 AI Engineer Portfolio Project
```

---

## ✅ Daily Progress Tracker

Tick each day as it's completed.

### Phase 1 — FastAPI Fundamentals (Days 1–5)

- [ ] **Day 1 – FastAPI Basics**: ASGI, Uvicorn, GET/POST, Swagger UI, ReDoc · 📖 [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
  - **Task:** `GET /`, `/about`, `/health`
- [ ] **Day 2 – Path Parameters**: `/users/{user_id}` · 📖 [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
  - **Task:** `/users/{id}`, `/products/{id}`, `/ai-models/{model_name}` (AI-model lookup)
- [ ] **Day 3 – Query Parameters**: skip, limit, search, defaults · 📖 [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
  - **Task:** `/products?skip=0&limit=10`, `/search?query=python`, `/documents?search=fastapi&limit=5`
- [ ] **Day 4 – Request Body**: Pydantic `BaseModel`, JSON bodies · 📖 [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
  - **Task:** `POST /chat`, `POST /predict` (write the chat request model from memory)
- [ ] **Day 5 – Response Models + Status Codes**: `response_model`, 200/201/400/404 · 📖 [Response Model](https://fastapi.tiangolo.com/tutorial/response-model/) · [Status Codes](https://fastapi.tiangolo.com/tutorial/response-status-code/)
  - **Task:** `POST /users`, `GET /users/{id}` with correct status codes

### Phase 2 — Validation + Backend Structure (Days 6–10)

- [ ] **Day 6 – Pydantic Validation**: types, Optional, `EmailStr`, `Field` · 📖 [Body – Fields](https://fastapi.tiangolo.com/tutorial/body-fields/)
  - **Task:** `POST /register` with email, age, password rules
- [ ] **Day 7 – Error Handling**: `HTTPException` · 📖 [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
  - **Task:** return 404 when a user doesn't exist; add errors to previous APIs
- [ ] **Day 8 – Project Structure + APIRouter**: routers, schemas, models, services, utils · 📖 [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
  - **Task:** refactor into `/auth`, `/users`, `/chat` routers — only app setup in `main.py`
- [ ] **Day 9 – Settings (.env) + CORS** *(new)*: `pydantic-settings`, `CORSMiddleware` · 📖 [Settings](https://fastapi.tiangolo.com/advanced/settings/) · [CORS](https://fastapi.tiangolo.com/tutorial/cors/)
  - **Task:** `core/config.py` with a `Settings` class; allow `http://localhost:5173`; add `.env` to `.gitignore`
- [ ] **Day 10 – Dependencies**: `Depends()`, `yield` dependencies · 📖 [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) · [Dependencies with yield](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)
  - **Task:** `get_settings()` and placeholder `get_db()`; build a clean REST API without duplicated logic

### Phase 3 — Async, Authentication + Database (Days 11–16)

- [ ] **Day 11 – Async vs Sync + Lifespan + Password Hashing**: `def` vs `async def`, lifespan, `pwdlib` · 📖 [Concurrency](https://fastapi.tiangolo.com/async/) · [Lifespan Events](https://fastapi.tiangolo.com/advanced/events/)
  - **Task:** load a dummy model once in lifespan; implement `hash_password()` / `verify_password()`
- [ ] **Day 12 – Authentication Concepts**: authn vs authz, OAuth2, JWT, bearer tokens · 📖 [Security Intro](https://fastapi.tiangolo.com/tutorial/security/)
  - **Task:** design `/auth/register`, `/auth/login`, `/users/me` on paper, then stub them
- [ ] **Day 13 – JWT**: header, payload, signature, expiry · 📖 [OAuth2 with Password, Bearer with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
  - **Task:** `POST /auth/login` returns an access token; reject expired tokens
- [ ] **Day 14 – Protected Routes + First Tests**: `get_current_user`, `TestClient`, dependency overrides · 📖 [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
  - **Task:** protect `/users/me` and `/chat`; test 401 vs 200
- [ ] **Day 15 – PostgreSQL**: tables, keys, CRUD · 📖 [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)
  - **Task:** `users` table in PostgreSQL (Docker is fine); connect via Settings DB URL
- [ ] **Day 16 – SQLAlchemy + Alembic**: models, sessions, migrations · 📖 [SQLAlchemy 2.0 Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) · [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
  - **Task:** user CRUD with `get_db`; Alembic migrations
  - 🏁 **Milestone:** FastAPI + JWT + PostgreSQL working together with tests

### Phase 4 — AI APIs + File Processing (Days 17–21)

- [ ] **Day 17 – File Upload**: `UploadFile`, multipart · 📖 [Request Files](https://fastapi.tiangolo.com/tutorial/request-files/)
  - **Task:** protected `POST /documents/upload` for PDF/TXT/CSV with type & size validation
- [ ] **Day 18 – PDF Processing + Chunking**: PDF → text, cleaning, chunk size/overlap · 📖 [pypdf](https://pypdf.readthedocs.io/)
  - **Task:** return filename, page count, chunk count; experiment with sizes 300/500/800 and overlap 50/100
- [ ] **Day 19 – AI Model API**: model loading in lifespan, inference · 📖 [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
  - **Task:** `POST /predict` on a model loaded once at startup, without blocking the event loop
- [ ] **Day 20 – LLM Chat API**: `conversation_id`, history · 📖 your LLM provider SDK docs (e.g. [Anthropic](https://docs.claude.com/))
  - **Task:** `POST /chat` with stored history
- [ ] **Day 21 – Streaming**: `StreamingResponse` · 📖 [Custom Response](https://fastapi.tiangolo.com/advanced/custom-response/)
  - **Task:** `POST /chat/stream`; be able to explain why streaming improves chat UX

### Phase 5 — RAG Backend (Days 22–25)

- [ ] **Day 22 – Embeddings**: text → vector, batching, metadata · 📖 [Sentence-Transformers](https://www.sbert.net/)
  - **Task:** embed chunks; store text with `document_id`, `page`, `chunk_index`
- [ ] **Day 23 – Qdrant**: collections, vectors, payload · 📖 [Qdrant Quickstart](https://qdrant.tech/documentation/quickstart/)
  - **Task:** store embeddings with payload; run top-K search
- [ ] **Day 24 – RAG Retrieval**: top-K, score threshold, user/document filtering · 📖 [Qdrant Search](https://qdrant.tech/documentation/concepts/search/)
  - **Task:** `POST /search` scoped to the logged-in user
- [ ] **Day 25 – Complete RAG**: question → embedding → Qdrant → context → LLM
  - **Task:** `POST /chat` with retrieved context
  - 🏁 **Milestone:** working AI RAG backend

### Phase 6 — Production Backend (Days 26–28)

- [ ] **Day 26 – Redis**: caching, sessions, rate limiting · 📖 [Redis Docs](https://redis.io/docs/) · [redis-py](https://redis-py.readthedocs.io/)
  - **Task:** cache repeated search results; explain Redis vs PostgreSQL
- [ ] **Day 27 – Background Tasks**: async document processing · 📖 [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
  - **Task:** upload → respond immediately → extract/chunk/embed/store in background
  - ⚠️ Runs in the same process; for heavy jobs consider Celery or ARQ (optional)
- [ ] **Day 28 – Docker + Docker Compose** · 📖 [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/) · [Compose Docs](https://docs.docker.com/compose/)
  - **Task:** run FastAPI + PostgreSQL + Redis + Qdrant with one `docker compose up`

### Phase 7 — Final Project (Days 29–30)

- [ ] **Day 29 – Complete AI Knowledge Assistant**
  - **Task:** `/auth/register`, `/auth/login`, `/users/me`, `/documents/upload`, `/search`, `/chat`, `/chat/stream`, `/chat/history`, `/health` — working end-to-end
- [ ] **Day 30 – Tests, Production + GitHub** · 📖 [Deployment](https://fastapi.tiangolo.com/deployment/)
  - **Task:** fill test gaps (auth, users, documents, chat); write README, `.env.example`, architecture notes, screenshots; push to GitHub

> 🔗 FastAPI page paths can change between releases. If a link 404s, search the page title on [fastapi.tiangolo.com](https://fastapi.tiangolo.com/).

---

## 🏗️ Final Project: AI Knowledge Assistant

A multi-user RAG backend: upload documents, search them semantically, and chat with an LLM grounded in your own files.

### Architecture

```
            ┌──────────────┐
 Client ──▶ │   FastAPI    │ ──▶ PostgreSQL  (users, documents, chat history)
 (React)    │ JWT • CORS   │ ──▶ Redis       (cache, rate limits)
            │ Background   │ ──▶ Qdrant      (chunk embeddings + payload)
            │ Tasks        │ ──▶ LLM API     (answers using retrieved context)
            └──────────────┘
```

**RAG pipeline:** Upload → extract text → chunk → embed → store in Qdrant → (query) embed question → top-K search (filtered by user) → build context → LLM → answer.

### Endpoints

| Method | Endpoint | Description | Auth |
|:------:|----------|-------------|:----:|
| POST | `/auth/register` | Create account | ❌ |
| POST | `/auth/login` | Get JWT access token | ❌ |
| GET | `/users/me` | Current user profile | ✅ |
| POST | `/documents/upload` | Upload PDF/TXT/CSV (processed in background) | ✅ |
| POST | `/search` | Semantic search over *your* documents | ✅ |
| POST | `/chat` | RAG chat with conversation history | ✅ |
| POST | `/chat/stream` | Streaming RAG chat | ✅ |
| GET | `/chat/history` | Previous conversations | ✅ |
| GET | `/health` | Health check | ❌ |

### Suggested Project Structure

```
app/
├── main.py              # app setup only
├── core/
│   ├── config.py        # pydantic-settings
│   └── security.py      # hashing + JWT
├── api/
│   ├── deps.py          # get_db, get_current_user, get_settings
│   └── routers/         # auth.py, users.py, documents.py, chat.py
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── services/            # document processing, embeddings, qdrant, llm
└── utils/
alembic/
tests/
Dockerfile
docker-compose.yml
.env.example
requirements.txt
```

---

## 🧰 Tech Stack

| Area | Tools |
|------|-------|
| Framework | FastAPI, Uvicorn, Pydantic, pydantic-settings |
| Auth | OAuth2 password flow, JWT, pwdlib |
| Database | PostgreSQL, SQLAlchemy 2.0, Alembic |
| AI / ML | Hugging Face Transformers, Sentence-Transformers, LLM provider SDK |
| Vector DB | Qdrant |
| Caching | Redis (redis-py) |
| Files | pypdf, `UploadFile` |
| Testing | pytest, `TestClient`, dependency overrides |
| DevOps | Docker, Docker Compose |

---

## ⚙️ Getting Started

```bash
# 1. Clone
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env             # then fill in DB URL, JWT secret, API keys

# 5. Run
uvicorn app.main:app --reload
```

- Swagger UI → http://localhost:8000/docs
- ReDoc → http://localhost:8000/redoc

**Full stack with Docker (from Day 28):**

```bash
docker compose up --build
```

**Run tests (from Day 14):**

```bash
pytest -v
```

---

## ⏱️ Daily Study Pattern

| Time | Activity |
|------|----------|
| 45 min | Learn the concept |
| 60 min | Code the examples |
| 60 min | Build the feature |
| 30 min | Debug + test |
| 30 min | Challenge |
| 15 min | Write notes |

**Short on time? (≈2 hours on college days):** 30 min learn · 60 min code · 30 min project.

---

## 📝 What Changed from v1

- **Added:** Settings/`.env` + CORS (Day 9) and Lifespan events (Day 11).
- **Async moved earlier:** Day 21 → Day 11, before database and model days.
- **Merged:** old Day 8 + Day 9 (structure + APIRouter); password hashing now shares Day 11.
- **Fixed doc links:** Days 15–16 (PostgreSQL, SQLAlchemy 2.0, Alembic) and Days 19–25 (Hugging Face, Sentence-Transformers, Qdrant, Redis, LLM docs).
- **Testing spread out:** pytest starts Day 14; Day 28 is Docker only; Day 30 closes test gaps.
- **Smaller fixes:** Day 3 typo, `/documents` protected only once it exists (Day 17), chunk size/overlap (Day 18), BackgroundTasks limits (Day 27), per-user Qdrant scoping (Day 24).

---

## 📚 Notes & Learnings

Use a `notes/` folder with one file per day (`notes/day-01.md`, …) covering: what I learned, what broke, how I fixed it, and one thing to revisit.

---

## 🤝 Contributing

This is a personal learning repo, but suggestions and corrections are welcome — open an issue or PR.


---

⭐ If this roadmap helps you, star the repo and follow along!
