from typing import List
# class Token:
#     def __init__(self, token_type, value):
#         self.type = token_type
#         self.value = value
#         print('165165fs1b651s6b1')
#
#     def __repr__(self):
#         print('165165fs1b651s6b1')
#         return f"{self.type}({self.value})"

tokensTable = []
class Lexer:
    def __init__(self, transition_table, accepting_states):
        self.transition_table = transition_table
        self.accepting_states = accepting_states
        self.current_state = 0
        self.current_token = ''
        self.tokenTable = [['','']]  # define tokenTable attribute here

    def currentToken(self, token, state, tokenTable):
        if state == 58:
            tokenTable.append(['VariableDecl', 'LET'])
            return tokenTable

        if state == 60:
            #print(tokenTable[-1][0])
            if tokenTable[-1][0] == 'Variable':
                tokenTable[-1][1] += token
                return tokenTable
            else:
                tokenTable.append(['Variable', token])
                return tokenTable

        if state == 1 or state == 102:
            if tokenTable[-1][0] == 'ExpVariable':
                tokenTable[-1][1] += token
                return tokenTable
            else:
                tokenTable.append(['ExpVariable', token])
                return tokenTable

        if state == 37:
            if tokenTable[-1][0] == 'Integer':
                tokenTable[-1][1] += token
                return tokenTable
            else:
                tokenTable.append(['Integer', token])
                return tokenTable

        if state == 2 or state == 8 or state == 4 or state == 5 or state == 6 or state == 7:
            if tokenTable[-1][0] == 'BinaryOp':
                tokenTable[-1][1] += token
                return tokenTable
            else:
                tokenTable.append(['BinaryOp', token])
                return tokenTable



        if state == 39 or state == 40 or state == 41 or state == 42 or state == 43 or state == 44 or state == 45:
            if tokenTable[-1][0] == 'ColourLiteral':
                tokenTable[-1][1] += token
                return tokenTable
            else:
                tokenTable.append(['ColourLiteral', token])
                return tokenTable

        if state == 19:
            tokenTable.append(['PadWidth', '__width'])
            return tokenTable

        if state == 25:
            tokenTable.append(['PadHeight', '__height'])
            return tokenTable

        if state == 49:
            tokenTable.append(['BooleanLiteral', 'True'])
            return tokenTable

        if state == 54:
            tokenTable.append(['BooleanLiteral', 'False'])
            return tokenTable

        if state == 30:
            tokenTable.append(['PadRandI', '__randi'])
            return tokenTable

        if state == 140:
            tokenTable.append(['PadRead', '__read'])
            return tokenTable

        if state == 138:
            tokenTable.append(['Comma', ' , '])
            return tokenTable

        if token == '(':
            tokenTable.append(['OpenPar', ' ( '])
            return tokenTable

        if token == ')':
            tokenTable.append(['ClosePar', ' ) '])
            return tokenTable

        if token == '{':
            tokenTable.append(['OpenBlock', ' { '])
            return tokenTable

        if token == '}':
            tokenTable.append(['CloseBlock', ' } '])
            return tokenTable

        if state == 12:
            tokenTable.append(['Unary', 'Not'])
            return tokenTable

        if state == 11:
            tokenTable.append(['Unary', token])
            return tokenTable

        if state == 87:
            tokenTable.append(['PrintStat', '__print'])
            return tokenTable

        if state == 92:
            tokenTable.append(['DelayStat', '__delay'])
            return tokenTable

        if state == 97:
            tokenTable.append(['ReturnStat', 'return'])
            return tokenTable

        if state == 136:
            tokenTable.append(['PixelStat', '__pixel'])
            return tokenTable

        if state == 137 :
            if tokenTable[-1][0] == 'PixelStat':
                tokenTable[-1][1] += token
                return tokenTable
            else:
                tokenTable.append(['PixelStat', token])
                return tokenTable

        if state == 125:
            tokenTable.append(['IfStat', ' IF'])
            return tokenTable

        if state == 132:
            tokenTable.append(['ElseStat', ' ELSE '])
            return tokenTable

        if state == 111:
            tokenTable.append(['ForStat', ' FOR '])
            return tokenTable

        if state == 121:
            tokenTable.append(['WhileStat', ' While '])
            return tokenTable

        if token == ';':
            tokenTable.append(['SemiCol', ' ; '])
            return tokenTable

        if token == ',':
            tokenTable.append(['Comma', ' , '])
            return tokenTable

        if state == 100:
            tokenTable.append(['FunctionDecl', ' FUN '])
            return tokenTable

        if state == 68:
            tokenTable.append(['Type', ' FLOAT '])
            return tokenTable

        if state == 71:
            tokenTable.append(['Type', ' INT '])
            return tokenTable

        if state == 74:
            tokenTable.append(['Type', ' BOOL '])
            return tokenTable

        if state == 79:
            tokenTable.append(['Type', ' COLOUR '])
            return tokenTable
        return tokenTable

    def get_next_token(self, input_string):
        self.current_state = 0
        self.current_token = ''
        self.table = []
        for char in input_string:
            try:
                self.current_state = self.transition_table[(self.current_state, char)]
                self.current_token += char
                self.table.append((char, self.current_state))

                #print(f"Current token: {self.current_token}, current state: {self.current_state}")

                self.tokenTable = self.currentToken(char, self.current_state, self.tokenTable)  # pass tokenTable as argument


            except KeyError:
                return False, self.current_token, self.current_state, self.table

        #print(self.tokenTable)

        if self.current_state in self.accepting_states:
            print(f"Valid syntax! Current token: {input_string}, current state: {self.current_state}")


            return self.tokenTable
        else:
            print(f"Invalid syntax! Current token: {input_string}, current state: {self.current_state}")
            #return False, self.current_token, self.current_state, self.table

# class ASTNode:
#     def __init__(self, value: str, children: List = []):
#         self.value = value
#         self.children = children
#
#     def __str__(self):
#         return f"{self.value}: {self.children}"



class Parser:
    #def __init__(self, lexer, input_string):
    def __init__(self, tokenTable):
        self.lexer = lexer
        #self.tokenTable = self.lexer.get_next_token(input_string)
        self.tokenTable = tokenTable
        self.current_token_index = 1


    def error(self, message):
        raise Exception(message)

    def parse_selector(self):
        if self.tokenTable[self.current_token_index][0] == 'FunctionDecl':
            return (self.parse_function_decl())

        if self.tokenTable[self.current_token_index][0] == 'VariableDecl':
            return(self.parse_variable_decl())

        if self.tokenTable[self.current_token_index][0] == 'Variable':
            return(self.parse_variable())

        if self.tokenTable[self.current_token_index][0] == 'PrintStat':
            return(self.parse_print())

        if self.tokenTable[self.current_token_index][0] == 'DelayStat':
            return(self.parse_delay())

        if self.tokenTable[self.current_token_index][0] == 'ReturnStat':
            return(self.parse_return())

        if self.tokenTable[self.current_token_index][0] == 'PixelStat':
            return(self.parse_pixel())

        if self.tokenTable[self.current_token_index][0] == 'OpenBlock':
            return(self.parse_block())

        if self.tokenTable[self.current_token_index][0] == 'WhileStat':
            return(self.parse_while())

        if self.tokenTable[self.current_token_index][0] == 'IfStat':
            return(self.parse_ifElse())


        if self.tokenTable[self.current_token_index][0] == 'ForStat':
            return (self.parse_for())

        return {'No choice'}

    def parse_sel(self):
        ast = []
        while(self.current_token_index < len(self.tokenTable)-1):

            if self.tokenTable[self.current_token_index][0] == 'FunctionDecl':
                ast.append(self.parse_function_decl())

            elif self.tokenTable[self.current_token_index][0] == 'VariableDecl':
                ast.append(self.parse_variable_decl())

            elif self.tokenTable[self.current_token_index][0] == 'Variable':
                ast.append(self.parse_variable())

            elif self.tokenTable[self.current_token_index][0] == 'PrintStat':
                ast.append(self.parse_print())

            elif self.tokenTable[self.current_token_index][0] == 'DelayStat':
                ast.append(self.parse_delay())

            elif self.tokenTable[self.current_token_index][0] == 'ReturnStat':
                ast.append(self.parse_return())

            elif self.tokenTable[self.current_token_index][0] == 'PixelStat':
                ast.append(self.parse_pixel())

            elif self.tokenTable[self.current_token_index][0] == 'OpenBlock':
                ast.append(self.parse_block())

            elif self.tokenTable[self.current_token_index][0] == 'WhileStat':
                ast.append(self.parse_while())

            elif self.tokenTable[self.current_token_index][0] == 'IfStat':
                ast.append(self.parse_ifElse())

            elif self.tokenTable[self.current_token_index][0] == 'ForStat':
                ast.append(self.parse_for())

            else:
                ast.append({'No choice'})


        return(ast)


    #might need to remove useless
    def get_current_token(self):
        return self.tokenTable[self.current_token_index]

    def parse_function_decl(self):
        # Expect the next token to be FunctionDecl

        if self.tokenTable[self.current_token_index][0] != 'FunctionDecl':
            self.error('Expected FunctionDecl')
        self.current_token_index += 1

        # Expect the next token to be the function name
        if self.tokenTable[self.current_token_index][0] != 'ExpVariable':
            self.error('Expected function name')
        func_name = self.tokenTable[self.current_token_index][1]
        self.current_token_index += 1

        # Expect the next token to be OpenPar
        if self.tokenTable[self.current_token_index][0] != 'OpenPar':
            self.error('Expected (')
        self.current_token_index += 1

        # Parse the function parameters
        params = []
        while True:
            if self.tokenTable[self.current_token_index][0] == 'ClosePar':
                break

            if self.tokenTable[self.current_token_index][0] != 'Variable':
                self.error('Expected variable name')

            param_name = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            if self.tokenTable[self.current_token_index][0] != 'Type':
                self.error('Expected parameter type')

            param_type = self.tokenTable[self.current_token_index][1]
            params.append((param_name, param_type))
            self.current_token_index += 1
            if self.tokenTable[self.current_token_index][0] != 'Comma' and self.tokenTable[self.current_token_index][
                0] != 'ClosePar':
                self.error('Expected , or )')

            if self.tokenTable[self.current_token_index][0] == 'Comma':
                self.current_token_index += 1


        self.current_token_index += 1
        return_type = self.tokenTable[self.current_token_index][1]
        if self.tokenTable[self.current_token_index][0] != 'Type':
            self.error('Expected parameter type')

        #self.current_token_index += 1
        # Expect the next token to be OpenBrace
        # if self.tokenTable[self.current_token_index][0] != 'OpenBlock':
        #     self.error('Expected {')

        self.current_token_index += 1
        block = self.parse_block()

        #print('func decl', self.tokenTable[self.current_token_index][0])
        # Construct and return the FunctionDecl AST node

        info = {'Function name': func_name, 'params': params, 'Return type': return_type, 'Block': block}
        #print('/*-/*-/*-/*-/*-/*-/*/*-/*-/*-/*-',self.current_token_index)
        return {'Function_Decl': info}

    def parse_variable_decl(self):
        # Expect the next token to be VariableDecl
        if self.tokenTable[self.current_token_index][0] != 'VariableDecl':
            self.error('Expected VariableDecl')
        self.current_token_index += 1

        # Expect the next token to be Variable
        if self.tokenTable[self.current_token_index][0] != 'Variable':
            self.error('Expected variable name')
        var_name = self.tokenTable[self.current_token_index][1]
        self.current_token_index += 1


        # Expect the next token to be Type
        if self.tokenTable[self.current_token_index][0] != 'Type':
            self.error('Expected type')
        var_type = self.tokenTable[self.current_token_index][1]
        self.current_token_index += 1

        # Parse the expression
        expr = self.parse_expr()

        #self.current_token_index += 1
        # Expect the next token to be SemiColon
        if self.tokenTable[self.current_token_index][0] != 'SemiCol':
            self.error('Expected ;')
        self.current_token_index += 1

        #print('varibake decl', self.tokenTable[self.current_token_index][0])
        # Construct and return the VariableDecl AST node

        info ={'name': var_name, 'type': var_type, 'expr': expr}
        return {'Variable_Decl': info}

    def parse_expr(self):

        left = self.parse_simple_expr()

        #self.current_token_index += 1

        if self.tokenTable[self.current_token_index][1] == '<' or \
                self.tokenTable[self.current_token_index][1] == '>' or \
                self.tokenTable[self.current_token_index][1] == '==' or \
                self.tokenTable[self.current_token_index][1] == '!=' or \
                self.tokenTable[self.current_token_index][1] == '<=' or \
                self.tokenTable[self.current_token_index][1] == '>=':



            op = self.tokenTable[self.current_token_index][1]

            self.current_token_index += 1
            right = self.parse_simple_expr()

            #print('expr', self.tokenTable[self.current_token_index][0])
            return {'Expression Op': op, 'Left Side': left, 'Right Side': right}

        else:
            #print('expr', self.tokenTable[self.current_token_index][0])
            return left

    def parse_simple_expr(self):

        left = self.parse_term()
        #self.current_token_index += 1

        if self.tokenTable[self.current_token_index][1] == '+' or\
                self.tokenTable[self.current_token_index][1] == '-' or \
                self.tokenTable[self.current_token_index][1] == 'or':

            op = self.tokenTable[self.current_token_index][1]

            self.current_token_index += 1
            right = self.parse_term()
            #self.current_token_index += 1
            #print('simple expr', self.tokenTable[self.current_token_index][0])
            return {'Expression Op': op, 'Left Side': left, 'Right Side': right}

        else:
            #print('simple expr', self.tokenTable[self.current_token_index][0])
            return left

    def parse_term(self):

        left = self.parse_factor()

        #self.current_token_index += 1

        if self.tokenTable[self.current_token_index][1] == '*' or \
                self.tokenTable[self.current_token_index][1] == '/' or \
                self.tokenTable[self.current_token_index][1] == 'and':
            op = self.tokenTable[self.current_token_index][1]

            self.current_token_index += 1
            right = self.parse_factor()
            #self.current_token_index += 1
            #print('term', self.tokenTable[self.current_token_index][0])
            return {'Expression Op': op, 'Left Side': left, 'Right Side': right}

        else:
            #print('term', self.tokenTable[self.current_token_index][0])
            return left

    def parse_factor(self):
        expTable = []


        if self.tokenTable[self.current_token_index][0] == 'ExpVariable':
            var_name = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1

            if self.tokenTable[self.current_token_index][0] == 'OpenPar':
                #function call
                self.current_token_index += 1
                exp = self.parse_expr()
                expTable.append(exp)
                while(self.tokenTable[self.current_token_index][0] == 'Comma'):
                    self.current_token_index += 1
                    exp = self.parse_expr()
                    expTable.append(exp)

                self.current_token_index += 1
                #print('factor', self.tokenTable[self.current_token_index][0])
                return{'FunctionName': var_name, 'Parameters': expTable}
            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'ExpVariable': var_name}

        if self.tokenTable[self.current_token_index][0] == 'Integer':
            token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'Integer': token}

        if self.tokenTable[self.current_token_index][0] == 'BooleanLiteral':
            token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'BooleanLiteral': token}

        if self.tokenTable[self.current_token_index][0] == 'ColourLiteral':
            var_name = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'ColourLiteral': var_name}

        if self.tokenTable[self.current_token_index][0] == 'PadWidth':
            token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'PadWidth': token}

        if self.tokenTable[self.current_token_index][0] == 'PadHeight':
            token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'PadHeight': token}

        #PadRead
        if self.tokenTable[self.current_token_index][0] == 'PadRead':
            token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            firstEx = self.parse_expr()

            if self.tokenTable[self.current_token_index][0] != 'Comma':
                self.error('Expected ,')
            self.current_token_index += 1

            secondEx = self.parse_expr()

            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'PadRead': token, 'First expression': firstEx, 'Second Expression': secondEx}

        if self.tokenTable[self.current_token_index][0] == 'PadRandI':
            token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            firstEx = self.parse_expr()

            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'PadRandI': token, 'Expression': firstEx}

        if self.tokenTable[self.current_token_index][0] == 'Unary':
            token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            firstEx = self.parse_expr()

            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'Unary': token, 'Expression': firstEx}

        if self.tokenTable[self.current_token_index][0] == 'OpenPar':
            #token = self.tokenTable[self.current_token_index][1]
            self.current_token_index += 1
            exp = self.parse_expr()

            if self.tokenTable[self.current_token_index][0] != 'ClosePar':
                self.error('Expected )')
            self.current_token_index += 1

            #print('factor', self.tokenTable[self.current_token_index][0])
            return {'SubExpr': '( )', 'Expression': exp}

        self.error('Expected a Valid Expression')

    def parse_variable(self):
        var_name = self.tokenTable[self.current_token_index][1]
        self.current_token_index += 1

        if(self.tokenTable[self.current_token_index][1]  == '='):
            self.current_token_index += 1
        #print('variable', self.tokenTable[self.current_token_index-2][1])
        # Parse the expression
        expr = self.parse_expr()
        self.current_token_index += 1
        #print('variable', self.tokenTable[self.current_token_index][0])
        info = {'Name': var_name, 'Expression': expr}
        return {'Variable': info}

    def parse_print(self):
        self.current_token_index += 1

        # Parse the expression
        expr = self.parse_expr()
        #print('print', self.tokenTable[self.current_token_index][0])
        self.current_token_index += 1
        info = {'Expression': expr}
        return {'PrintStat': info, }

    def parse_delay(self):
        self.current_token_index += 1

        # Parse the expression
        expr = self.parse_expr()
        #print('delay', self.tokenTable[self.current_token_index][0])
        self.current_token_index += 1
        info = {'Expression': expr}
        return {'DelayStat': info}

    def parse_return(self):
        self.current_token_index += 1

        # Parse the expression
        expr = self.parse_expr()
        #print('return', self.tokenTable[self.current_token_index][0])
        self.current_token_index += 1
        #print('return', self.tokenTable[self.current_token_index][0])
        info = {'Expression': expr}
        return {'ReturnStat': info}

    def parse_pixel(self):
        expTable = []
        token = self.tokenTable[self.current_token_index][1]
        self.current_token_index += 1

        if token == '__pixelr':
            expr = self.parse_expr()
            expTable.append(expr)
            for i in range(4):
                if self.tokenTable[self.current_token_index][0] != 'Comma':
                    self.error('Expected a Valid Expression')
                self.current_token_index += 1
                expr = self.parse_expr()
                expTable.append(expr)


        if token == '__pixel':
            expr = self.parse_expr()
            expTable.append(expr)
            for i in range(2):
                if self.tokenTable[self.current_token_index][0] != 'Comma':
                    self.error('Expected a Valid Expression')
                self.current_token_index += 1
                expr = self.parse_expr()
                expTable.append(expr)

        if self.tokenTable[self.current_token_index][0] != 'SemiCol':
            self.error('Invalid Number Of Expressions')
        #print('Pixel', self.tokenTable[self.current_token_index][0])
        self.current_token_index += 1
        info= {'Type:': token, 'Expressions': expTable}
        return {'Pixel_Statment': info }


    def parse_block(self):
        #print('BLOCK *-*-*-*--*-*-* BLOCK')
        self.current_token_index += 1
        statTable = []


        while(True):
         #   print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
          #  print(self.tokenTable[self.current_token_index][0])
           # print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            #print(len(self.tokenTable))

            statement = self.parse_selector()
            #print(self.tokenTable[self.current_token_index][0])
            #print(self.current_token_index)
            statTable.append(statement)
            #print(statTable)



            #and self.current_token_index == len(self.tokenTable)
            if (self.tokenTable[self.current_token_index][0] == 'CloseBlock'):
                if (self.current_token_index == len(self.tokenTable) - 1):
                    info = {'Statement': statTable}
                    return {'Block': info}
                break





        self.current_token_index += 1
        info = {'Statement': statTable}

        return {'Block': info }

    def parse_while(self):
        self.current_token_index += 1

        # Parse the expression
        if self.tokenTable[self.current_token_index][0] != 'OpenPar':
            self.error('Invalid While loop')

        self.current_token_index += 1
        expr = self.parse_expr()

        if self.tokenTable[self.current_token_index][0] != 'ClosePar':
            self.error('Invalid While loop')

        #self.current_token_index += 1
        #print('->->->_')
        block = self.parse_block()



        #self.current_token_index += 1
        #self.current_token_index += 1

        #print('While', self.tokenTable[self.current_token_index][0])
        info =  {'Expression': expr, 'Block': block}
        return {'While Stat': info}

    def parse_ifElse(self):
        self.current_token_index += 1

        # Parse the expression
        if self.tokenTable[self.current_token_index][0] != 'OpenPar':
            self.error('Invalid While loop')

        self.current_token_index += 1
        expr = self.parse_expr()

        if self.tokenTable[self.current_token_index][0] != 'ClosePar':
            self.error('Invalid While loop')

        self.current_token_index += 1
        block = self.parse_block()
        #self.current_token_index += 1


        if self.tokenTable[self.current_token_index][0] == 'ElseStat':
            #self.current_token_index += 1
            #print('IFELSE', self.tokenTable[self.current_token_index][0])
            eBlock = self.parse_block()
            #print('IF+*ELSE', self.tokenTable[self.current_token_index][0])
            #self.current_token_index += 1
            #eInfo = {eBlock}
            info = {'Expression': expr, 'Block': block, 'ELSE_Stat': eBlock}
            return {'IF_Stat': info}
        else:
            #print('IF', self.tokenTable[self.current_token_index][0])
            #self.current_token_index += 1
            info = {'Expression': expr, 'Block': block}
            return {'IF_Stat': info}

    def parse_for(self):
        self.current_token_index += 1

        # Parse the expression
        if self.tokenTable[self.current_token_index][0] != 'OpenPar':
            self.error('Invalid For loop')

        self.current_token_index += 1
        varDecl = ''

        if self.tokenTable[self.current_token_index][0] == 'VariableDecl':
            varDecl = self.parse_variable_decl()

        self.current_token_index -= 1


        if self.tokenTable[self.current_token_index][0] != 'SemiCol':
            self.error('Invalid For loop')

        self.current_token_index += 1

        expr = self.parse_expr()

        if self.tokenTable[self.current_token_index][0] != 'SemiCol':
            self.error('Invalid For loop')

        self.current_token_index += 1
        assignment = ''
        if self.tokenTable[self.current_token_index][0] == 'ExpVariable':
            assignment = self.parse_variable()
            self.current_token_index -= 1

        if self.tokenTable[self.current_token_index][0] != 'ClosePar':
            self.error('Invalid For loop')

        self.current_token_index += 1

        block = self.parse_block()

        info = {'Variable Decl' : varDecl, 'Expression': expr, 'Assignment': assignment, 'Block': block}
        return {'For Stat': info}


class XmlVisitor:
    def __init__(self, ast_dict):
        self.xml = ''
        self.indentation = 0
        self.ast_dict = ast_dict

    def visit(self, node):
        if isinstance(node, dict):
            for key, value in node.items():
                #print(key)
                #print(value)
                self.indent()
                self.xml += f"<{key}>"
                self.indentation += 1
                self.xml += '\n'
                self.visit(value)
                self.indent()
                self.xml += f"</{key}>"
                self.xml += '\n'
                self.indentation -= 1
        elif isinstance(node, list):
            for item in node:
                self.visit(item)
        else:
            self.indent()
            self.xml += str(node)
            self.xml += '\n'

    def indent(self):
        self.xml += '  ' * self.indentation

    def write_to_file(self, file_path):
        with open(file_path, 'w') as f:
            f.write(self.xml)

    def generate_xml(self):
        self.visit(self.ast_dict)
        return self.xml


class SemanticAnalysis:
    def __init__(self, ast):
        self.ast = ast
        self.symbolTable = [[],[]]
        self.newScope = False
        self.functionTable = []

        # to check for duplicate variable declaration
        self.variableDecl()

    def error(self, message):
        raise Exception(message)
    def addVariable(self, name, type, location):

        #global scope
        for i in self.symbolTable[0]:
            if i[0] == name:
                #already exist
                self.error('Variable ' + i[0] + ' already declared')

        if location == 0:
            self.symbolTable[0].append([name, type])

        if location == 1:
            if self.newScope == True:
                self.symbolTable[1].append([[name, type]])
            else:
                for i in self.symbolTable[1][-1]:
                    if i[0] == name:
                        # already exists
                        self.error('Variable ' + i[0] + ' already declared')
                self.symbolTable[1][-1].append([name, type])

    def getType(self,name,scope):
        for i in self.symbolTable[0]:
            if i[0] == name:
                #already exist
                return i[1]
        if scope == 1:
            if len(self.symbolTable[1]) != 0:
                for i in self.symbolTable[1][-1]:
                    if i[0] == name:
                        return i[1]

    def searchVariable(self, name, scope):
        #global scope
        for i in self.symbolTable[0]:
            if i[0] == name:
                #already exist
                return True
        if scope == 1:
            if len(self.symbolTable[1]) != 0:
                for i in self.symbolTable[1][-1]:
                    if i[0] == name:
                        return True
                return False
            else:
                return False
        else:
            return False
    def statCheck(self, statement, scope):

        if 'Variable' in statement:
            var = statement['Variable']
            self.assignmentCheck(var, scope)

        if 'Variable_Decl' in statement:
            var_decl = statement['Variable_Decl']
            self.varDeclCheck(var_decl, scope)

        if 'While Stat' in statement:
            whileStat = statement['While Stat']
            self.whileStatCheck(whileStat, scope)

        if 'IF_Stat' in statement:
            ifStat = statement['IF_Stat']
            self.ifStatCheck(ifStat,scope)

        if 'For Stat' in statement:
            forStat = statement['For Stat']
            self.forStatCheck(forStat,scope)

        if 'PrintStat' in statement:
            printStat = statement['PrintStat']
            self.printReturnDelayStatCheck(printStat,scope)

        if 'ReturnStat' in statement:
            Stat = statement['ReturnStat']
            self.returnStatCheck(Stat, scope)


        if 'DelayStat' in statement:
            Stat = statement['DelayStat']
            self.printReturnDelayStatCheck(Stat, scope)

        if 'Pixel_Statment' in statement:
            Stat = statement['Pixel_Statment']
            self.pixelStatCheck(Stat, scope)

    def varDeclCheck(self, Stat, scope):
        find = False
        name = Stat['name']
        type = Stat['type']
        self.addVariable(name, type, scope)
        #print(name,type)
        exp = Stat['expr']
        array = self.flatten_dict(exp)
        for i in range(len(array)):
            #8print(array[i])
            if array[i] == 'ExpVariable':
                find = self.searchVariable(array[i+1], scope)
                #print(array[i+1],find)
                if find == False:
                    self.error('Variable "' + array[i+1] + '" not declared')
                else:
                    if self.getType(array[i + 1], scope) != type:
                        self.error('Variable "' + array[i + 1] + '" do not match the type of ' + name)
            elif array[i] == 'BooleanLiteral':
                #print(type)
                if type != ' BOOL ':
                    self.error('Variable "' + name + '" does not except boolean')
            elif array[i] == 'ColourLiteral':
                #print(type)
                if type != ' COLOUR ':
                    self.error('Variable "' + name + '" does not except colour types')

            elif array[i] == 'PadWidth':
                if type != ' INT ':
                    self.error('Variable "' + name + '" does not except int types')

            elif array[i] == 'PadHeight':
                if type != ' INT ':
                    self.error('Variable "' + name + '" does not except int types')

            elif array[i] == 'PadRandI':
                if type != ' INT ':
                    self.error('Variable "' + name + '" does not except int types')



        self.newScope = False

    def assignmentCheck(self, assigment, scope):
        #find = False
        name = assigment['Name']
        type = self.getType(name, scope)
        find = self.searchVariable(name, scope)
        if find == False:
            self.error('Variable "' + name + '" not declared')

        exp = assigment['Expression']
        array = self.flatten_dict(exp)
        for i in range(len(array)):
            if array[i] == 'ExpVariable':
                #print(array[i + 1])
                find = self.searchVariable(array[i+1], scope)
                if find == False:
                    self.error('Variable "' + array[i + 1] + '" not declared')
                else:
                    if self.getType(array[i + 1], scope) != type:
                        self.error('Variable "' + array[i + 1] + '" do not match the type of ' + name)
            elif array[i] == 'BooleanLiteral':
                # print(type)
                if type != ' BOOL ':
                    self.error('Variable "' + name + '" does not except boolean')
            elif array[i] == 'ColourLiteral':
                # print(type)
                if type != ' COLOUR ':
                    self.error('Variable "' + name + '" does not except colour types')

            elif array[i] == 'PadWidth':
                if type != ' INT ':
                    self.error('Variable "' + name + '" does not except int types')

            elif array[i] == 'PadHeight':
                if type != ' INT ':
                    self.error('Variable "' + name + '" does not except int types')

            elif array[i] == 'PadRandI':
                if type != ' INT ':
                    self.error('Variable "' + name + '" does not except int types')



    def flatten_dict(self, dictionary):
        flattened = []
        for key, value in dictionary.items():
            flattened.append(key)
            if isinstance(value, dict):
                flattened.extend(self.flatten_dict(value))
            else:
                flattened.append(value)
        return flattened

    def forStatCheck(self, forStat, scope):
        #print(forStat)
        if 'Variable Decl' in forStat:
            var_decl = forStat['Variable Decl']['Variable_Decl']
            self.varDeclCheck(var_decl, scope)
        if 'Expression' in forStat:
            exp = forStat['Expression']
            array = self.flatten_dict(exp)
            for i in range(len(array)):
                if array[i] == 'ExpVariable':
                    find = self.searchVariable(array[i + 1], scope)
                    # print(array[i+1],find)
                    if find == False:
                        self.error('Variable "' + array[i + 1] + '" not declared')
        if 'Assignment' in forStat:
            exp = forStat['Assignment']['Variable']
            self.assignmentCheck(exp, scope)

        stat = forStat['Block']['Block']['Statement']

        for statement in stat:
            self.statCheck(statement, scope)

    def ifStatCheck(self, ifStat, scope):
        exp = ifStat['Expression']
        array = self.flatten_dict(exp)
        for i in range(len(array)):
            if array[i] == 'ExpVariable':
                find = self.searchVariable(array[i + 1], scope)
                # print(array[i+1],find)
                if find == False:
                    self.error('Variable "' + array[i + 1] + '" not declared')

        stat = ifStat['Block']['Block']['Statement']
        #print(ifStat)
        for statement in stat:
            self.statCheck(statement, scope)
        if(len(ifStat)==3):
            elseStat = ifStat['ELSE_Stat']['Block']['Statement']
            for statement in elseStat:
                self.statCheck(statement, scope)
            #print(elseStat)


        #print(block)

    def whileStatCheck(self, whileStat, scope):
        if 'Expression' in whileStat:
            exp = whileStat['Expression']
            array = self.flatten_dict(exp)
            for i in range(len(array)):
                if array[i] == 'ExpVariable':
                    find = self.searchVariable(array[i + 1], scope)
                    # print(array[i+1],find)
                    if find == False:
                        self.error('Variable "' + array[i + 1] + '" not declared')
        block = whileStat['Block']['Block']
        stat = block['Statement'][0]['Block']['Statement']
        for statement in stat:
            self.statCheck(statement, scope)

    def printReturnDelayStatCheck(self, printStat, scope):
        find = False
        exp = printStat['Expression']
        array = self.flatten_dict(exp)
        for i in range(len(array)):
            if array[i] == 'ExpVariable':
                find = self.searchVariable(array[i+1], scope)
                #print(array[i+1],find)
                if find == False:
                    self.error('Variable "' + array[i + 1] + '" not declared')

    def returnStatCheck(self, returnStat, scope):
        find = False
        exp = returnStat['Expression']
        #print(exp)
        array = self.flatten_dict(exp)

        #print(array)
        for i in range(len(array)):
            variableType = ''
            if array[i] == 'ExpVariable':
                find = self.searchVariable(array[i+1], scope)
                #print(array[i+1],find)
                if find == False:
                    self.error('Variable "' + array[i + 1] + '" not declared')
                else:
                    variableType = self.getType(array[i+1], scope)
            elif array[i] == 'BooleanLiteral':
                variableType = ' BOOL '

            elif array[i] == 'Integer':
                variableType = ' INT '

            elif array[i] == 'ColourLiteral':
                variableType = ' COLOUR '

            elif array[i] == 'PadWidth':
                variableType = ' INT '

            elif array[i] == 'PadHeight':
                variableType = ' INT '

            elif array[i] == 'PadRandI':
                variableType = ' INT '

            #print(variableType, self.functionTable[-1][1])
            #print(variableType)
            if variableType != '':
                if variableType != self.functionTable[-1][1]:
                    self.error('Wrong return type : "' + array[i + 1] + '"  needs to be' + self.functionTable[-1][1])





    def pixelStatCheck(self, pixelStat, scope):
        find = False
        exp = pixelStat['Expressions']
        #print(exp)
        mainType = pixelStat['Type:']
        #print(mainType)
        if mainType == '__pixelr':
            length = 4
        else:
            length = 2
        for item in range(len(exp)):
           # print (exp[item])
            if item < length:
                if 'ExpVariable' in exp[item]:
                    find = self.searchVariable(exp[item]['ExpVariable'], scope)
                    # print(array[i+1],find)
                    if find == False:
                        self.error('Variable "' + exp[item]['ExpVariable'] + '" not declared')

                    type = self.getType(exp[item]['ExpVariable'], scope)

                    if type != ' INT ':
                        self.error('the first four expressions are to be type int and the last one of type colour')


                elif 'Integer' not in exp[item]:
                    self.error('Integer needed')
            else:
                if 'ExpVariable' in exp[item]:
                    find = self.searchVariable(exp[item]['ExpVariable'], scope)
                    # print(array[i+1],find)
                    if find == False:
                        self.error('Variable "' + exp[item]['ExpVariable'] + '" not declared')

                    type = self.getType(exp[item]['ExpVariable'], scope)

                    if type != ' COLOUR ':
                        self.error('last one of type colour')


                elif 'ColourLiteral' not in exp[item]:
                    self.error('last one of type colour')





    #main
    def variableDecl(self):
        #check for global variables
        for i in self.ast:

            for key, value in i.items():
                self.newScope = True
                if key == 'Function_Decl':
                    hasReturn = False
                    duplicate = False
                    functionName = value['Function name']
                    functionType = value['Return type']
                    for x in self.functionTable:
                        if x[0] == functionName and x[1] == functionType:
                            duplicate = True
                    if duplicate == True:
                        self.error('Function "' + functionName + '" of type' + functionType + 'already exists.')
                    else:
                        self.functionTable.append([functionName,functionType])


                    for i in value['params']:
                        self.addVariable(i[0], i[1], 1)
                        self.newScope = False
                        #print(i)

                    block = value['Block']['Block']
                    statements = block['Statement']
                    #print(statements[2])
                    for statement in statements:
                        if 'ReturnStat' in statement:
                            hasReturn = True
                        self.statCheck(statement, 1)

                    if hasReturn == False:
                        self.error('Function "' + functionName + '" needs to has a Return statement')
                else:
                    self.statCheck({key: value}, 0)


                self.newScope = True
        print(self.symbolTable)


transition_table = {}

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hex = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
multiplicativeOp = ['*', '/', 'and']

# 〈Identifier 〉
for x in letter:
    if x == 'n':
        transition_table[(55, x)] = 9
        transition_table[(2, x)] = 9
    else:
        if x == 't':
            transition_table[(55, x)] = 46
        else:
            if x == 'f':
                transition_table[(55, x)] = 50
            else:
                transition_table[(55, x)] = 1
        #transition_table[(2, x)] = 1
    transition_table[(1, x)] = 1

    transition_table[(9, x)] = 1
    transition_table[(10, x)] = 1
    transition_table[(11, x)] = 1
    transition_table[(46, x)] = 1
    transition_table[(47, x)] = 1
    transition_table[(48, x)] = 1
    transition_table[(49, x)] = 1
    transition_table[(50, x)] = 1
    transition_table[(51, x)] = 1
    transition_table[(52, x)] = 1
    transition_table[(53, x)] = 1
    transition_table[(54, x)] = 1
    transition_table[(0, x)] = 60
    transition_table[(59, x)] = 60
    transition_table[(60, x)] = 60
    transition_table[(101, x)] = 102
    transition_table[(102, x)] = 102
    transition_table[(105, x)] = 60
    transition_table[(116, x)] = 60
    transition_table[(202, x)] = 60

    transition_table[(56, x)] = 60
    transition_table[(57, x)] = 60
    transition_table[(58, x)] = 60
    transition_table[(93, x)] = 60
    transition_table[(94, x)] = 60
    transition_table[(95, x)] = 60
    transition_table[(96, x)] = 60
    transition_table[(97, x)] = 60
    transition_table[(88, x)] = 60
    transition_table[(124, x)] = 60
    transition_table[(125, x)] = 60
    transition_table[(98, x)] = 60
    transition_table[(110, x)] = 60
    transition_table[(111, x)] = 60
    transition_table[(117, x)] = 60
    transition_table[(118, x)] = 60
    transition_table[(119, x)] = 60
    transition_table[(120, x)] = 60
    transition_table[(121, x)] = 60
    transition_table[(99, x)] = 60
    transition_table[(100, x)] = 60


for d in digit:
    transition_table[(1, d)] = 1
    transition_table[(9, d)] = 1
    transition_table[(10, d)] = 1
    transition_table[(55, d)] = 37
    transition_table[(37, d)] = 37
    transition_table[(38, d)] = 37
    transition_table[(46, d)] = 1
    transition_table[(47, d)] = 1
    transition_table[(48, d)] = 1
    transition_table[(49, d)] = 1
    transition_table[(50, d)] = 1
    transition_table[(51, d)] = 1
    transition_table[(52, d)] = 1
    transition_table[(53, d)] = 1
    transition_table[(54, d)] = 1
    transition_table[(60, d)] = 60
    transition_table[(102, d)] = 102
    transition_table[(2, d)] = 37

    transition_table[(56, d)] = 60
    transition_table[(57, d)] = 60
    transition_table[(58, d)] = 60
    transition_table[(93, d)] = 60
    transition_table[(94, d)] = 60
    transition_table[(95, d)] = 60
    transition_table[(96, d)] = 60
    transition_table[(97, d)] = 60
    transition_table[(88, d)] = 60
    transition_table[(124, d)] = 60
    transition_table[(125, d)] = 60
    transition_table[(98, d)] = 60
    transition_table[(110, d)] = 60
    transition_table[(111, d)] = 60
    transition_table[(117, d)] = 60
    transition_table[(118, d)] = 60
    transition_table[(119, d)] = 60
    transition_table[(120, d)] = 60
    transition_table[(121, d)] = 60
    transition_table[(99, d)] = 60
    transition_table[(100, d)] = 60


transition_table[(1, '_')] = 1
transition_table[(9, '_')] = 1
transition_table[(10, '_')] = 1
transition_table[(46, '_')] = 1
transition_table[(47, '_')] = 1
transition_table[(48, '_')] = 1
transition_table[(49, '_')] = 1
transition_table[(50, '_')] = 1
transition_table[(51, '_')] = 1
transition_table[(52, '_')] = 1
transition_table[(53, '_')] = 1
transition_table[(54, '_')] = 1
transition_table[(60, '_')] = 60
transition_table[(102, '_')] = 102

transition_table[(56, '_')] = 60
transition_table[(57, '_')] = 60
transition_table[(58, '_')] = 60
transition_table[(93, '_')] = 60
transition_table[(94, '_')] = 60
transition_table[(95, '_')] = 60
transition_table[(96, '_')] = 60
transition_table[(97, '_')] = 60
transition_table[(88, '_')] = 60
transition_table[(124, '_')] = 60
transition_table[(125, '_')] = 60
transition_table[(98, '_')] = 60
transition_table[(110, '_')] = 60
transition_table[(111, '_')] = 60
transition_table[(117, '_')] = 60
transition_table[(118, '_')] = 60
transition_table[(119, '_')] = 60
transition_table[(120, '_')] = 60
transition_table[(121, '_')] = 60
transition_table[(99, '_')] = 60
transition_table[(100, '_')] = 60

#spacer
transition_table[(1, ' ')] = 3
#transition_table[(2, ' ')] = 2
transition_table[(2, ' ')] = 55
transition_table[(8, ' ')] = 2
transition_table[(9, ' ')] = 3
transition_table[(10, ' ')] = 3
transition_table[(12, ' ')] = 55
transition_table[(19, ' ')] = 3
transition_table[(25, ' ')] = 3
transition_table[(30, ' ')] = 55
transition_table[(140, ' ')] = 55
transition_table[(34, ' ')] = 55
transition_table[(35, ' ')] = 55
transition_table[(37, ' ')] = 3
transition_table[(45, ' ')] = 3
transition_table[(58, ' ')] = 59
transition_table[(60, ' ')] = 61
transition_table[(62, ' ')] = 55
transition_table[(63, ' ')] = 64
transition_table[(69, ' ')] = 80
transition_table[(81, ' ')] = 55
transition_table[(88, ' ')] = 55
transition_table[(100, ' ')] = 101
transition_table[(103, ' ')] = 59
transition_table[(104, ' ')] = 105
transition_table[(106, ' ')] = 107
transition_table[(109, ' ')] = 64
transition_table[(111, ' ')] = 112
transition_table[(113, ' ')] = 114
transition_table[(31, ' ')] = 55
transition_table[(115, ' ')] = 55
transition_table[(31, ' ')] = 55
transition_table[(36, ' ')] = 3
transition_table[(117, ' ')] = 200
#transition_table[(37, ' ')] = 1
transition_table[(8, ' ')] = 55
transition_table[(7, ' ')] = 55
transition_table[(121, ' ')] = 122
transition_table[(123, ' ')] = 55
transition_table[(0, ' ')] = 0


#transition_table[(36, '}')] = 200




#〈MultiplicativeOp〉
transition_table[(3, '*')] = 2
transition_table[(3, '/')] = 2
transition_table[(3, 'a')] = 4
transition_table[(4, 'n')] = 5
transition_table[(5, 'd')] = 2

#〈AdditiveOp〉 ::= ‘+’ | ‘-’ | ‘or’
transition_table[(3, '+')] = 2
transition_table[(3, '-')] = 2
transition_table[(3, 'o')] = 6
transition_table[(6, 'r')] = 2

#〈RelationalOp〉 ::= ‘<’ | ‘>’ | ‘==’ | ‘!=’ | ‘<=’ | ‘>=’
transition_table[(3, '=')] = 7
transition_table[(3, '!')] = 7
transition_table[(7, '=')] = 2
transition_table[(3, '<')] = 8
transition_table[(3, '>')] = 8
transition_table[(8, '=')] = 2

#〈Unary〉
transition_table[(9, 'o')] = 10
transition_table[(10, 't')] = 12
transition_table[(55, '-')] = 11
transition_table[(2, '-')] = 11

#〈PadWidth〉 :: = ‘__width’
transition_table[(55, '_')] = 13
transition_table[(13, '_')] = 14
transition_table[(2, '_')] = 13
transition_table[(14, 'w')] = 15
transition_table[(15, 'i')] = 16
transition_table[(16, 'd')] = 17
transition_table[(17, 't')] = 18
transition_table[(18, 'h')] = 19


#〈PadHeight〉 :: = ‘__height’
transition_table[(14, 'h')] = 20
transition_table[(20, 'e')] = 21
transition_table[(21, 'i')] = 22
transition_table[(22, 'g')] = 23
transition_table[(23, 'h')] = 24
transition_table[(24, 't')] = 25

#〈PadRandI〉 :: = ‘__randi’ 〈Expr 〉
transition_table[(14, 'r')] = 26
transition_table[(26, 'a')] = 27
transition_table[(27, 'n')] = 28
transition_table[(28, 'd')] = 29
transition_table[(29, 'i')] = 30

#〈PadRead〉 :: = ‘__read’ 〈Expr 〉‘,’〈Expr 〉
transition_table[(26, 'e')] = 32
transition_table[(32, 'a')] = 33
transition_table[(33, 'd')] = 140
transition_table[(3, ',')] = 34

#〈FunctionCall〉 ::= 〈Identifier 〉 ‘(’ [ 〈ActualParams〉 ] ‘)’
transition_table[(3, '(')] = 35
transition_table[(35, ')')] = 36
transition_table[(3, ')')] = 36

# <IntegerLiteral〉 ::= 〈Digit〉 { 〈Digit〉 }
# 〈FloatLiteral〉 ::= 〈Digit〉 { 〈Digit〉 } ‘.’ 〈Digit〉 { 〈Digit〉 }
transition_table[(37, '.')] = 38

#〈ColourLiteral〉 ::= ‘#’ 〈Hex 〉 〈Hex 〉 〈Hex 〉 〈Hex 〉 〈Hex 〉 〈Hex 〉
transition_table[(55, '#')] = 39
for h in hex:
    transition_table[(39, h)] = 40
    transition_table[(40, h)] = 41
    transition_table[(41, h)] = 42
    transition_table[(42, h)] = 43
    transition_table[(43, h)] = 44
    transition_table[(44, h)] = 45

#〈BooleanLiteral〉 ::= ‘true’ | ‘false’
#transition_table[(26, 't')] = 32
transition_table[(46, 'r')] = 47
transition_table[(47, 'u')] = 48
transition_table[(48, 'e')] = 49

transition_table[(50, 'a')] = 51
transition_table[(51, 'l')] = 52
transition_table[(52, 's')] = 53
transition_table[(53, 'e')] = 54

#〈SubExpr 〉 ::= ‘(’ 〈Expr 〉 ‘)’
transition_table[(55, '(')] = 35

#〈VariableDecl〉 ::= ‘let’ 〈Identifier 〉 ‘:’ 〈Type〉 ‘=’ 〈Expr 〉
transition_table[(0, 'l')] = 56
transition_table[(56, 'e')] = 57
transition_table[(57, 't')] = 58

transition_table[(61, '=')] = 62
transition_table[(61, ':')] = 63

transition_table[(64, 'f')] = 65
transition_table[(65, 'l')] = 66
transition_table[(66, 'o')] = 67
transition_table[(67, 'a')] = 68
transition_table[(68, 't')] = 69

transition_table[(64, 'i')] = 70
transition_table[(70, 'n')] = 71
transition_table[(71, 't')] = 69

transition_table[(64, 'b')] = 72
transition_table[(72, 'o')] = 73
transition_table[(73, 'o')] = 74
transition_table[(74, 'l')] = 69

transition_table[(64, 'c')] = 75
transition_table[(75, 'o')] = 76
transition_table[(76, 'l')] = 77
transition_table[(77, 'o')] = 78
transition_table[(78, 'u')] = 79
transition_table[(79, 'r')] = 69

transition_table[(80, '=')] = 81

# 〈PrintStatement〉 ::= ‘__print’ 〈Expr 〉
transition_table[(0, '_')] = 82
transition_table[(82, '_')] = 83
transition_table[(83, 'p')] = 84
transition_table[(84, 'r')] = 85
transition_table[(85, 'i')] = 86
transition_table[(86, 'n')] = 87
transition_table[(87, 't')] = 88

#〈DelayStatement〉 ::= ‘__delay’ 〈Expr 〉
transition_table[(83, 'd')] = 89
transition_table[(89, 'e')] = 90
transition_table[(90, 'l')] = 91
transition_table[(91, 'a')] = 92
transition_table[(92, 'y')] = 88

# 〈RtrnStatement〉 ::= ‘return’ 〈Expr 〉
transition_table[(0, 'r')] = 93
transition_table[(93, 'e')] = 94
transition_table[(94, 't')] = 95
transition_table[(95, 'u')] = 96
transition_table[(96, 'r')] = 97
transition_table[(97, 'n')] = 88

#〈FunctionDecl〉 ::= ‘fun’ 〈Identifier 〉 ‘(’ [ 〈FormalParams〉 ] ‘)’ ‘->’ 〈Type〉 〈Block〉
transition_table[(0, 'f')] = 98
transition_table[(98, 'u')] = 99
transition_table[(99, 'n')] = 100
transition_table[(102, '(')] = 103
transition_table[(80, ',')] = 104
transition_table[(80, ')')] = 106
transition_table[(103, ')')] = 106
transition_table[(107, '-')] = 108
transition_table[(108, '>')] = 109
transition_table[(80, '{')] = 201

#〈ForStatement〉 ::= ‘for’ ‘(’ [ 〈VariableDecl〉 ] ’;’ 〈Expr 〉 ’;’ [ 〈Assignment〉 ] ‘)’ 〈Block〉
transition_table[(98, 'o')] = 110
transition_table[(110, 'r')] = 111
transition_table[(112, '(')] = 113
transition_table[(113, ';')] = 115
transition_table[(114, 'l')] = 56
transition_table[(116, ')')] = 117
transition_table[(1, ')')] = 36
transition_table[(55, ')')] = 36

#〈WhileStatement〉 ::= ‘while’ ‘(’ 〈Expr 〉 ‘)’ 〈Block〉
transition_table[(0, 'w')] = 117
transition_table[(117, 'h')] = 118
transition_table[(118, 'i')] = 119
transition_table[(119, 'l')] = 120
transition_table[(120, 'e')] = 121
transition_table[(122, '(')] = 123

#〈IfStatement〉 ::= ‘if’ ‘(’ 〈Expr 〉 ‘)’ 〈Block〉 [ ‘else’ 〈Block〉 ]

transition_table[(0, 'i')] = 124
transition_table[(124, 'f')] = 125
transition_table[(125, ' ')] = 126
transition_table[(126, '(')] = 127
transition_table[(127, ' ')] = 55
transition_table[(128, 'e')] = 129
transition_table[(129, 'l')] = 130
transition_table[(130, 's')] = 131
transition_table[(131, 'e')] = 132
transition_table[(132, ' ')] = 200
transition_table[(200, '{')] = 201

# 〈PixelStatement〉 ::= ‘__pixelr’ 〈Expr 〉‘,’〈Expr 〉‘,’〈Expr 〉‘,’〈Expr 〉‘,’〈Expr 〉
# | ‘__pixel’ 〈Expr 〉‘,’〈Expr 〉‘,’〈Expr 〉

transition_table[(84, 'i')] = 133
transition_table[(133, 'x')] = 134
transition_table[(134, 'e')] = 135
transition_table[(135, 'l')] = 136
transition_table[(136, ' ')] = 55
transition_table[(136, 'r')] = 137
transition_table[(137, ' ')] = 55
transition_table[(3, ',')] = 138
transition_table[(138, ' ')] = 55


#〈Block〉 ::= ‘{’ { 〈Statement〉 } ‘}’
transition_table[(0, '{')] = 201
transition_table[(36, '{')] = 201
transition_table[(201, ' ')] = 202
transition_table[(202, 'l')] = 56 #<VariableDecl>
transition_table[(202, '_')] = 82 #<PrintStatment> <DelayStatment>  <PixelStatment>
transition_table[(202, 'r')] = 93 # <ReturnStatment>
transition_table[(202, 'i')] = 124 #<IfStatment>
transition_table[(202, 'f')] = 98 #<ForStatment> <FunctionDecleration>
transition_table[(202, 'w')] = 117 #<WhileStatment>
transition_table[(202, '{')] = 201 #<Block>





transition_table[(3, '}')] = 203
transition_table[(0, '}')] = 203
transition_table[(202, '}')] = 203
transition_table[(203, '}')] = 203
transition_table[(203, ' ')] = 128

#transition_table[(0, '?')] = 55
#final state
transition_table[(1, ';')] = 31
transition_table[(25, ';')] = 31
transition_table[(19, ';')] = 31
transition_table[(36, ';')] = 31
transition_table[(49, ';')] = 31
transition_table[(54, ';')] = 31
transition_table[(3, ';')] = 31


transition_table[(31, '}')] = 203



accepting_states = {31, 203, 201}


lexer = Lexer(transition_table, accepting_states)
filename = 'input.txt'
code = ''
with open(filename, 'r') as file:
    print('---- LEXER ----')
    for line in file:
        line = line.strip()
        if line:
            #valid_syntax, current_token, current_state, table = lexer.get_next_token(line)
            tokenTable = lexer.get_next_token(line)
            #code = code + line + ' '



parser = Parser(tokenTable)
ast = parser.parse_sel()
print()
print('---- PASER ----')
print(ast)
visitor = XmlVisitor(ast)
visitor.generate_xml()
visitor.write_to_file('output.xml')

print()
print('---- Semantic Analysis ----')
SemanticAnalysis = SemanticAnalysis(ast)
#print(xml)
print()
print('-*-*-*-THE END-*-*-*-')

