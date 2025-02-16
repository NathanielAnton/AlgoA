from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import mysql.connector
import pickle
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Connexion à la base de données MySQL
db_connection = mysql.connector.connect(
    host="127.0.0.1",  
    port=3307,  # Port correct selon docker ps
    user="root",
    password="rootpassword",
    database="sentiment_db"
)

cursor = db_connection.cursor()

# Fonction pour récupérer les données les plus récentes
def get_latest_data():
    query = "SELECT text, positive, negative FROM tweet ORDER BY id DESC LIMIT 100"
    cursor.execute(query)
    rows = cursor.fetchall()

    texts = [row[0] for row in rows]
    labels = [(row[1], row[2]) for row in rows]

    print(f"Nombre de tweets : {len(texts)}")
    print(f"Nombre de labels : {len(labels)}")

    if len(texts) != len(labels):
        raise ValueError("Le nombre de tweets ne correspond pas au nombre de labels.")

    return texts, labels

# Fonction pour afficher et sauvegarder une matrice de confusion
def plot_confusion_matrix(cm, title, filename):
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Négatif', 'Positif'], yticklabels=['Négatif', 'Positif'])
    plt.title(title)
    plt.xlabel("Prédictions")
    plt.ylabel("Véritables Labels")
    plt.savefig(filename)  # Sauvegarde en image
    plt.show()

# Fonction pour réentraîner le modèle
def retrain_model():
    texts, labels = get_latest_data()

    if len(texts) == 0:
        print("⚠️ Pas de nouvelles données pour réentraîner le modèle.")
        return
    
    print(f"🔄 Réentraînement avec {len(texts)} nouveaux tweets.")

    y = [1 if label[0] == 1 else 0 for label in labels]  # 1 = Positif, 0 = Négatif
    vectorizer = TfidfVectorizer(stop_words='english')

    # Charger l'ancien modèle et le vectorizer si disponibles
    try:
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        with open("sentiment_model.pkl", "rb") as f:
            model = pickle.load(f)
        print("✅ Ancien modèle chargé.")
    except FileNotFoundError:
        print("⚠️ Aucun modèle précédent trouvé, entraînement d'un nouveau modèle.")
        model = LogisticRegression(class_weight='balanced')

    X = vectorizer.fit_transform(texts)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Rapport de classification
    print("### Rapport de Classification ###")
    report = classification_report(y_test, y_pred)
    print(report)

    # Calcul et affichage de la matrice de confusion globale
    cm_global = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cm_global, "Matrice de Confusion Globale", "confusion_matrix_global.png")

    # Extraire les vraies et fausses prédictions
    true_positives = cm_global[1, 1]  # Bien classé comme positif
    false_negatives = cm_global[1, 0]  # Classé négatif mais était positif
    false_positives = cm_global[0, 1]  # Classé positif mais était négatif
    true_negatives = cm_global[0, 0]  # Bien classé comme négatif

    # Matrice pour les prédictions positives
    cm_positive = [[0, false_negatives], [0, true_positives]]
    plot_confusion_matrix(cm_positive, "Matrice de Confusion - Classe Positive", "confusion_matrix_positive.png")

    # Matrice pour les prédictions négatives
    cm_negative = [[true_negatives, 0], [false_positives, 0]]
    plot_confusion_matrix(cm_negative, "Matrice de Confusion - Classe Négative", "confusion_matrix_negative.png")

    # Sauvegarde du modèle et du vectorizer
    with open("sentiment_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("✅ Nouveau modèle sauvegardé.")

if __name__ == "__main__":
    retrain_model()
