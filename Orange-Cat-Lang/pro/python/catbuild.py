from languajes import *
from bridge import *
from config import *

this = Languaje("OrangeCat")
python = Languaje("Python")
mainBridge = Bridge(0)

thisSide = BridgeSide(this)
pythonSide = BridgeSide(this)

connectBridge = Bridge(-1)

def buildMain():
    update()
    this.langName = "ocat"
    mainBridge.connect2(this, python)
    connectBridge.connect2(thisSide, pythonSide)

def update():
    if VERBOSE_ACTIONS:
        print("Updated")