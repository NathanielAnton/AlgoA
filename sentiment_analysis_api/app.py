import joblib
from flask import Flask, request, jsonify
from models import db, Tweet  # Assure-toi que Tweet est bien importé
from sklearn.feature_extraction.text import CountVectorizer

# Charger ton modèle et le vectorizer
try:
    model = joblib.load("sentiment_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except FileNotFoundError:
    # Si les fichiers ne sont pas trouvés, retourner une erreur
    model = None
    vectorizer = None

# Création de l'application Flask
app = Flask(__name__)

# Configure la base de données
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user:password@localhost:3306/sentiment_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    # Vérification que la requête contient des données JSON
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400

    # Vérification que les tweets sont présents dans les données
    if not data or 'tweets' not in data:
        return jsonify({"error": "No 'tweets' key in the request data"}), 400

    tweets = data['tweets']

    # Vérification que la liste de tweets est non vide et que chaque élément est une chaîne de caractères
    if not tweets:
        return jsonify({"error": "The list of tweets is empty"}), 400
    if not all(isinstance(tweet, str) for tweet in tweets):
        return jsonify({"error": "All tweets must be strings"}), 400

    if model is None or vectorizer is None:
        return jsonify({"error": "Model or vectorizer is missing"}), 500

    sentiments = {}

    try:
        # Vectorisation des tweets
        X = vectorizer.transform(tweets)

        # Prédiction des scores de probabilité (valeurs continues entre 0 et 1)
        probs = model.predict_proba(X)

        # Calcul des scores de sentiment entre -1 et 1
        for i, tweet in enumerate(tweets):
            # La classe 1 est la classe positive, on utilise la probabilité pour la classe positive
            sentiment_score = 2 * probs[i][1] - 1  # Transformer la probabilité en score entre -1 et 1
            sentiments[f"tweet{i+1}"] = round(sentiment_score, 2)  # Arrondir le score pour une présentation plus propre

    except Exception as e:
        return jsonify({"error": f"Error during sentiment analysis: {str(e)}"}), 500

    return jsonify(sentiments)

if __name__ == "__main__":
    app.run(debug=True)
