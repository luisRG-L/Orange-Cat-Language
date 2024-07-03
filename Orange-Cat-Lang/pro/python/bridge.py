from catbuild import *
from config import *

class BridgeSide:
    def __init__(self, type):
        if VERBOSE_PROCESS:
            print("Type:", type, "for self", self)
    
    def printStack(self):
        if VERBOSE_PROCESS:
            print("Stack:", self)
    
class Bridge:
    thread = 0

    def __init__(self, thread : int):
        if VERBOSE_PROCESS:
            print("Compiling thread", thread)
        self.thread = thread

    def connect2(self, com1, com2):
        if VERBOSE_PROCESS:
            print("Connected thread:", com1, com2)

    def update(self):
        if VERBOSE_ACTIONS:
            print("Updated")