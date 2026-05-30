🛡️ FakeShield — AI-Powered Fake News Detection System
Beaconhouse National University | CSC-233: AI Lab | Spring 2026
SDG 16: Peace, Justice and Strong Institutions
---
🌐 Live Links
Frontend (GitHub Pages): https://abdreigns27-maker.github.io/FakeShield
Backend API (Railway): https://fakeshield-api-production.up.railway.app
---
👥 Team (Section A)
Name	Roll No.	Model
Abdullah Irfan (Group Lead)	F2024-0146	Logistic Regression
Tayyeba Sharafat	F2024-1188	Naive Bayes
Danish Tariq	F2024-0017	Random Forest
Syed Mohsin Salman	F2024-0293	SVM (LinearSVC) ★ Best
---
📌 Overview
FakeShield is a full-stack machine learning web application that classifies news articles as Real or Fake. Users paste any news text into the website and instantly get a prediction with a confidence score. Four classification models are trained on the same data; the best-performing one (SVM at 99.71%) powers the deployed app.
---
📁 Repository Structure
```
FakeShield/
├── dataset/
│   ├── preprocess.ipynb            ← run FIRST (shared by everyone)
│   └── tfidf_vectorizer.pkl        ← saved vectorizer
│
├── models/
│   ├── Abdullah_LR.ipynb           ← Logistic Regression
│   ├── Tayyeba_NB.ipynb            ← Naive Bayes
│   ├── Danish_RF.ipynb             ← Random Forest
│   ├── Mohsin_SVM.ipynb            ← SVM
│   ├── Compare_Models.ipynb        ← picks best_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── naive_bayes_model.pkl
│   ├── svm_model.pkl
│   └── best_model.pkl
│
├── backend/                        ← Flask API (deployed on Railway)
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── tfidf_vectorizer.pkl
│   └── best_model.pkl
│
├── index.html                      ← Frontend (GitHub Pages)
├── render.yaml
└── README.md
```
---
⚠️ Large Files (Google Drive)
Some files exceeded GitHub's 25MB limit and are available via Google Drive:
processed_data.csv → https://drive.google.com/file/d/1R__7bZl9KispBZ7M77ahWrZ1YJ9FPic_/view?usp=sharing
random_forest_model.pkl → https://drive.google.com/file/d/1taOXe0_-rIP3-EnpL26KKih_cRXNbutZ/view?usp=sharing
---
📊 Dataset
Name: Fake and Real News Dataset
Source: Kaggle
Size: ~44,898 articles (23,481 Fake + 21,417 Real)
Features used: title + text combined, TF-IDF vectorized (50k features, unigrams + bigrams)
---
🤖 Models & Results
Model	Member	Accuracy
Logistic Regression	Abdullah Irfan	99.19%
Naive Bayes	Tayyeba Sharafat	96.45%
Random Forest	Danish Tariq	99.67%
SVM (LinearSVC) ★	Syed Mohsin Salman	99.71%
---
🛠️ Tech Stack
Python · scikit-learn · NLTK · TF-IDF · Flask · Flask-CORS · Gunicorn · HTML/CSS/JS · Railway · GitHub Pages · Google Colab
