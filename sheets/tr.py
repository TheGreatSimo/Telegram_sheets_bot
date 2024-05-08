#!/usr/bin/env python3

import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("key.json", scopes=scopes)
client = gspread.authorize(creds)



women_id= "13e-d2n0hc5bsMe9NzUIXNqCsDN7ysYqR5Nxm8OV0yo4"
sheet = client.open_by_key(women_id)
worksheet = sheet.sheet1


existing_data = worksheet.col_values(1)  
next_row_index = len(existing_data) + 1

new_text = "zbi 3"
worksheet.update_cell(next_row_index, 1, new_text)

