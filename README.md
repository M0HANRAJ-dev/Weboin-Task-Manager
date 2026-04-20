# Task Manager – FastAPI

A full-stack Task Manager built with FastAPI backend, SQLite database, JWT authentication, and a plain HTML/JS frontend.

- **GitHub:** https://github.com/M0HANRAJ-dev/Weboin-Task-Manager
- **Live Demo:** _Add after deploying to Render/Railway_
- **API Docs:** `<your-url>/docs`

---

## Project Structure

```
Weboin-Task-Manager/
├── app/
│   ├── routes/
│   │   ├── tasks.py       # Task CRUD endpoints
│   │   └── user.py        # Register & Login
│   ├── utils/
│   │   └── security.py    # Password hashing
│   ├── auth.py            # JWT creation & verification
│   ├── database.py        # DB engine & session
│   ├── main.py            # App entry point
│   ├── models.py          # SQLAlchemy models
│   └── schemas.py         # Pydantic schemas
├── frontend/
│   └── index.html         # Single-page UI
├── tests/
│   ├── conftest.py        # Test fixtures
│   └── test_main.py       # Pytest test cases
├── .env.example
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in values:

```
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./test.db
```

> ⚠️ Never commit your `.env` file. It is listed in `.gitignore`.

---

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/M0HANRAJ-dev/Weboin-Task-Manager.git
cd Weboin-Task-Manager

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment
cp .env.example .env
# Edit .env with your values

# 5. Start the server
uvicorn app.main:app --reload
```

- UI: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## Run Tests

```bash
pytest tests/ -v
```

13 test cases covering: registration, login, task CRUD, filtering, pagination, and auth protection.

---

## Run with Docker

```bash
docker build -t task-manager .
docker run -p 8000:8000 --env-file .env task-manager
```

---

## API Endpoints

| Method | Endpoint      | Auth | Description                        |
|--------|---------------|------|------------------------------------|
| POST   | /register     | No   | Register a new user                |
| POST   | /login        | No   | Login and receive JWT token        |
| POST   | /tasks/       | Yes  | Create a task                      |
| GET    | /tasks/       | Yes  | List tasks (paginated, filterable) |
| GET    | /tasks/{id}   | Yes  | Get a single task                  |
| PUT    | /tasks/{id}   | Yes  | Update task (title/desc/completed) |
| DELETE | /tasks/{id}   | Yes  | Delete a task                      |

### Query Parameters for `GET /tasks/`

| Parameter          | Description                  |
|--------------------|------------------------------|
| `?completed=true`  | Filter completed tasks only  |
| `?completed=false` | Filter pending tasks only    |
| `?skip=0`          | Pagination offset            |
| `?limit=10`        | Pagination page size (max 100) |

---

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, SQLite
- **Auth:** JWT (python-jose), bcrypt (passlib)
- **Frontend:** Plain HTML + CSS + JavaScript
- **Tests:** Pytest + HTTPX TestClient
- **Deployment:** Docker-ready
