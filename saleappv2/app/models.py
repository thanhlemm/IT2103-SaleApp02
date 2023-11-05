from sqlalchemy import Column, Integer, String
from saleappv2.app import db


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)


if __name__ == '__main__':
    from saleappv2.app import app  # app nay la bien cua db = SQLAlchemy(app=app)

    with app.app_context():
        db.create_all()
