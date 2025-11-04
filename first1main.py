import os

import uv

# from app.core.config import settings
# from app.core.logging import get_logger
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "Todo App API"),
    version=os.getenv("APP_VERSION", "0.1.0"),
    description=os.getenv("APP_DESCRIPTION", "A simple FastAPI application"),
    debug=bool(os.getenv("APP_DEBUG", True)),
)

# Log configuration source on startup

logger = get_logger(__name__)
logger.info(f"🔧 Configuration: {settings.config_source}")


@app.get("/health")
async def health() -> dict:
    return {
        "status": "healthy",
        "app_name": os.getenv("APP_NAME", "Todo App API"),
        "version": os.getenv("APP_VERSION", "0.1.0"),
    }


if __name__ == "__main__":
    uv.run(
        app,
        host=os.getenv("APP_HOST", "127.0.0.1"),
        port=os.getenv("APP_PORT", "8000"),
        reload=os.getenv("APP_RELOAD", True),
    )
