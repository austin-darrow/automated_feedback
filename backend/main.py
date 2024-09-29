from fastapi import FastAPI
import logging
from routers.feedback import router as feedback_router

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(feedback_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
