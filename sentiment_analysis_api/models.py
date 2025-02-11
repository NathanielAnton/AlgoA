import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    positive = db.Column(db.Boolean, nullable=False)
    negative = db.Column(db.Boolean, nullable=False)

def load_training_data():
    tweets = Tweet.query.all()
    texts = [tweet.text for tweet in tweets]
    labels = [1 if tweet.positive else 0 for tweet in tweets]  # 1 = Positif, 0 = Négatif
    
    return texts, labels
