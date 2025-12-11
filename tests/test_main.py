# tests/test_main.py
import sys, os
# ajoute le dossier parent (racine du projet) au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2})
    assert response.status_code == 200
    assert "prediction" in response.json()
