from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate
from app.db.session import get_db

router = APIRouter(prefix="/feedbacks")


@router.get("/", status_code=status.HTTP_201_CREATED)
def get_feedbacks(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).order_by(Feedback.id).all()
    return [feedback.message for feedback in feedbacks]


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_feedback(feedback_data: FeedbackCreate, db: Session = Depends(get_db)):
    new_feedback = Feedback(**feedback_data.model_dump())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return {"message": "Feedback added successfully!"}
