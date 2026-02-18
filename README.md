🌟 Secure Pay AI — Fraud Detection System

Secure Pay AI is an AI-based fraud detection application designed to analyze digital transactions and identify suspicious activity in real time.
It combines machine learning models with a simple web interface to help detect and prevent fraudulent transactions.

The system uses synthetic data generation (GAN) to improve training data quality and a Random Forest classifier to predict whether a transaction is fraudulent or safe.

⚙️ Key Features

AI-based fraud detection using trained ML models

Real-time prediction via REST API

Synthetic data generation for model training

Web dashboard for transaction monitoring

Responsive frontend interface

🧩 Tech Stack

Frontend: React, Vite, Tailwind CSS
Backend: Python, Flask
AI/ML: GAN, Random Forest (scikit-learn)
Database: Firebase

🚀 How It Works

Transaction details are entered in the web interface.

Data is sent to the Flask API.

The trained Random Forest model analyzes the features.

The system returns Fraud or Not Fraud prediction.

Result is displayed on the dashboard.

📡 API

POST /predict

Request:

{
  "features": [values]
}


Response:

{
  "prediction": "Fraud or Not Fraud"
}
