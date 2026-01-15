from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from typing import Optional

app = FastAPI(title="NLP Deployment Demo")

class InputText(BaseModel):
    text: str

MODEL_PATH = "nlp_model.joblib"

@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        model = None

@app.post("/predict")
def predict(input: InputText):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Train model first.")
    pred = model.predict([input.text])[0]
    return {"prediction": int(pred)}

@app.get("/health")
def health():
    return {"status": "ok"}