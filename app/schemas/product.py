from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, validator

from app.core.constants import (
    CATEGORY_MAX_LEN,
    CATEGORY_MIN_LEN,
    DESCRIPTION_MIN_LEN,
    MAX_PRICE,
    MIN_PRICE,
    PRODUCT_NAME_MAX_LEN,
    PRODUCT_NAME_MIN_LEN,
)


class ProductCreate(BaseModel):
    name: str = Field(
        min_length=PRODUCT_NAME_MIN_LEN,
        max_length=PRODUCT_NAME_MAX_LEN
    )
    price: Decimal = Field(ge=MIN_PRICE, le=MAX_PRICE)
    description: str = Field(min_length=DESCRIPTION_MIN_LEN)
    category: str = Field(
        min_length=CATEGORY_MIN_LEN,
        max_length=CATEGORY_MAX_LEN
    )

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя товара не может быть пустым!')
        return value

    @validator('description')
    def desc_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Описание товара не может быть пустым!')
        return value


class ProductDB(ProductCreate):
    id: int

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(
        min_length=PRODUCT_NAME_MIN_LEN,
        max_length=PRODUCT_NAME_MAX_LEN
    )
    price: Optional[Decimal] = Field(ge=MIN_PRICE, le=MAX_PRICE)
    description: Optional[str] = Field(min_length=DESCRIPTION_MIN_LEN)
    category: Optional[str] = Field(
        min_length=CATEGORY_MIN_LEN,
        max_length=CATEGORY_MAX_LEN
    )
