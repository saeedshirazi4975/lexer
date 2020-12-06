from .parser import parser

def run():
    src_str = input('Enter your source :    ')
    src_itr = iter(src_str)

    print('\ntokens :\n--------')
    if src_str:
        for i in parser(src_itr):
            print(f'\t\t{i}')
    else:
        print('\t\t(\'there is nothing\')')
    print('end!\n-------------------------------------------------------------------------------------------------------\n')
