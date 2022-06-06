from fastapi import APIRouter
from src.endpoins import language, menu

router = APIRouter()
router.include_router(language.router)
router.include_router(menu.router)