from fastapi import APIRouter
from api.webhook import router as webhook
from api.telegram import router as telegram

router = APIRouter()

router.include_router(prefix='/api', router=webhook)
router.include_router(prefix='/telegram', router=telegram)