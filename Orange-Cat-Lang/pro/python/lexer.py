from config import *

VARTYPE = [
    "int",
    "decimal",
    "bool",
    "func",
    "char",
    "string",
    "class",
    "enum",
    "array",
    "_type"
]

ASSIGN = [
    "=",
    "*=",
    "&="
]

VALUE = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "'",
    "\"",
    "true", "false",
    "none", "null", "void"
]

OPERATOR = [
    "+", "-", "*", "/",
    "==", "**", "&&",
    ">", "*>", "&>",
    "<", "*<", "&<",
    ">=", "*>=", "&>=",
    "<=", "*<=", "&<="
]

COMMAND = [
    "if", "else", "elif",
    "forever", "for", "break",
    "return", "import", "export",
    "then", "print", "get",
    ""
]

COMMENT = [
    "//", "//<", "///<",
    "/#", "/*", "/+"
]

END = [";"]

KEYWORD = [
    "(", ")", "{", "}", "[", "]", ","
]

# Adding LOCAL keyword
MODIFIERS = ["local"]

SPECIAL = [":", ".", "<T>", "#"]

tokens = [
    VARTYPE,
    ASSIGN,
    VALUE,
    OPERATOR,
    COMMAND,
    COMMENT,
    END,
    KEYWORD,
    MODIFIERS,  # Adding LOCAL to the tokens list
    SPECIAL
]

VARTYPE_TOKEN = 0
ASSIGN_TOKEN = 1
VALUE_TOKEN = 2
OPERATOR_TOKEN = 3
COMMAND_TOKEN = 4
COMMENT_TOKEN = 5
END_TOKEN = 6
KEYWORD_TOKEN = 7
MODIFIER_TOKEN = 8  # Adding LOCAL_TOKEN
VARNAME_TOKEN = 10  # Adjusting VARNAME_TOKEN index
SPECIAL_TOKEN = 9

tokenName = [
    "Var type",
    "Assign",
    "Value",
    "Operator",
    "Command",
    "Comment",
    "End",
    "Keyword",
    "Modifier",  # Adding "Local"
    "Special",
    "Var name"
]

def lexer_code(line: str):
    lexer = Lexer(line)
    return lexer.lexer_code()

def getTokenIndex(line: str):
    lexer = Lexer(line)
    return lexer.getTokenIndex()

def specify_code(line: str):
    return tokenName[lexer_code(line)]

class Lexer:
    def __init__(self, line: str):
        self.line = line
    
    def lexer_code(self):
        if VERBOSE_ACTIONS:
            print("Lexing")
        if self.line is None:
            raise NotImplementedError("Lexer error: Not implemented line")
        if self.line == "":
            return None
        for i in range(len(tokens)):
            for n in range(len(tokens[i])):
                if self.line.startswith(tokens[i][n]):
                    return i
        if self.line[0].isalpha():
            return VARNAME_TOKEN
        return None
    
    def getTokenIndex(self):
        appendList = []
        if VERBOSE_ACTIONS:
            print("Lexing")
        if self.line is None:
            raise NotImplementedError("Lexer error: Not implemented line")
        if self.line == "":
            return None
        for i in range(len(tokens)):
            for n in range(len(tokens[i])):
                if self.line.startswith(tokens[i][n]):
                    appendList.append(i)
                    appendList.append(n)
        if self.line[0].isalpha():
            return VARNAME_TOKEN
        return None
    
def iterateTokens(code):
    tokenList = []
    for line in code.split('\n'):
        result = lexer_code(line.strip())
        if result is not None:
            tokenList.append(result)
    return tokenList

def getTokenArray(code):
    tokenArray = []
    for line in code.split('\n'):
        result = getTokenIndex(line.strip())
        if result is not None:
            tokenArray.append(result)
    return tokenArray
