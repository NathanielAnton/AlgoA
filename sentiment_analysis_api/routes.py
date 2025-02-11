from flask import Blueprint, request, jsonify
from models import db, Tweet

api_bp = Blueprint('api', __name__)

@api_bp.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'GET':
        return jsonify({"message": "Utilisez une requête POST avec des tweets."}), 400

    data = request.json
    tweets = data.get("tweets", [])
    response = {tweet: 0 for tweet in tweets}  # Score neutre temporaire
    return jsonify(response)
