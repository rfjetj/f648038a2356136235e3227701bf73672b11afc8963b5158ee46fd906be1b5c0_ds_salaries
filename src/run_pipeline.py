from data_preprocessing import load_data, filter_data_scientist, preprocess_and_split
from feature_engineering import (
    create_feature_transformer,
    fit_transform_features,
    transform_features,
)
from training import train_model
from evaluation import evaluate_model
import os


def main():
    print("Current working directory:", os.getcwd())
    data = load_data("src/salaries.csv")

    data = filter_data_scientist(data)
    X_train, X_test, y_train, y_test = preprocess_and_split(data)

    preprocessor = create_feature_transformer(X_train)
    X_train = fit_transform_features(preprocessor, X_train)
    X_test = transform_features(preprocessor, X_test)

    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()
