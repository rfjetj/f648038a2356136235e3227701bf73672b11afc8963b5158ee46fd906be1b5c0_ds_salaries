import pandas as pd
from sklearn.model_selection import train_test_split
def load_data(file_path) -> pd.DataFrame:
    """Load the dataset from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def filter_data_scientist(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to keep only Data Scientist job title."""
    return df[df['job_title'] == 'Data Scientist'].copy().reset_index(drop=True)

def preprocess_and_split (df: pd.DataFrame) -> tuple:
    """Preprocess the DataFrame and split into features and target."""
    df = df.dropna()
    df = df.drop(columns=['salary', 'salary_currency'])

    # Split features and target
    X = df.drop(columns=['salary_in_usd'])
    y = df['salary_in_usd']

    # Split train/test
    return train_test_split(X, y, test_size=0.2, random_state=42)