letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['_', '(', ')', ';', ',', '->', '{', '}']
MultiplicativeOp = ['*', '/', 'and']
AdditiveOp = ['+', '-', 'or']
RelationalOp = ['<', '>', '==', '!=', '<=', '>=']
table = [[1, 6, 6, 6, 6, 6, 5, 5],
         [1, 1, 1, 2, 3, 4, 6, 6],
         [1, 6, 6, 6, 6, 6, 5, 5], 
         [1, 6, 6, 6, 6, 6, 5, 5], 
         [1, 6, 6, 6, 6, 6, 5, 5],
         [6, 6, 6, 2, 3, 4, 6, 6],
         [6, 6, 6, 6, 6, 6, 6, 6]]


column = [letter, digit, '_', MultiplicativeOp, AdditiveOp, RelationalOp, '__height', '__width']

currentState = 0
nextState = 0
counter = 0

# Ask the user to input a sentence
sentence = input("Enter a sentence: ")
# Convert the sentence to a list of characters
char_array = list(sentence)
# Remove the spaces from the array
char_array = [char for char in char_array if char != ' ']

def next_state(nextstate):
    for y in letter:
        if char_array[counter] == y:
            for i in range(len(column)):
                if column[i] == letter:
                    nextstate = table[nextstate][i]

    for x in digit:
        if char_array[counter] == x:
            #print(x)
            for i in range(len(column)):
                if column[i] == digit:
                    nextstate = table[nextstate][i]

    if char_array[counter] == '_':
        for i in range(len(column)):
            if column[i] == '_':
                nextstate = table[nextstate][i]

    return nextstate

for i in range(len(char_array)):
    currentState = next_state(currentState)
    print(currentState)