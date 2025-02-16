# Sentiment Analysis API

Ce dépôt contient une API de détection des sentiments basée sur une régression logistique. L'API permet d'analyser des tweets et de déterminer leur polarité (positive ou négative).

## Installation et exécution

### 1. Cloner le dépôt
```bash
git clone https://github.com/NathanielAnton/AlgoA.git
```


### 2. Lancer l'Api Flask
```bash
cd .\sentiment_analysis_api\
```

Il faudra se mettre dans l'environnement virtuel donc effectuer ces commandes

Pour macOS/Linux :
```bash
.\venv\bin\activate
```
Pour Windows :
```bash
.\venv\Scripts\activate
```

Ensuite on pourra lancer l'api via la commande :

```bash
python app.py
```

### 3. Réentraîner le modèle de Machine Learning

Si vous souhaitez réentraîner le modèle avec de nouvelles données, suivez ces étapes :

Démarrer les services Docker (MySQL)
```bash
docker-compose up -d
```

Activer l'environnement virtuel

Refaites l'étape 3 mentionnée plus haut pour activer l'environnement virtuel.

Exécuter le script de réentraînement du modèle
```bash
python ml_model.py
```