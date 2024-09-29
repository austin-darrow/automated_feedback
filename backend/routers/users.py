from fastapi import APIRouter
from services import db

router = APIRouter(prefix="/api", tags=["users"])

@router.post("/users", response_model=dict)
async def create_user(email: str, password_hash: str):
    db_connection = db.get_db_connection()
    db.create_user(email, password_hash, db_connection)
    return {"email": email}