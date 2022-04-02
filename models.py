# from app import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Images(db.Model):
    __tablename__="images"
    id=db.Column(db.Integer,primary_key=True)
    timestamp=db.Column(db.DateTime,nullable=False)
    image_link=db.Column(db.String,nullable=False)
    
    def __init__(self,timestamp,image_link):
        self.timestamp=timestamp
        self.image_link=image_link
