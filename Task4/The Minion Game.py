def minion_game(string):
    kevin, stuart = 0, 0
    vowels = 'AEIOU'
    n = len(string)
    for i, c in enumerate(string):
        if vowels.find(c) != -1:
            kevin += n - i
        else:
            stuart += n - i
    if kevin - stuart != 0:
        print(f'Kevin {kevin}' if kevin > stuart else f'Stuart {stuart}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
