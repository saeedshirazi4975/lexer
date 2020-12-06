from .lexer import lexer

#####-------------------------------------------------------------------------------------------------------------#####

LETT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

OPT = ['+', '-', '*', '/', '%', '^', '=', '<', '>']

DLIM = '(){}[];'

DIG = '0123456789'

SPACE = ' '

#####-------------------------------------------------------------------------------------------------------------#####

def parser(tmp):

    lexeme = ''
    c = tmp.__next__()

    while c is not None:

        try:
            if c in OPT:
                if lexeme:
                    for i in lexer(lexeme):
                        yield i
                    lexeme = ''

                yield ('OPT', c)
                c = tmp.__next__()

            elif c in DLIM:
                if lexeme:
                    for i in lexer(lexeme):
                        yield i
                    lexeme = ''

                yield ('DLIM', c)
                c = tmp.__next__()

            elif c == SPACE:
                if lexeme:
                    for i in lexer(lexeme):
                        yield i
                    lexeme = ''
                c = tmp.__next__()

            elif (c == '@') or (c == '?') or (c == '&') or (c == '~') or (c == ',') or (c == ',') or (c == '#') or (c == '$') or (c == '.') or (c in LETT) or (c in DIG):
                lexeme += c
                c = tmp.__next__()

        except StopIteration:
            break

    if lexeme:
        for i in lexer(lexeme):
            yield i
