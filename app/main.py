import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.routes import user, tasks

app = FastAPI(title="Task Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(tasks.router)

_HTML_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "frontend", "index.html"
)

@app.get("/")
def root():
    try:
        with open(_HTML_PATH, "r") as f:
            return HTMLResponse(f.read())
    except Exception:
        return HTMLResponse("<h1>Task Manager API</h1><p>Visit <a href='/docs'>/docs</a></p>")
