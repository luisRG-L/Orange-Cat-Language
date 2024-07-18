from .utilities import *
from .config import *

project_name = input("Project name: ")
project_path = PROJECTS + project_name

# Todo

todo_name = 'todo.md'
todo_path = os.path.join(project_path, todo_name)

createFile(todo_path, "# Todo list\n")

# Readme

readme_name = 'readme.md'
readme_path = os.path.join(project_path, readme_name)

createFile(readme_path, "# Readme\n")