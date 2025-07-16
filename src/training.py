import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train):
    """Train an XGBoost model with hyperparameter tuning."""
    model = XGBRegressor(random_state=42, n_jobs=-1)

    # Define hyperparameters to tune
    param_grid = {
        'n_estimators': [100, 300, 500],
        'max_depth': [3, 5, 7, 10],
        'learning_rate': [0.01, 0.05, 0.1],
        'min_child_weight': [1, 3, 5],
        'subsample': [0.7, 0.8, 1.0],
        'colsample_bytree': [0.6, 0.8, 1.0]
    }

    # Perform grid search with cross-validation
    grid_search = GridSearchCV(model, param_grid, scoring='neg_mean_squared_error', cv=5, verbose=1, n_jobs=-1)
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    print("Best parameters:", grid_search.best_params_)
    print("Best score (negative MSE):", grid_search.best_score_)

    # Save the best model
    joblib.dump(best_model, './models/model.pkl')
    print("Best model saved to ./models/model.pkl")

    return best_model