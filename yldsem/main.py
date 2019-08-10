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