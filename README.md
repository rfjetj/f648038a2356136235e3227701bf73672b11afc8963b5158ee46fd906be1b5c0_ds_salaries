# Project Overview
This project aims to predict the annual salary (in USD) of Data Scientists based on various job and company features such as experience level, employment type, company size, and location. The dataset contains salary records reported from 2020 through 2025 across different job titles, but the analysis is focused exclusively on Data Scientist roles to build a specialized and accurate predictive model.

# How to get the data
The dataset used in this project can be downloaded from [text](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs/data).
Place the CSV file in the data/Bronze/ folder with the filename salaries.csv before running the pipeline.

# Folder Structure
"""
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
│   └── test.ipynb
├── pyproject.toml
├── src
│   ├── data_preprocessing.py
│   ├── evaluation.py
│   ├── feature_engineering.py
│   ├── run_pipeline.py
│   ├── salaries.csv
│   └── training.py
└── uv.lock
"""