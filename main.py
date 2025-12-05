# main.py
# -----------------------------------------------------------------------------
# STEP 2: API & Dockerfile (FastAPI application)
# Loads model.pkl and exposes a /predict endpoint.
# -----------------------------------------------------------------------------
import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI(
    title="Minimal MLOps POC API",
    description="Serves a simple scikit-learn Logistic Regression model."
)

# --- 1. Load Model ---
MODEL_PATH = "model.pkl"
try:
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)
    print(f"Successfully loaded model from {MODEL_PATH}")
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}. Ensure 'model_trainer.py' was run.")
    model = None # The API will still run, but prediction will fail

# --- 2. Request Schema ---
# Defines the input structure for the /predict endpoint
class PredictionRequest(BaseModel):
    # Based on the Iris dataset features used in model_trainer.py (sepal length and width)
    features: list[float]

# --- 3. API Endpoint ---
@app.post("/predict")
def predict_endpoint(request: PredictionRequest):
    """
    Accepts a list of two floats (features) and returns the model's prediction.
    """
    if model is None:
         return {"error": "Model not loaded. Check server logs."}
         
    # FastAPI/Pydantic ensures features is a list of floats
    # Convert the list to a numpy array for the model
    # Reshape for a single sample prediction: [[f1, f2]]
    data_in = np.array([request.features])
    
    # Make the prediction
    prediction = model.predict(data_in).tolist()[0]
    
    # Return the prediction and the input data
    return {
        "prediction": prediction,
        "input_data": request.features,
        "model_type": "LogisticRegression"
    }

@app.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "model_loaded": model is not None}