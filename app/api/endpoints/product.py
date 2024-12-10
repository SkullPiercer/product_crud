from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_name_duplicate, check_product_exists
from app.core.db import get_async_session
from app.crud.product import product_crud
from app.models import Product
from app.schemas.product import ProductCreate, ProductDB, ProductUpdate

router = APIRouter()


@router.post(
    '/',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def create_new_product(
        product: ProductCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(product.name, session)
    return await product_crud.create(product, session)


@router.delete(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def remove_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    product = await check_product_exists(product_id, session)
    return await product_crud.remove(product, session)


@router.get(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def get_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    await check_product_exists(product_id, session)
    return await product_crud.get(product_id, session)


@router.get(
    '/',
    response_model=list[ProductDB],
    response_model_exclude_none=True,
)
async def get_all_product(
        session: AsyncSession = Depends(get_async_session),
) -> list[Product]:
    return await product_crud.get_multi(session=session)


@router.patch(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def partially_update_product(
        product_id: int,
        obj_in: ProductUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    product = await check_product_exists(product_id, session)

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    return await product_crud.update(product, obj_in, session)
