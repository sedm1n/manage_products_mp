from sqlalchemy import Boolean, ForeignKey, Integer, String,CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.backend.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    username: Mapped[str] = mapped_column(
        String(), unique=True, index=True, nullable=False
    )
    fullname: Mapped[str] = mapped_column(String(), nullable=True)
    
    email: Mapped[str] = mapped_column(
        String(), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(), nullable=False)
    
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    is_supplier: Mapped[bool] = mapped_column(Boolean(), default=False)
    is_customer: Mapped[bool] = mapped_column(Boolean(), default=True)

    shipping_addresses = relationship("ShippingAddress", back_populates="user")

    orders = relationship("Order", back_populates="user")
    
    def __repr__(self):
        return f"<User(name={self.username}, email={self.email}, is_active={self.is_active})>"
    
    __table_args__ = (
        CheckConstraint("LENGTH(username) >= 3", name="username_min_length"),
        CheckConstraint("LENGTH(email) > 4", name="email_min_length"),
        CheckConstraint("LENGTH(hashed_password) > 4", name="hashed_password"),  
    )
    

class ShippingAddress(Base):
    __tablename__ = "shipping_addresses"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    address: Mapped[str] = mapped_column(String(150), nullable=False)
    user_id: Mapped[int] = mapped_column(
        Integer(), ForeignKey("users.id"), nullable=False
    )

    user = relationship("User", back_populates="shipping_addresses")
