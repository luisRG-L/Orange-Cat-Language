from .lexer import *
from .errors import *
from .config import *

def parse_code(code):
    tokens = iterateTokens(code)
    parser = Parser(tokens, code)
    parser.doFunctionally()
    if VERBOSE_MEMORY:
        parser.iterate()

class Parser:
    def __init__(self, op_toks, code):
        self.op_toks = op_toks
        self.code = code
        self.token_pos = 0
        self.variables = {}
        self.anonymus = {}
        self.local_variables = {}
        self.methods = {}
        self.classes = {}
        self.isRunning = True
        if VERBOSE_ACTIONS:
            print("Parsing operation tokens")

    def error(self, text):
        printSyntaxError(text)
        self.isRunning = False

    def verify(self, tokenType, token2=None):
        if self.token_pos < len(self.op_toks):
            if self.op_toks[self.token_pos] == tokenType or (token2 is not None and self.op_toks[self.token_pos] == token2):
                self.token_pos += 1
            else:
                self.error(f"Unexpected token '{self.code[self.token_pos]}', {self.token_pos}")

    def doFunctionally(self):
        while self.token_pos < len(self.op_toks) and self.isRunning:
            if self.op_toks[self.token_pos] == VARTYPE_TOKEN:
                self.parseVariableDeclaration()
            elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
                if self.code[self.token_pos] in self.methods:
                    self.parseFunctionCall()
                else:
                    self.parseVariableAssignment()
            elif self.op_toks[self.token_pos] == COMMAND_TOKEN:
                if self.code[self.token_pos] == "print":
                    self.parsePrintStatement()
                elif self.code[self.token_pos] == "get":
                    self.parseGetStatement()
            elif self.op_toks[self.token_pos] == COMMENT_TOKEN:
                print("Comment")
            elif self.op_toks[self.token_pos] == MODIFIER_TOKEN:
                if self.code[self.token_pos] == "local":
                    self.parseLocalVariableDeclaration()
            elif self.op_toks[self.token_pos] == SPECIAL_TOKEN:
                self.parseAnonymusTypeDeclaration()
            else:
                self.error(f"Unexpected token {self.token_pos}")
            if self.isRunning and self.token_pos < len(self.op_toks) and self.op_toks[self.token_pos] != END_TOKEN:
                self.error(f"Expected end of statement {self.token_pos}")
            else:
                self.token_pos += 1

    def parseAnonymusTypeDeclaration(self):
        self.token_pos += 1
        self.verify(VARNAME_TOKEN)
        var_name = self.code[self.token_pos - 1]
        self.verify(ASSIGN_TOKEN)
        self.verify(VARTYPE_TOKEN)
        var_type = self.code[self.token_pos - 1]
        if var_type not in VARTYPE:
            self.error(f"Unknown variable type {var_type}")
            return
        self.verify(SPECIAL_TOKEN)
        self.anonymus[var_name] = var_type

    def parseVariableDeclaration(self):
        var_type = self.code[self.token_pos]
        self.token_pos += 1
        self.verify(VARNAME_TOKEN)
        var_name = self.code[self.token_pos - 1]
        
        # Check if the variable name is already in use
        if var_name in self.variables:
            self.error(f"Variable {var_name} is already declared")
            return
        
        if var_type == "int" or var_type == "decimal":
            self.verify(ASSIGN_TOKEN)
            var_value = self.parseExpression()  # Parse expression for variable value
            self.variables[var_name] = var_value
        elif var_type == "string":
            self.verify(ASSIGN_TOKEN)
            self.verify(VALUE_TOKEN)  # Check if next token is a value
            var_value = self.code[self.token_pos - 1]
            self.variables[var_name] = var_value
        elif var_type == "bool":
            self.verify(ASSIGN_TOKEN)
            self.verify(VALUE_TOKEN)  # Check if next token is a value
            var_value = True if self.code[self.token_pos - 1] == "true" else False
            self.variables[var_name] = var_value
        elif var_type == "func":
            self.verify(KEYWORD_TOKEN)  # Verifying '('
            params = []
            while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != ")":
                param_type = self.code[self.token_pos]
                self.verify(VARTYPE_TOKEN)
                param_name = self.code[self.token_pos]
                self.verify(VARNAME_TOKEN)
                params.append((param_type, param_name))
                if self.op_toks[self.token_pos] == KEYWORD_TOKEN and self.code[self.token_pos] == ",":
                    self.token_pos += 1  # Skip ','
                elif self.op_toks[self.token_pos] == KEYWORD_TOKEN and self.code[self.token_pos] == ")":
                    break
                else:
                    self.error("Expected ',' or ')' in function declaration")
            self.verify(KEYWORD_TOKEN)  # Verifying ')'
            self.verify(KEYWORD_TOKEN)  # Verifying '{'
            func_body = []
            while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != "}":
                func_body.append(self.code[self.token_pos])
                self.token_pos += 1
            self.verify(KEYWORD_TOKEN)  # Verifying '}'
            self.methods[var_name] = {'params': params, 'body': func_body}
        elif var_type == "class":
            self.verify(KEYWORD_TOKEN) # Verifying '('
            params = []
            while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != ")":
                param_type = self.code[self.token_pos]
                self.verify(VARTYPE_TOKEN)
                param_name = self.code[self.token_pos]
                self.verify(VARNAME_TOKEN)
                params.append((param_name, param_name))
                if self.op_toks[self.token_pos] == KEYWORD_TOKEN and self.code[self.token_pos] == ",":
                    self.token_pos += 1  # Skip ','
                elif self.op_toks[self.token_pos] == KEYWORD_TOKEN and self.code[self.token_pos] == ")":
                    break
                else:
                    self.error("Expected ',' or ')' in class declaration")
            self.verify(KEYWORD_TOKEN) # Verifying ')'
            self.verify(KEYWORD_TOKEN) # Verifying '{'
            ctor_body = []
            while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != "}":
                ctor_body.append(self.code[self.token_pos])
                self.token_pos += 1
            self.verify(KEYWORD_TOKEN)  # Verifying '}'
            self.classes[var_name] = {'params': params, 'body': func_body}
        elif var_type == "_type":
            anonymus_type = var_name
            self.verify(VARNAME_TOKEN)
            var_name_t = self.op_toks[self.token_pos]
            if anonymus_type == "int" or var_type == "decimal":
                self.verify(ASSIGN_TOKEN)
                var_value = self.parseExpression()  # Parse expression for variable value
                self.variables[var_name_t] = var_value
            elif anonymus_type == "string":
                self.verify(ASSIGN_TOKEN)
                self.verify(VALUE_TOKEN)  # Check if next token is a value
                var_value = self.code[self.token_pos - 1]
                self.variables[var_name_t] = var_value
            elif anonymus_type == "bool":
                self.verify(ASSIGN_TOKEN)
                self.verify(VALUE_TOKEN)  # Check if next token is a value
                var_value = True if self.code[self.token_pos - 1] == "true" else False
                self.variables[var_name_t] = var_value
        else:
            self.error("Unexpected token in variable declaration")

    def parseLocalVariableDeclaration(self):
        self.token_pos += 1
        self.parseVariableDeclaration()

    def parseVariableAssignment(self):
        var_name = self.code[self.token_pos]
        if var_name not in self.variables and var_name not in self.local_variables:
            self.error(f"Variable {var_name} is not declared")
            return
        self.token_pos += 1
        self.verify(ASSIGN_TOKEN)
        var_value = self.parseExpression()
        if var_name in self.variables:
            self.variables[var_name] = var_value
        else:
            self.local_variables[var_name] = var_value

    def parseFunctionCall(self):
        func_name = self.code[self.token_pos]
        if func_name not in self.methods:
            self.error(f"Function {func_name} is not declared")
            return
        self.token_pos += 1
        self.verify(KEYWORD_TOKEN)  # Verifying '('
        args = []
        while self.op_toks[self.token_pos] != KEYWORD_TOKEN or self.code[self.token_pos] != ")":
            args.append(self.parseExpression())
            if self.op_toks[self.token_pos] == KEYWORD_TOKEN and self.code[self.token_pos] == ",":
                self.token_pos += 1  # Skip ','
            elif self.op_toks[self.token_pos] == KEYWORD_TOKEN and self.code[self.token_pos] == ")":
                break
            else:
                self.error("Expected ',' or ')' in function call")
        self.verify(KEYWORD_TOKEN)  # Verifying ')'
        self.executeFunction(func_name, args)

    def parsePrintStatement(self):
        self.verify(COMMAND_TOKEN)
        self.token_pos += 1  # Verifying '('
        message = ""
        if self.op_toks[self.token_pos] == VALUE_TOKEN:
            message += self.code[self.token_pos]
            self.token_pos += 1
        elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
            var_name = self.code[self.token_pos]
            if var_name in self.variables:
                message += str(self.variables[var_name])
            elif var_name in self.local_variables:
                message += str(self.local_variables[var_name])
            else:
                self.error(f"Variable {var_name} is not declared")
                return
            self.token_pos += 1
        self.token_pos += 1  # Verifying ')'
        self.token_pos += 1
        message = message.replace('%', ' ')
        message = message.replace('"', '')
        print(message)

    def parseGetStatement(self):
        self.token_pos += 1
        self.verify(KEYWORD_TOKEN)  # Verifying '('
        message = ""
        if self.op_toks[self.token_pos] == VALUE_TOKEN:
            message += self.code[self.token_pos]
        elif self.op_toks[self.token_pos] == VARNAME_TOKEN:
            var_name = self.code[self.token_pos]
            if var_name in self.variables:
                message += str(self.variables[var_name])
            elif var_name in self.local_variables:
                message += str(self.local_variables[var_name])
            else:
                self.error(f"Variable {var_name} is not declared")
                return
            self.token_pos += 1
        self.verify(KEYWORD_TOKEN)  # Verifying ')'
        message = message.replace('%', ' ')
        message = message.replace('"', '')
        print(input(message))

    def parseExpression(self):
        expr = self.code[self.token_pos]
        self.token_pos += 1
        return expr

    def executeFunction(self, func_name, args):
        func = self.methods[func_name]
        if len(args) != len(func['params']):
            self.error(f"Function {func_name} expected {len(func['params'])} arguments but got {len(args)}")
            return
        local_vars = {}
        for i, (param_type, param_name) in enumerate(func['params']):
            local_vars[param_name] = args[i]
        self.local_variables = local_vars
        old_code = self.code
        old_op_toks = self.op_toks
        self.code = func['body']
        self.op_toks = iterateTokens(self.code)
        self.token_pos = 0
        self.doFunctionally()
        self.local_variables = {}
        self.code = old_code
        self.op_toks = old_op_toks
        self.token_pos = 0

def iterateTokens(code):
    tokenList = []
    for line in code:
        result = lexer_code(line.strip())
        if result is not None:
            tokenList.append(result)
    return tokenList

def getTokenArray(code):
    tokenArray = []
    for line in code:
        result = getTokenIndex(line.strip())
        if result is not None:
            tokenArray.append(result)
    return tokenArray
