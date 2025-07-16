# Project Overview
This project aims to predict the annual salary (in USD) of Data Scientists based on various job and company features such as experience level, employment type, company size, and location. The dataset contains salary records reported from 2020 through 2025 across different job titles, but the analysis is focused exclusively on Data Scientist roles to build a specialized and accurate predictive model.

# How to get the data
The dataset used in this project can be downloaded from [Kaggle](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs/data).
Place the CSV file in the data/Bronze/ folder with the filename salaries.csv before running the pipeline.

# Folder Structure
```
├── .python-version
├── README.md
├── data
│   ├── Bronze
│   │   └── salaries.csv
│   └── Silver
├── models
├── evaluation.txt
│   └── model.pkl
├── notebooks
│   ├── EDA.ipynb
│   ├── preprocessing_modelling copy.ipynb
│   ├── preprocessing_modelling.ipynb
├── pyproject.toml
├── src
│   ├── data_preprocessing.py
│   ├── evaluation.py
│   ├── feature_engineering.py
│   ├── run_pipeline.py
│   ├── salaries.csv
│   └── training.py
└── uv.lock
```

# Setup Instructions
This project uses [uv](https://github.com/astral-sh/uv) for managing the Python environment and dependencies.

1. Install Python
Download and install Python 3.12+ from the [official website](https://www.python.org/downloads/).
2. Install uv
Install `uv` using pip
```bash
pip install uv
```
3. Create a virtual environment
```uv venv .venv --python python3.12```
4. Activate the virtual environment (Windows)
```.\.venv\Scripts\activate```
5. Install dependencies
```
uv add scikit-learn
uv add pandas numpy
uv add ipykernel
uv add matplotlib seaborn
uv add xgboost catboost
```

# Pre-commit Hook Config
I use **pre-commit** to keep my code clean and consistent before every commit.
### Hooks used
- **ruff** (v0.12.3)  
  Checks Python code for errors and fixes formatting automatically (`--fix`).
- **ruff-format**  
  Ensures consistent code style.
- **uv-lock** (v0.7.20)  
  Keeps the `uv.lock` file updated when dependencies change.


# Reflection
This project has been tough for me coming from a non-dev background. All of the topics are very unfamiliar and the rate of discussion is too fast. I find myself relying on LLMs like chatGPT to help generate the code, understand concepts and determine the next steps to take. I also found my experienced classmates very helpful in this assignment 💪. 

Despite the challenges, this experience gave me a glimpse of how ML and Data Science projects are done in production. This greatly expanded my perspective in handling real-world projects. With the more structured approach, it is easier to understand and visualize the processes. I look forward to applying these skills and deepening my knowledge as I continue my journey