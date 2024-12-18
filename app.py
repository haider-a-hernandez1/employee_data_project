import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV data into a DataFrame
df = pd.read_csv('employee_data.csv')

# Debugging: print the first few rows of the DataFrame to confirm it is loaded
print(df.head())  # This will print the first few rows of the data

@app.route('/')
def index():
    # You can add the queries and visualizations here
    return render_template('index.html', data=df.head())  # Pass the data to the template

if __name__ == '__main__':
    app.run(debug=True)


