from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
def create_feature_transformer(X_train):
    """Create a preprocessor for transforming features."""
    cat_cols = X_train.select_dtypes(include=['object', 'category']).columns.tolist()
    num_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
    print(f"Categorical columns: {cat_cols}")
    print(f"Numeric columns: {num_cols}")
    preprocessor = ColumnTransformer(transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', StandardScaler(), num_cols)
    ])

    return preprocessor

def fit_transform_features(preprocessor, X_train):
    return preprocessor.fit_transform(X_train)

def transform_features(preprocessor, X_test):
    return preprocessor.transform(X_test)