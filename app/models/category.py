from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime, func, Computed
from sqlalchemy.orm import relationship



class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    parent_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=True)

    
    parent = relationship("Category", remote_side=[id], backref="subcategories")

    def __repr__(self):
        return f"<Category(name={self.name}, parent_id={self.parent_id})>"

    