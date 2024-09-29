from fastapi import FastAPI
import logging
from routers.feedback import router as feedback_router
from init import setup_db
from contextlib import asynccontextmanager

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_db.init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(feedback_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
