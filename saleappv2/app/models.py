from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from saleappv2.app import db


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    from saleappv2.app import app  # app nay la bien cua db = SQLAlchemy(app=app)

    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)

        p1 = Product(name='iPhone 13', price=22000000, category_id=1, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU")
        p2 = Product(name='iPad Pro 2022', price=24000000, category_id=2, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU")
        p3 = Product(name='iPhone 13', price=27000000, category_id=1, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU")
        p4 = Product(name='Note 23+', price=22000000, category_id=1, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU")
        p5 = Product(name='Galaxy Tab 9', price=22000000, category_id=2, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU")
        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
        #db.create_all()
