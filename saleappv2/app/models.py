from sqlalchemy import Column, Integer, String
from app import db 

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

if __name__ == '__main__':
    from . import app #app nay la bien cua db = SQLAlchemy(app=app)
    with app.app_context():
        db.create_all()