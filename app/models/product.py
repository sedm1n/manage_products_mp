from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime, func, Computed
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric,default=0,  nullable=False)
    stock = Column(Integer, default=0, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    
    category = relationship("Category", backref="products")

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, category_id={self.category_id})>"

