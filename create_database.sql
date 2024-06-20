-- Create the database
CREATE DATABASE IF NOT EXISTS employee_attrition_analysis;

-- Use the newly created database
USE employee_attrition_analysis;

-- Create the employees table
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    business_travel VARCHAR(255),
    daily_rate INT,
    department VARCHAR(255),
    distance_from_home INT,
    education INT,
    education_field VARCHAR(255),
    employee_count INT,
    employee_number INT,
    environment_satisfaction INT,
    gender VARCHAR(255),
    hourly_rate INT,
    job_involvement INT,
    job_level INT,
    job_role VARCHAR(255),
    job_satisfaction INT,
    marital_status VARCHAR(255),
    monthly_income INT,
    monthly_rate INT,
    num_companies_worked INT,
    over18 VARCHAR(255),
    over_time VARCHAR(255),
    percent_salary_hike INT,
    performance_rating INT,
    relationship_satisfaction INT,
    standard_hours INT,
    stock_option_level INT,
    total_working_years INT,
    training_times_last_year INT,
    work_life_balance INT,
    years_at_company INT,
    years_in_current_role INT,
    years_since_last_promotion INT,
    years_with_curr_manager INT,
    attrition BOOLEAN
);
