# This file uses os.walk to walk through the directories of the Downloads folder
# The result is print out of a directory, its subfolders, and the files within the subfolders

import os
from pathlib import Path

# Variable assignment to Path.home() -> Path.
homeFolder = Path.home()
subFolder = Path('Downloads')

p = homeFolder / subFolder

for folderName, subfolders, filenames in os.walk(p):
    print('The current folder is ' + folderName)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename) 
    
    print('')