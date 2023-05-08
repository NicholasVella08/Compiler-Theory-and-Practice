from typing import List
class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"


# # class Lexer:
# #     def __init__(self, transition_table, accepting_states):
# #         self.transition_table = transition_table
# #         self.accepting_states = accepting_states
# #         self.current_state = 0
# #         self.current_token = ''
# #
# #     def get_next_token(self, input_string):
# #         self.current_state = 0
# #         self.current_token = ''
# #         for char in input_string:
# #             try:
# #                 self.current_state = self.transition_table[(self.current_state, char)]
# #                 self.current_token += char
# #             except KeyError:
# #                 return False, self.current_token, self.current_state
# #         if self.current_state in self.accepting_states:
# #             return True, self.current_token, self.current_state
# #         else:
# #             return False, self.current_token, self.current_state
#
class TokenType:
    INT = 'INT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MUL = 'MUL'
    DIV = 'DIV'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'
    LET = 'LET'
    VAR = 'VAR'
    ASSIGN = 'ASSIGN'
    SEMI = 'SEMI'
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
            tokenTable.append(['Colon', ' , '])
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

                print(f"Current token: {self.current_token}, current state: {self.current_state}")

                self.tokenTable = self.currentToken(char, self.current_state, self.tokenTable)  # pass tokenTable as argument


            except KeyError:
                return False, self.current_token, self.current_state, self.table

        print(self.tokenTable)

        if self.current_state in self.accepting_states:
            return True, self.current_token, self.current_state, self.table
        else:
            return False, self.current_token, self.current_state, self.table

class ASTNode:
    def __init__(self, value: str, children: List = []):
        self.value = value
        self.children = children

    def __str__(self):
        return f"{self.value}: {self.children}"


class Parser:
    def __init__(self, lexer, input):
        self.lexer = lexer
        self.current_token = None
        self.current_state = None
        self.input = input
        self.table = []

    def parse(self):
        valid_syntax, self.current_token, self.current_state, self.table = self.lexer.get_next_token(self.input)
        node = ''
        for i in range(2):
            node = self.program()
            print(node)


    def program(self):
        print(self.table)
        for i in self.table:
            #print(i)
            if i[1] == 59:

                index_59 = self.table.index(i)  # Get the index of the element with value 58
                del self.table[:index_59 + 1]  # Delete every element after the element with value 58
                return ('ASTVarDecl')


            if i[1] == 61:
                identifier = []
                identifierLoc = self.table.index(i)
                for x in range(identifierLoc):
                    identifier.append(self.table[x][0])
                j = ''
                node = 'ASTIdentifier: ', j.join(identifier)
                index = self.table.index(i)  # Get the index of the element with value 58
                del self.table[:index + 1]  # Delete every element after the element with value 58
                return(node)





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

with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            valid_syntax, current_token, current_state, table = lexer.get_next_token(line)
            if valid_syntax:
                print(f"Valid syntax! Current token: {current_token}, current state: {current_state}")
                #parser = Parser(lexer)
                #ast = parser.parse(line)
                #print(ast)
            else:
                print(f"Invalid syntax! Current token: {current_token}, current state: {current_state}")



#print(tokensTable)
