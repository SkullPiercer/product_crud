from app.crud.base import CRUDBase
from app.models import Product


class CRUDProducts(CRUDBase):
    pass


donation_crud = CRUDProducts(Product)
