from catbuild import *
from utilities import *
from bridge import *
from lexer import *
from languajes import *
from exiter import *
from parse import *
from basicCodes import *

exe = Languaje(".exe")
jar = Languaje(".jar")
ocf = Languaje(".ocf")
zipf = Languaje(".zip")

exebridge = Bridge(1)

buildMain()

def connect():
    global ocf, zipf, jar, exe, exebridge
    exe.connect(ocf, exebridge)
    jar.connect(zipf, exebridge)
    jar.connect(ocf, exebridge)
    exe.connect(zipf, exebridge)
    exebridge.update()


def updateOCat():
    global ocf, zipf, jar, exe, exebridge
    exebridge.update()
    exe.connect(this, exebridge)
    jar.connect(this, exebridge)
    zipf.connect(this, exebridge)
    ocf.connect(this, exebridge)
    exebridge.update()

def exitLexedCode(code):
    for x in range(len(code)):
        if VERBOSE_TOKENS:
            print("Type keyword:", tokenName[lexer_code(code[x])])
            print("Number keyword:", lexer_code(code[x]))
    if VERBOSE_TOKENS:
        print("Exit number code:", get_exit(code))

def printStacks():
    thisSide.printStack()
    pythonSide.printStack()
    BridgeSide(connectBridge.thread).printStack()

def doProcess(code):
    if VERBOSE_ACTIONS:
        print("Doing process")
    parse_code(code)

def start_proccess(code):
    connect()
    updateOCat()
    exitLexedCode(code)
    updateOCat()
    printStacks()
    doProcess(code)
    updateOCat()
