from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

app = FastAPI(title="INCLUA – IA Demo (Docker)", version="1.0.0")

TRAIN_TEXTS = [
    "atendimento igualitário e sem discriminação",
    "barreiras de acesso e tratamento desigual",
    "serviço público acolhedor e inclusivo",
    "discriminação institucional e estigmatização",
]
LABELS = [1, 0, 1, 0]

pipeline: Pipeline = Pipeline([
    ("vect", CountVectorizer()),
    ("clf", LogisticRegression(max_iter=1000)),
])

pipeline.fit(TRAIN_TEXTS, LABELS)

class PredictOut(BaseModel):
    label: str
    score: float

@app.get("/predict", response_model=PredictOut)
async def predict(text: Optional[str] = None):
    if not text:
        raise HTTPException(status_code=400, detail="Parametro 'text' é obrigatório")
    proba = pipeline.predict_proba([text])[0]
    label_idx = int(proba.argmax())
    label = "inclusivo" if label_idx == 1 else "risco"
    score = float(proba[label_idx])
    return PredictOut(label=label, score=score)
