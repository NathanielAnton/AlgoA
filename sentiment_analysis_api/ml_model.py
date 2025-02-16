from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import mysql.connector
import pickle

# Connexion à la base de données MySQL
db_connection = mysql.connector.connect(
    host="127.0.0.1",  # Utilisation de localhost
    port=3307,  # Port correct selon docker ps
    user="root",
    password="rootpassword",
    database="sentiment_db"
)

cursor = db_connection.cursor()

# Fonction pour récupérer les données
def get_data():
    cursor.execute("SELECT text, positive, negative FROM tweet WHERE text IS NOT NULL AND text != ''")
    rows = cursor.fetchall()

    texts = [row[0] for row in rows]
    labels = [(row[1], row[2]) for row in rows]

    # Vérification des longueurs
    print(f"Nombre de tweets : {len(texts)}")
    print(f"Nombre de labels : {len(labels)}")

    # Vérification de l'alignement des données
    if len(texts) != len(labels):
        raise ValueError("Le nombre de tweets ne correspond pas au nombre de labels.")

    return texts, labels

# Préparation et entraînement du modèle
def train_model():
    texts, labels = get_data()

    # Séparation des labels en classes positives et négatives
    y = [1 if label[0] == 1 else 0 for label in labels]  # Sentiment positif
    y_neg = [1 if label[1] == 1 else 0 for label in labels]  # Sentiment négatif

    # Transformation des textes en vecteurs TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    print(f"Nombre de features après vectorisation : {X.shape[1]}")

    # Séparation des données en ensemble d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Création et entraînement du modèle
    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train, y_train)

    # Prédictions et évaluation
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Sauvegarde du modèle
    with open("sentiment_model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)

    # Sauvegarde du vectoriseur
    with open("vectorizer.pkl", "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

if __name__ == "__main__":
    train_model()
