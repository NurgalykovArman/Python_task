def outputfiles(path):
    """creating a generator containing all files"""
    filesss =os.walk(path)
    return filesss

def separ(filesss):
    """separation by columns"""
    folder = []
    filename = []
    extension = []
    for d in filesss:
        for j in d[2]:
            folder.append(d[0].split('\\')[-1])
        for j in d[2]:
            if(j.rsplit('.', 1)[0] == ''):
                filename.append("NULL")
            else:
                filename.append(j.rsplit('.', 1)[0])
        for j in d[2]:
            if('.' in j):
                extension.append(j.split('.')[-1])
            else:
                extension.append("NULL")
    return folder, filename, extension

import os 
import pandas as pd
import numpy as np

try:

    folder = []
    filename = []
    extension = []

    path = r'C:\Users\admin\OneDrive\Рабочий стол\testtask'

    filesss = outputfiles(path)

    temp = separ(filesss)

    folder = temp[0]
    filename = temp[1]
    extension = temp[2]
        
    df = pd.DataFrame({'Folder_name': folder,
                   'File_name': filename,
                   'FIle_extension': extension}, index=np.arange(1, len(filename)+1))

    df.to_excel('./result.xlsx')

except PermissionError:
    print("Close the excel file before running the code")