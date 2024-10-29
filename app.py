import numpy as np

from flask import Flask, render_template
from google.oauth2 import service_account
from googleapiclient.discovery import build

import pandas as pd

from src.cleaning import clean_data
from src.plot import create_barchart, create_piechart

# Initialize the Flask application
app = Flask(__name__)

# Load credentials and set up Google Sheets API service
creds = service_account.Credentials.from_service_account_file(
    'secrets/service-account.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
)
sheets_service = build('sheets', 'v4', credentials=creds)

# Function to get data from Google Sheets
def get_sheet_contents(spreadsheet_id, range_name='Weininventur!A1:Z10'):
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()
    return result.get('values', [])  # Return the cell values

# Define the route for the homepage
@app.route('/')
def index():
    # Replace with your actual spreadsheet ID
    spreadsheet_id = '1C00vBQCW0nYRX0tRtVWf-Wyq-9GmmM8HmuC5jzO2QX0'  # Put your spreadsheet ID here
    list_data = get_sheet_contents(spreadsheet_id, 
                              range_name='Weininventur') # Adjust range as needed
    
    df_raw = pd.DataFrame(list_data[1:], columns=list_data[0])

    df_cleaned = clean_data(df_raw, "Name")
    
    bar_fig_json = create_barchart(df=df_cleaned, ID="Jahrgang")
    pie_fig_json = create_piechart(df=df_cleaned, ID="Land")
    #print(bar_fig_json)

    # Normalize row lengths: Convert DataFrame back to list of lists
    list_cleaned = df_cleaned.values.tolist()  # Convert DataFrame to list of lists
    list_cleaned.insert(0, df_cleaned.columns.tolist())  # Add headers back to the list

    print("Data Shape:", len(list_cleaned), "rows and", len(list_cleaned[0]), "columns")  # Check number of rows and columns

    # Debugging: Print the data structure to the console
    if list_cleaned:
        print("Columns:", list_cleaned[0])  # Print the first row (headers)
        print("Columns:", list_cleaned[-1])
        #print("shape:", pd.DataFrame(data[1:], columns=data[0]).dropna(subset="Name").iloc[-1])
    else:
        print("No data found.")
    return render_template('index.html', data=list_cleaned, bar_fig=bar_fig_json, pie_fig=pie_fig_json)

if __name__ == '__main__':
    app.run(debug=True)
