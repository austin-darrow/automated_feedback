from fastapi import FastAPI
import logging
import logging.config
import setup_db
from contextlib import asynccontextmanager
# CORS
from fastapi.middleware.cors import CORSMiddleware


from routers.assignments import router as assignments_router
from routers.feedback import router as feedback_router
from routers.users import router as users_router

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_db.init_db()
    yield

app = FastAPI(lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(assignments_router)
app.include_router(feedback_router)
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
