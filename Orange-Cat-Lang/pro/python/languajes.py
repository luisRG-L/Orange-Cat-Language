from bridge import *
from config import *

class Languaje:
    langName = ""

    def __init__(self, name : str):
        if VERBOSE_PROCESS:
            print("Added languaje support:", name)
        self.langName = name
        if name == "self" or name == "__init__":
            raise NameError("Can't be a self or __init__")
    
    def connect(self, lang, bridge):
        bridge.connect2(self, lang)
        if VERBOSE_PROCESS:
            print("Connected:", bridge, "from", lang)