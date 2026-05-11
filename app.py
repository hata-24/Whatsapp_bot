from fastapi import FastAPI
import joblib

app=FastAPI()

intent_model=joblib.load("intent_model.pkl")
product_model=joblib.load("product_model.pkl")


@app.post("/predict")
def predict(data: dict):
    text=data.get("text", "")
    intent_probs=intent_model.predict_proba([text])[0]
    intent_classes=intent_model.classes_
    best_idx=intent_probs.argmax()
    intent_conf=intent_probs[best_idx]
    intent=intent_classes[best_idx]
    if intent_conf<0.20:
        intent="other"

    product_probs=product_model.predict_proba([text])[0]
    product_classes=product_model.classes_

    best_idx=product_probs.argmax()
    product_conf=product_probs[best_idx]
    product=product_classes[best_idx]

    if product_conf<0.20:
        product="Default"
    return{
        "intent":intent,
        "product":product,
    }