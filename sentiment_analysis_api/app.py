import joblib
from flask import Flask, request, jsonify
from models import db, Tweet  # Assure-toi que Tweet est bien importé
from sklearn.feature_extraction.text import CountVectorizer

# Charger ton modèle et le vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Création de l'application Flask
app = Flask(__name__)

# Configure la base de données
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user:password@localhost:3306/sentiment_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()

    if not data or 'tweets' not in data:
        return jsonify({"error": "No tweets provided"}), 400

    tweets = data['tweets']
    sentiments = {}

    # Vectorisation des tweets
    X = vectorizer.transform(tweets)

    # Prédiction des scores de probabilité (valeurs continues entre 0 et 1)
    probs = model.predict_proba(X)

    # Calcul des scores de sentiment entre -1 et 1
    for i, tweet in enumerate(tweets):
        # La classe 1 est la classe positive, on utilise la probabilité pour la classe positive
        sentiment_score = 2 * probs[i][1] - 1  # Transformer la probabilité en score entre -1 et 1
        sentiments[f"tweet{i+1}"] = round(sentiment_score, 2)  # Arrondir le score pour une présentation plus propre

    return jsonify(sentiments)

if __name__ == "__main__":
    app.run(debug=True)
