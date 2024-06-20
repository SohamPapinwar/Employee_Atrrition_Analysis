from flask import render_template, request, redirect, url_for
from app import app
from sqlalchemy import create_engine
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# Database configuration
user = 'root'
password = '*****'
host = '*******'
database = 'employee_attrition_analysis'
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

# Load data from the database
def load_data():
    query = 'SELECT * FROM employees'
    df = pd.read_sql(query, engine)
    return df

# Data preprocessing
def preprocess_data(df):
    le = LabelEncoder()
    df['Attrition'] = le.fit_transform(df['Attrition'])
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df.drop('Attrition', axis=1))
    df_scaled = pd.DataFrame(scaled_features, columns=df.columns[:-1])
    df_scaled['Attrition'] = df['Attrition']
    return df_scaled

# Build models
def build_models(X_train, y_train):
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)
    nn_model = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, random_state=42)
    nn_model.fit(X_train, y_train)
    return dt_model, nn_model

## Visualization
def plot_eda(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Attrition', data=df)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def plot_correlation(df):
    plt.figure(figsize=(20, 10))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def plot_attrition_by_department(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Department', hue='Attrition', data=df)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def plot_attrition_by_jobrole(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(x='JobRole', hue='Attrition', data=df)
    plt.xticks(rotation=45)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def plot_income_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df, x='MonthlyIncome', hue='Attrition', kde=True, element="step")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

def plot_age_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df, x='Age', hue='Attrition', kde=True, element="step")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

@app.route('/')
def index():
    df = load_data()
    df_processed = preprocess_data(df)
    X = df_processed.drop('Attrition', axis=1)
    y = df_processed['Attrition']
    dt_model, nn_model = build_models(X, y)
    
    eda_plot = plot_eda(df)
    correlation_plot = plot_correlation(df)
    department_plot = plot_attrition_by_department(df)
    jobrole_plot = plot_attrition_by_jobrole(df)
    income_plot = plot_income_distribution(df)
    age_plot = plot_age_distribution(df)
    
    return render_template('index.html', 
                           eda_plot=eda_plot, 
                           correlation_plot=correlation_plot, 
                           department_plot=department_plot, 
                           jobrole_plot=jobrole_plot, 
                           income_plot=income_plot, 
                           age_plot=age_plot)

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        query = f'SELECT * FROM employees WHERE EmployeeNumber = {employee_id}'
        df = pd.read_sql(query, engine)
        if df.empty:
            return render_template('employee.html', error="Employee not found")
        return render_template('employee.html', employee=df.iloc[0].to_dict())
    return render_template('employee.html')
