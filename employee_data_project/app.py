import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV data into a DataFrame
df = pd.read_csv('employee_data.csv')

@app.route('/')
def index():
    # You can add the queries and visualizations here
    return render_template('index.html', data=df.head())  # Just a sample, replace with actual query results

if __name__ == '__main__':
    app.run(debug=True)