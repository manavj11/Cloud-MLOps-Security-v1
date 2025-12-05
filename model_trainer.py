# model_trainer.py
# -----------------------------------------------------------------------------
# STEP 1: Model Creation
# Trains a simple Logistic Regression model on the Iris dataset and saves it.
# -----------------------------------------------------------------------------
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_and_save_model():
    """Trains the model and saves it as model.pkl."""
    print("Loading Iris dataset...")
    # Load data and select a feature subset for simplicity
    X, y = load_iris(return_X_y=True)
    # Use only the first two features for simplicity and speed
    X = X[:, :2] 
    
    # Split for a more realistic scenario (though the model won't be evaluated here)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training Logistic Regression model...")
    # Initialize and train the model
    model = LogisticRegression(solver='liblinear', random_state=0)
    model.fit(X_train, y_train)

    # Save the trained model artifact
    model_filename = 'model.pkl'
    with open(model_filename, 'wb') as file:
        pickle.dump(model, file)
        
    print(f"Model successfully trained and saved as {model_filename}")

if __name__ == "__main__":
    train_and_save_model()