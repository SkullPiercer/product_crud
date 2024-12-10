from sqlalchemy import Column, Numeric, String, Text

from app.core.constants import (
    CATEGORY_MAX_LEN, PRICE_PRECISION, PRICE_SCALE, PRODUCT_NAME_MAX_LEN
)
from app.core.db import Base


class Product(Base):
    name = Column(
        String(PRODUCT_NAME_MAX_LEN),
        unique=True,
        nullable=False
    )
    price = Column(
        Numeric(PRICE_PRECISION, PRICE_SCALE),
        nullable=False
    )
    description = Column(
        Text,
        nullable=False
    )
    category = Column(
        String(CATEGORY_MAX_LEN),
        nullable=False
    ) # Enum
