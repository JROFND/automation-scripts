import pandas as pd 

n = 500000  # number of rows per chunk
df = pd.read_csv("erx.csv")
# sf_df = df.loc[df['LOC NAME'] == 'SANFORD USD MEDICAL CENTER']

for i in range(0, df.shape[0], n):
    df[i:i+n].to_excel(f"erx_file{i:03}.xlsx", index=None, header=True)

