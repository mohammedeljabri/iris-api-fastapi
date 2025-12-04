# Étape 1 : choisir l'image Python
FROM python:3.10-slim

# Étape 2 : définir un dossier de travail
WORKDIR /app

# Étape 3 : copier les fichiers nécessaires
COPY requirements.txt .
COPY app.py .
COPY model.pkl .
COPY train_model.py .

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : exposer le port (important pour le cloud)
EXPOSE 8000

# Étape 6 : lancer l'application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
