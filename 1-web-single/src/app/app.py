import os
from logging import getLogger

from fastapi import FastAPI

logger = getLogger(__name__)

app = FastAPI(
    title="ServingPattern",
    description="web single paattern",
    version="0.1"
)

app.include_router(routers.router, prefix="", tags=[""])