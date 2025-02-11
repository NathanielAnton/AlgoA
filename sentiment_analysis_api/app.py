from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Importer après l'initialisation de db pour éviter les erreurs circulaires
from routes import api_bp
app.register_blueprint(api_bp)  # ⚠️ Cette ligne est essentielle

@app.route('/')
def home():
    return "L'API d'analyse de sentiments fonctionne ! 🚀"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
