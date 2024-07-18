from . OrangeCat import *

fileName = input("Project name: ")
print ("\n")
code = getFileArray(PROJECTS + fileName + "\\main.ocat")
start_proccess(code)