import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Replace with your actual MySQL credentials
user = 'root'
password = '445204'
host = '127.0.0.2'
database = 'employee_attrition_analysis'

# Define the database connection string
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

# Load data from CSV file
file_path = '../data/WA_Fn-UseC_-HR-Employee-Attrition.csv'
data = pd.read_csv(file_path)

# Function to convert NumPy data types to native Python types
def convert_to_native_type(x):
    if isinstance(x, (np.integer, np.int64, np.int32)):
        return int(x)
    elif isinstance(x, (np.floating, np.float64, np.float32)):
        return float(x)
    else:
        return x

# Apply conversion to each element in the DataFrame
data = data.applymap(convert_to_native_type)

# Ensure all integer columns are Python native integers
for column in data.select_dtypes(include=['int64', 'int32']).columns:
    data[column] = data[column].apply(int)

# Save processed data to SQL database
data.to_sql('employees', con=engine, if_exists='replace', index=False)
