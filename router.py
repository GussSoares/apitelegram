from fastapi import APIRouter
from api.webhook import router as webhook

router = APIRouter()

router.include_router(prefix='/api', router=webhook)