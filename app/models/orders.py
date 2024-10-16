from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime, func, Computed
from sqlalchemy.orm import relationship



class ShippingAddress(Base):
    __tablename__ = "shipping_addresses"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="shipping_addresses") 

    

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    shipping_address_id = Column(Integer, ForeignKey("shipping_addresses.id"), nullable=False)
    amount = Column(Numeric, nullable=False)
    paid = Column(Boolean, default=False, nullable=False)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now()) 

    order_items = relationship("OrderItem", backref="order")
    user = relationship("User", back_populates="orders")  

    @property
    def total_amount(self):
        return sum(item.total_cost for item in self.order_items)

    

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)  
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    price = Column(Numeric, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    total_cost = Column(Numeric, Computed("price * quantity"))
   
    product_relationship = relationship("Product", backref="order_items")
