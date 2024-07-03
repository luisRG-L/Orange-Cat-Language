from utilities import *
from config import *

print("Dev projects: \n")
folders = list_dirs(PROJECTS)
for folder in folders:
    print(folder + "/")

print("Scripts: \n")
files = list_files(PROJECTS)
for file in files:
    print(file)
