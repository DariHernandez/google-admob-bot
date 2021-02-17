#! python3
# Conect to google spreadsheets

import gspread, sys, time
from oauth2client.service_account import ServiceAccountCredentials

class Google_shets (): 
    """ Class to conect to google shets and upload data"""

    def __init__ (self, google_sheet_link): 
        """ Construtor of the class"""

        # Read credentials
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        # Conect to google sheet
        sheet = client.open_by_url(google_sheet_link)

        # Set the sheet 1 as worksheet
        self.worksheet = sheet.sheet1

    def write_data (self, data): 
        """ Write list of data in the worksheet"""
        
        # check if data exist
        if not data: 
            print ("THERE IS NO NEW INFORMATION TO WRITE IN THE FILE.")
        else:
            print ("Writing information on spreadsheet...")

            # Loop for each row of data
            for row in data: 

                # Set the position of the next row. Omit the header
                position = data.index(row) + 2

                # Write data in gss
                self.write_row (row, position)


    def write_row (self, data, row):
        """ Write a row in the spread sheet, at specific position"""

        # Insert row in specific position of the worksheet
        self.worksheet.insert_row (data, row)

    def get_data (self): 
        """ Read all records of the sheet"""

        records = self.worksheet.get_all_records()
        return records

