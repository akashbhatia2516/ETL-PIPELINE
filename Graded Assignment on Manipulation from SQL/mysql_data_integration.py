import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Load Excel file
file_path = "RAW_Sheets_TECHSPHERE.xlsx"
xls = pd.ExcelFile(file_path)

# Read each sheet
employee_details = xls.parse('Employee_Details')
project_assignments = xls.parse('Project_Assignments')
attendance_records = xls.parse('Attendance_Records')
training_programs = xls.parse('Training_Programs')

# Database connection settings
DB_HOST = "your_host"
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_NAME = "TechSphere_DB"

# Create a connection
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# Convert DataFrames to SQL tables
employee_details.to_sql("Employee_Details", con=engine, if_exists="replace", index=False)
project_assignments.to_sql("Project_Assignments", con=engine, if_exists="replace", index=False)
attendance_records.to_sql("Attendance_Records", con=engine, if_exists="replace", index=False)
training_programs.to_sql("Training_Programs", con=engine, if_exists="replace", index=False)

print("Data successfully uploaded to MySQL!")
