import pandas as pd

excel_file = 'test.xlsx'
"""df = pd.read_excel(excel_file)
print(df.head())"""

cols = [0,1,2]
df = pd.read_excel(excel_file, usecols=cols)
print(df.head())