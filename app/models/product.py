from sqlalchemy import Boolean, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.backend.db import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    price: Mapped[Numeric] = mapped_column(Numeric, default=0, nullable=False)
    stock: Mapped[int] = mapped_column(Integer(), default=0, nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    image_url: Mapped[str] = mapped_column(String(200), nullable=True)
    rating: Mapped[Numeric] = mapped_column(Numeric, default=0, nullable=False)
    supplier_id: Mapped[int] = mapped_column(
        Integer(), ForeignKey("users.id"), nullable=True
    )

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    category_id: Mapped[int] = mapped_column(
        Integer(), ForeignKey("categories.id"), nullable=False
    )
    category: Mapped["Category"] = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, category_id={self.category_id})>"
