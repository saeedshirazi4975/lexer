LETT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

DIG = '0123456789'

KW = [
    'and', 'as', 'assert', 'break', 'class', 'continue', 
    'def', 'del', 'elif', 'else', 'except', 'exec', 
    'finally', 'for', 'from', 'global', 'if', 'import', 
    'in', 'is', 'lambda', 'not', 'or', 'pass', 
    'print', 'raise', 'return', 'try', 'while', 'with', 
    'yield'
]

ERROR_SYMBOLS = '$@~&'

#####-------------------------------------------------------------------------------------------------------------#####

def lexer(lexeme):

    try:
        if lexeme in KW:
            yield ('KW', lexeme)

        elif (lexeme[0] in LETT) and not any(i in ERROR_SYMBOLS or i == '.' for i in lexeme):
            yield ('ID', lexeme)

        elif (lexeme[0]==lexeme[-1]) and (lexeme[0] in '\'\"'):
             yield ('STR', lexeme)

        elif lexeme.count('.') > 1:
            yield ('unknown', lexeme)

        elif lexeme.count('.') == 1:
 
            if not any(i in LETT or i in ERROR_SYMBOLS for i in lexeme):
                yield ('F_NUM', lexeme)

            else:
                yield ('unknown', lexeme)

        elif lexeme.count('.') == 0:

            if any(i in LETT or i in ERROR_SYMBOLS for i in lexeme):
                yield ('unknown', lexeme)

            elif any(i in DIG for i in lexeme):
                yield ('NUM', lexeme)

        else:
            yield ('unknown', lexeme)

    except IndexError:
        yield ('unknown', lexeme)