# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Charger le modèle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Iris Model API")


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def root():
    return {"message": "API prête !"}


@app.post("/predict")
def predict(features: IrisFeatures):
    X = np.array(
        [
            [
                features.sepal_length,
                features.sepal_width,
                features.petal_length,
                features.petal_width,
            ]
        ]
    )

    pred = model.predict(X)[0]
    return {"prediction": int(pred)}
