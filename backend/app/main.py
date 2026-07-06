from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.core.config import settings

from app.db.base import Base
from app.db.session import engine, get_db

from app.models.client import Client
from app.models.event import Event
from app.models.feedback import Feedback

from app.api.routes.opportunities import router as opportunities_router


# -----------------------------
# CREATE TABLES
# -----------------------------
Base.metadata.create_all(bind=engine)


# -----------------------------
# APP INIT
# -----------------------------
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)


# -----------------------------
# CORS (MUST COME BEFORE ROUTES)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# ROUTES
# -----------------------------
app.include_router(opportunities_router)


# -----------------------------
# BASIC ENDPOINTS
# -----------------------------
@app.get("/")
def root():
    return {
        "project": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -----------------------------
# DEBUG DATASET ENDPOINT
# -----------------------------
@app.get("/debug/dataset")
def get_dataset(db: Session = Depends(get_db)):
    return db.query(Client).all()