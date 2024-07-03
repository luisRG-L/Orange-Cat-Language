from OrangeCat import *

fileName = input("File route: ")
print ("\n")
code = getFileArray(PROJECTS + fileName + ".ocat")
start_proccess(code)