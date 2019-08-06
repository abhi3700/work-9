import pandas as pd
from re import search

"""
How to find the file as "tab separated values"?
- find out in  "Save as" whether "Tab-separated" or "Comma-separated" 
"""
df = pd.read_csv('data\\F17210001.F1_STI_WF01.001', sep= '\t')

yldsemlist = df[df.columns[0]].tolist()
# print(cdsemlist)

substring = "SampleCenterLocation"
yldsemval_list = []

for item in yldsemlist:
    if search(substring, item):
        # print(item[88:-4])
        # cdsemval_list.append(item)
        print(item)

# print(cdsemval_list)
