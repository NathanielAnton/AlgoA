from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@host.docker.internal/socialmetrics'


db = SQLAlchemy(app)

# Importer après l'initialisation de db pour éviter les erreurs circulaires
from routes import api_bp
app.register_blueprint(api_bp)  # ⚠️ Cette ligne est essentielle

@app.route('/')
def home():
    return "L'API d'analyse de sentiments fonctionne ! 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

