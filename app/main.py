from fastapi import FastAPI

from app.config import settings
from app.logger import logger

from api.legal_health import router as legal_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Register API Routers
app.include_router(legal_router)


@app.get("/")
def root():
    logger.info("Root endpoint accessed.")

    return {
        "message": "Welcome to THEMIS AI Engine"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }