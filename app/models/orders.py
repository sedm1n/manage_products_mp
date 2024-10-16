from sqlalchemy import (Boolean, Computed, DateTime, ForeignKey, Integer,
                        Numeric, String, func, mapped_column, Mapped)
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Order(Base):
    __tablename__ = "orders"

    id:Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    user_id:Mapped[int] = mapped_column(Integer(), ForeignKey("users.id"), nullable=False)
    shipping_address_id:Mapped[int] = mapped_column(Integer(), ForeignKey("shipping_addresses.id"), nullable=False)
    amount:Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    paid:Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created:Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated:Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now()) 

    order_items:Mapped[List["OrderItem"]] = relationship("OrderItem", backref="order")
    user:Mapped["User"] = relationship("User", back_populates="orders")  

    @property
    def total_amount(self)->Numeric:
        return sum(item.total_cost for item in self.order_items)

    

class OrderItem(Base):
    __tablename__ = "order_items"

    id:Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    order_id:Mapped[int] = mapped_column(Integer(), ForeignKey("orders.id"), nullable=False)  
    product_id:Mapped[int] = mapped_column(Integer(), ForeignKey("products.id"), nullable=False)
    price:Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    quantity:Mapped[int] = mapped_column(Integer(), default=1, nullable=False)
    total_cost:Mapped[Numeric] = mapped_column(Numeric, Computed("price * quantity"))
   
    product:Mapped["Product"] = relationship("Product", backref="order_items")
