from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["feedback"])

@router.post("/feedback/{teacher_id}/{assignment_id}", response_model=dict)
async def generate_feedback(writing_sample: str, teacher_id: int, assignment_id: int):
    return {"feedback": f"Teacher {teacher_id}, a student wrote the following for {assignment_id}:\n{writing_sample}\n\n Great job!"}