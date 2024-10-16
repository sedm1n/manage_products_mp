from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime, func, Computed
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=True)
    fullname = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)

    shipping_addresses = relationship("ShippingAddress", back_populates="user") 
    orders = relationship("Order", back_populates="user")  
