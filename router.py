from fastapi import APIRouter

from api.telegram.endpoints import router as telegram
from api.webhook import router as webhook

router = APIRouter()

router.include_router(prefix="/api", router=webhook)
router.include_router(prefix="/telegram", router=telegram)
