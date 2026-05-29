from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, admin, categories, chapters, problems, progress, solutions
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(categories.router)
app.include_router(chapters.router)
app.include_router(problems.router)
app.include_router(progress.router)
app.include_router(solutions.router)


@app.get("/")
def root():
    return {"message": settings.APP_NAME, "status": "running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/client-ip")
def client_ip():
    return {"ip": "10.3.121.36"}
