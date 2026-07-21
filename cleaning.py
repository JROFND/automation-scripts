import os
import glob
import pandas as pd
from datetime import date
import warnings
import numpy as np
import re
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

save_folder = r'W:\SHARE2 Pharmacy Department Share\340B\Jeff R\Specialty Pharmacy Tool'
os.chdir(save_folder)


# Find all Excel files matching the pattern
cardinal_files = glob.glob(os.path.join(save_folder, 'SANFORD_*.xlsx'))
apexus_files = glob.glob(os.path.join(save_folder, 'APEXUS*.xlsx'))


df_list = []


# Define a cleaning function
def clean_ndc(value):
    if pd.isnull(value):
        return value
    # Removes non-alphanumeric characters
    return re.sub(r'\W+', '', str(value).strip())


def standardize_ndc(ndc):
    if pd.isnull(ndc):
        return ndc
    ndc = re.sub(r'\D', '', str(ndc))  # Remove non-digits
    return ndc.zfill(11)  # Pad to 11 digits

# Process Cardinal files


for file_path in cardinal_files:
    df = pd.read_excel(
        file_path,  engine='openpyxl',
        usecols=['NDC 11', 'NDC Number',
                 'Ship To Customer Number',
                 # 'Customer Name',
                 # 'Material Number (Numeric)',
                 'Current Catalog Price'],
        dtype={
            'NDC 11': object,
            'Ship To Customer Number': object,
            'Material Number (Numeric)': object
        })    .rename(columns={
            'NDC 11': 'NDC', 'NDC Number': 'NDC_Number',
            # 'Material Number (Numeric)': 'CIN',
            'Ship To Customer Number': 'Account',
            'Current Catalog Price': 'Current_Price'}
    )
    df_list.append(df)

cardinal_df = pd.concat(df_list, ignore_index=True)

cardinal_df_copy = cardinal_df.copy()

cardinal_df_copy = cardinal_df_copy[cardinal_df_copy['Account'].isin(
    ['2150124178', '2150125178', '2150125169', '2150125128'])]

cardinal_df_copy['NDC_Number'] = cardinal_df_copy['NDC_Number'].apply(
    standardize_ndc)

    
# Process Apexus file
apexus_df = pd.read_excel(apexus_files[0], engine='openpyxl', sheet_name='Non-GPO_WAC_PVP_catalog',header=3, 
                          usecols=['NDC', 'Item #', '340B Selling Price', '340B Selling Price Eff Date']).rename(
    columns={'340B Selling Price': 'Ceiling_Price', '340B Selling Price Eff Date': 'Ceiling_Date'})

apexus_df_copy = apexus_df.copy()


apexus_df_copy = apexus_df_copy[
    apexus_df_copy['NDC'].notna() &
    ~apexus_df_copy['Item #'].str.contains('DPPV', case=False, na=False)
].reset_index()

