import json

from saleApp.saleapp import db, app
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class  Base(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)

class Category(Base):
    products = relationship('Product', backref="category", lazy=True)
    def __str__(self):
        return self.name

class Product(Base):
    image = Column(String(500), default="https://e7.pngegg.com/pngimages/10/205/png-clipart-computer-icons-error-information-error-angle-triangle-thumbnail.png")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__=="__main__":
    with app.app_context():
        # db.create_all()
        c1 = Category(name="Laptop")
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet")
        #
        # db.session.add_all([c1,c2,c3])

        # with open("saleApp/data/product.json", encoding="utf-8") as f:
        #     products = json.load(f)
        #
        #     for p in products:
        #         db.session.add(Product(**p))
        #
        # db.session.commit()

