from typing import List, Optional

from backend.db import Base
from sqlalchemy import (Boolean, Computed, DateTime, ForeignKey, Integer,
                        Numeric, String, func, mapped_column)
from sqlalchemy.orm import Mapped, mapped_mapped_column, relationship


class Category(Base):
    __tablename__ = "categories"

    id:Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    parent_id:Mapped[Optional[int]] = mapped_column(Integer(), ForeignKey("categories.id", ondelete="CASCADE"), nullable=True)
    slug:Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    is_active:Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    
    products:Mapped[List["Product"]] = relationship("Product", back_populates="category")
    
    def __repr__(self):
        return f"<Category(name={self.name}, parent_id={self.parent_id})>"

    