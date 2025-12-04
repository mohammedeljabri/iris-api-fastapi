# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Charger les données
data = load_iris()
X = data.data
y = data.target

# Entraîner un modèle simple
model = RandomForestClassifier()
model.fit(X, y)

# Sauvegarder le modèle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Modèle entraîné et sauvegardé sous model.pkl")
