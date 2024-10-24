from fastapi import APIRouter
from services import db, feedback

router = APIRouter(prefix="/api", tags=["feedback"])

@router.post("/feedback/{teacher_id}/{assignment_id}", response_model=dict)
async def generate_feedback(writing_sample: str, teacher_id: int, assignment_id: int):
    db_connection = db.get_db_connection()
    generated_feedback = feedback.generate_feedback(writing_sample)
    db.insert_essay(writing_sample, generated_feedback, teacher_id, assignment_id, db_connection)
    return {"feedback": generated_feedback}


@router.get("/feedback/{teacher_id}/{assignment_id}", response_model=dict)
async def get_feedback(teacher_id: int, assignment_id: int):
    db_connection = db.get_db_connection()
    essays = db.get_essay(teacher_id, assignment_id, db_connection)
    return {"feedback": essays}