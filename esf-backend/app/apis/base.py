from app.apis import feedback_routes
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(feedback_routes.router, tags=["feedback"])
