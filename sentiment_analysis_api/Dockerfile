# Utiliser une image de base avec Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par Flask (5000)
EXPOSE 5000

# Définir la commande à exécuter lorsque le conteneur démarre
CMD ["python", "app.py"]
