from utilities import *
from basicCodes import *
from config import *
import os

project_name = input("Project name: ")
project_path = PROJECTS + project_name+"/libs"

createFolder(project_path)

lib_name = input("Library name: ")
lib_path = project_path + "/"+ lib_name

lib_uri = input("Library URL(or URI): ")

createFile(lib_path, OML_CODE_START + lib_uri + OML_CODE_END)

print("Installed library: "+lib_name+"("+lib_uri+")")