from app.db.base import Base
from sqlalchemy import Column, Integer, String


class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
