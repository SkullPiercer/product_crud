from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.product import ProductCreate, ProductDB

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
    await check_name_duplicate(project.name, session)
    new_product = await projects_crud.create(project, session)

    return new_project