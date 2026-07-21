import shutil
import os
import re
import pandas as pd
import os
import glob
import time
import openpyxl
from pathlib import Path
from openpyxl import load_workbook
import numpy as np
from datetime import datetime, date

# move files from downloads to walgreens input folder that were
# modified today and contain the keyword in the filename
source_directory = 'C:/Users' # Replace with the actual source directory
downloads_directory = "W:/  # Replace with the actual downloads directory
keyword = "340BComplete_RxDetails"  # Replace with the keyword you're looking for
today = date.today()
for filename in os.listdir(source_directory):
    filepath = os.path.join(source_directory, filename)
    if os.path.isfile(filepath):
                mtime = datetime.fromtimestamp(os.path.getmtime(filepath)).date()
                destination_filepath = os.path.join(downloads_directory, filename)
                if mtime == today and keyword in filename and filename.endswith('.xlsx'):
                    files = shutil.copy2(filepath, destination_filepath)  
                    # excel_file = pd.ExcelFile(excel_files)
                    # ret_df=[]
                    # spec_df = []
                    # for e in files:                        
                    workbook = openpyxl.load_workbook(files)
                    sheet = workbook.active                    
                    columns_to_numeric = ['']
                    columns_to_date = ['']
                    rows_to_remove = [0,1,2,3,4,5,6]
                    ret_df=[]
                    # spec_df = []
                    keyword = "Retail"   
                    matching_sheets = [sheet for sheet in workbook.sheetnames if keyword.lower() in sheet.lower()]   
                    for m in matching_sheets:           
                        new_filename_base =sheet["E4"].value.replace("ITEM","NAME")+sheet["E3"].value.replace("Time Period","_Time_Period")
                        # # Check if the cell has a value
                        if new_filename_base:
                            # Sanitize the filename
                            valid_filename = "".join(c if c.isalnum() or c in (' ', '.', '_') else '_' for c in str(new_filename_base)).strip()
                            new_filename = f"{valid_filename}.xlsx"
                            retdf = pd.read_excel(new_filename,sheet_name=sheet, header=None, 
                            names =(''))
                            ret_df.append(retdf) 
                            
 
