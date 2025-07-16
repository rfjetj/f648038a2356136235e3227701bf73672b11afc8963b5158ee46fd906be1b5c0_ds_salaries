import joblib
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate_model(model, X_test, y_test):
    """Evaluate the model on the test set."""
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    print("Model evaluation:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Root Mean Squared Error: {rmse:.2f}")
    print(f"R^2 Score: {r2:.2f}")
    with open('./models/evaluation.txt', 'w') as f:
        f.write(f"Mean Squared Error: {mse:.2f}\n")
        f.write(f"Root Mean Squared Error: {rmse:.2f}\n")
        f.write(f"R^2 Score: {r2:.2f}\n")
    return mse, rmse, r2