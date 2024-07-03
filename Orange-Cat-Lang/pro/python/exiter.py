from config import *
from lexer import *

def get_exit(code):
    if VERBOSE_ACTIONS:
        print("Getting output file")
    number = ""
    for i in range(len(code)):
        number += str(lexer_code(code[i]))
    return number