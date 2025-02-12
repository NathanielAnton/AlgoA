from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280), nullable=False) 
    positive = db.Column(db.Boolean, default=False)  
    negative = db.Column(db.Boolean, default=False)  
