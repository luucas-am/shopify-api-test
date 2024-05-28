from fastapi import APIRouter

from src.api.service import ProductsService

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", status_code=200)
async def get_all_orders():
    return ProductsService.get_all()
