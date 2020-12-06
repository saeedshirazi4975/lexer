LETT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

KW = ['for', 'if', 'while', 'then']

DIG = '0123456789'

#####-------------------------------------------------------------------------------------------------------------#####

def lexer(lexeme):

    try:
        if lexeme in KW:
            yield ('KW', lexeme)

        elif lexeme[0] == '#' and lexeme[1] == '$' and lexeme[2] in LETT and '.' not in lexeme:
            yield ('ID', lexeme)

        elif lexeme.count('.') > 1:
            yield ('unknown', lexeme)

        elif lexeme.count('.') == 1:

            if any(i in LETT for i in lexeme):
                yield ('unknown', lexeme)

            else:
                yield ('F_NUM', lexeme)

        elif lexeme.count('.') == 0:

            if any(i in LETT or i in '#$'for i in lexeme):
                yield ('unknown', lexeme)

            # elif any(i in '#$' for i in lexeme):
            #     yield ('unknown', lexeme)

            elif any(i in DIG for i in lexeme):
                yield ('NUM', lexeme)

        else:
            yield ('unknown', lexeme)

    except IndexError:
        yield ('unknown', lexeme)