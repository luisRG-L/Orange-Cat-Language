from .utilities import *
from .config import *
from .basicCodes import *
import subprocess

filename = input("file name: ") + ".ocat"
path = PROJECTS + filename

createFile(path, BASIC_CODE)

try:
    subprocess.run(['notepad.exe', path], check=True)
    print(f"Opened file: {path}")
except subprocess.CalledProcessError as e:
    print(f"Error opening ocat editor: {e}")
except FileNotFoundError:
    print("You don't have any ocat editor. Install an editor.")
except Exception as e:
    print(f"Unchecked error: {e}")
