# Employee Attrition Analysis

This project analyzes and predicts employee attrition using HR data. The project includes data loading, preprocessing, analysis, model building, and a Flask web interface to visualize the results.

## Directory Structure

employee-attrition-analysis/
│
├── data/
│ └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── database/
│ ├── create_database.sql
│ ├── insert_data.sql
│
├── scripts/
│ ├── load_data.py
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ └── templates/
│ └── index.html
│
├── requirements.txt
└── README.md
|__ run.py

## Setup and Installation

1. Create the database and tables:
   - Run the SQL scripts in the `database/` directory.

2. Load data into the database:
   - Run the `load_data.py` script in the `scripts/` directory.

3. Install the required Python packages:
   - `pip install -r requirements.txt`

4. Run the Flask web application:
   - `python run.py`

5. Open your browser and navigate to `http://127.0.0.1:5000/`
