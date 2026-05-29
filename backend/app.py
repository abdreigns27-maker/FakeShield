# ============================================================
# FakeShield — Flask Backend API
# CSC-233: AI Lab | Beaconhouse National University
#
# Endpoints:
#   GET  /          -> health check
#   POST /predict   -> { "text": "..." } returns { label, confidence }
#
# Run locally:  python app.py
# Deployed on Render with gunicorn (see Procfile / render.yaml)
# ============================================================

import pickle
import re
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))

app = Flask(__name__)
CORS(app)   # allow the frontend (GitHub Pages) to call this API

# ── Load model + vectorizer once at startup ──────────────────
BASE = os.path.dirname(os.path.abspath(__file__))
tfidf = pickle.load(open(os.path.join(BASE, "tfidf_vectorizer.pkl"), "rb"))
model = pickle.load(open(os.path.join(BASE, "best_model.pkl"),       "rb"))


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = " ".join(w for w in text.split() if w not in STOP_WORDS)
    return text


@app.route("/")
def home():
    return jsonify({"status": "FakeShield API is running", "endpoint": "/predict (POST)"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "No text provided"}), 400

    cleaned    = clean_text(text)
    vectorized = tfidf.transform([cleaned])
    prediction = int(model.predict(vectorized)[0])

    # Confidence: predict_proba if available, else decision_function
    try:
        proba      = model.predict_proba(vectorized)[0]
        confidence = float(max(proba) * 100)
    except AttributeError:
        decision   = model.decision_function(vectorized)[0]
        confidence = float(min(abs(decision) * 20, 99.9))

    label = "Fake" if prediction == 1 else "Real"

    return jsonify({
        "label": label,
        "prediction": prediction,
        "confidence": round(confidence, 1)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
