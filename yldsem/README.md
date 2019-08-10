## Problem statement
* Replace coordinates in a file with a desired value. Repeat the same for thousands of files present in a directory. The line is: 
```
SampleCenterLocation 21989.6 235.865;
```
New line
```
SampleCenterLocation xxx xxx;
```

## Project Directory
```console
.
|-- README.md
|-- data
|   |-- F17210001.F1_STI_WF01.001
|   |-- F17210001.F1_STI_WF09.001
|   `-- F17210001.F1_STI_WF14.001
|-- main.py
|-- main2.py
`-- new
    `-- F17210001.F1_STI_WF01.001

2 directories, 7 files
```

## Solution
* #### For a single file
```py
# file = filedialog.askopenfilename()    # prompt for choosing a file  
file = "data/F17210001.F1_STI_WF01.001"

# opening the file in line mode 
lines = open(file).read().splitlines() 
 
# going to 17th line and replacing it with desired values
lines[17] = 'SampleCenterLocation xxx xxx;' 
 
# writing op to file
open('new/F17210001.F1_STI_WF01.001','w').write('\n'.join(lines))
```
<b><u>Output:</u></b>
```txt
......
......
.....
SampleCenterLocation xxx xxx;
.....
.....
....
```
* #### For all the files [Entire code]
```py
# from tkinter import filedialog
import os 
 
# file = filedialog.askopenfilename()    # prompt for choosing a file  
# file = "data/F17210001.F1_STI_WF01.001"
for dirname, dirpath, files in os.walk("./data/"):
    for file in files:
        # print(file)
        # opening the file in line mode
        f = "./data/" + file 
        lines = open(f).read().splitlines() 
        # print(lines)
        # # going to 17th line and replacing it with desired values
        lines[17] = 'SampleCenterLocation xxx xxx;' 
         
        # # writing op to file
        open(f,'w').write('\n'.join(lines))
``` 

## Working
* Copy & Paste the original files from `orig` folder to `data` folder.
* Execute the python code in ST3 or terminal.
* Now, you will find the new line replacing the old line in the files in `data` folder.

### Cons
* Here, the code has been written for a particular line no. i.e. `17`, which is common in all the files in the directory.
