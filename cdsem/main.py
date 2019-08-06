import pandas as pd
from re import search

"""
How to find the file as "tab separated values"?
- find out in  "Save as" whether "Tab-separated" or "Comma-separated" 
"""
df = pd.read_csv('data\\cdsem.msr', sep= '\t')

cdsemlist = df[df.columns[0]].tolist()
# print(cdsemlist)

substring = "      ~image_info    !Cursor_inf"
cdsemval_list = []

for item in cdsemlist:
    if search(substring, item):
        # print(item[88:-4])
        cdsemval_list.append(item[88:-4])

print(cdsemval_list)
