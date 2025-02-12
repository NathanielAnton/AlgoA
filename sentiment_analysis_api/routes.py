from flask import Blueprint, request, jsonify
from ml_model import predict_sentiment, get_session

# Création du blueprint Flask
api_bp = Blueprint('api', __name__)

@api_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    tweets = data.get("tweets", [])

    if not isinstance(tweets, list) or not all(isinstance(t, str) for t in tweets):
        return jsonify({"error": "❌ Entrée invalide. Envoyez une liste de textes."}), 400

    response = predict_sentiment(tweets)
    return jsonify(response)
