def mutate_string(string, position, character):
    str_n=""
    for key,val in enumerate(string):
        if key==position:
            str_n+=character
        else:
            str_n+=val
    return str_n
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
