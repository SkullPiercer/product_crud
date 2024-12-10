from typing import Optional

from pydantic import BaseModel, Field, root_validator, validator

from app.core.constants import (
    DESCRIPTION_MIN_LEN, PRODUCT_NAME_MAX_LEN, PRODUCT_NAME_MIN_LEN, PRICE_GT
)


class ProductCreate(BaseModel):
    name: str = Field(
        min_length=PRODUCT_NAME_MIN_LEN,
        max_length=PRODUCT_NAME_MAX_LEN
    )
    price: float = Field(min_length=DESCRIPTION_MIN_LEN)
    description: str = Field(min_length=DESCRIPTION_MIN_LEN)
    category: str = Field(..., gt=PRICE_GT)

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
