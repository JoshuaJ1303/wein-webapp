from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your downloaded JSON credentials file
# Scope sets the correct API endpoint to access.
creds = service_account.Credentials.from_service_account_file(
    'secrets/service-account.json',
    #scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    scopes=['https://www.googleapis.com/auth/drive.readonly']
)

# Initialize the Drive API client
service = build('drive', 'v3', credentials=creds)

# Function to list files in Google Drive
def list_drive_files():
    results = service.files().list(pageSize=10, fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(f"{item['name']} ({item['id']})")

# Call the function to list files
list_drive_files()


# Path to your downloaded JSON credentials file
# Scope sets the correct API endpoint to access.
creds = service_account.Credentials.from_service_account_file(
    'secrets/service-account.json',
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    #scopes=['https://www.googleapis.com/auth/drive.readonly']
)
# Access content
sheets_service = build('sheets', 'v4', credentials=creds)
# Function to get columns from a Google Sheets file
def get_sheet_columns(spreadsheet_id, range_name='Weininventur!A1:Z1'):
    # Access the data in the specified range
    sheet = sheets_service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    header_row = result.get('values', [])

    # Display the columns (header row)
    if header_row:
        print("Columns:", header_row[0])  # Display the first row as column names
    else:
        print("No data found.")

# Replace with your actual spreadsheet ID
spreadsheet_id = '1C00vBQCW0nYRX0tRtVWf-Wyq-9GmmM8HmuC5jzO2QX0'
get_sheet_columns(spreadsheet_id)

