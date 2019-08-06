* extract desired lines
```py
for item in cdsemlist:
    if search(substring, item):
        print(item)
```

```console
      ~image_info    !Cursor_inf             -1,-1,990,4130,-1,-1,-1,-1,-1,-1,1,1,-1,1," 472.1 nm",""
      ~image_info    !Cursor_inf             -1,-1,990,4130,-1,-1,-1,-1,-1,-1,1,1,-1,1," 479.5 nm",""
      ~image_info    !Cursor_inf             -1,-1,990,4130,-1,-1,-1,-1,-1,-1,1,1,-1,1," 467.7 nm",""
      ~image_info    !Cursor_inf             -1,-1,990,4130,-1,-1,-1,-1,-1,-1,1,1,-1,1," 464.9 nm",""
      ~image_info    !Cursor_inf             -1,-1,990,4130,-1,-1,-1,-1,-1,-1,1,1,-1,1," 473.6 nm",""
```
* final code
```py
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

```
```console
[' 472.1 nm', ' 479.5 nm', ' 467.7 nm', ' 464.9 nm', ' 473.6 nm']
```