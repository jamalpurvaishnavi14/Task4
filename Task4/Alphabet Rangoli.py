def print_rangoli(size):
    s_list = []
    s_up, s_down = '', ''
    for asc in range(96 + size, 96, -1):
        s_list.append(chr(asc))
        row = '-'.join(s_list + (sorted(s_list)[1:])).center(((size - 1) * 3) + size, '-') + '\n'
        s_up = s_up + row
        s_down = row + s_down

    s_up = ''.join(list(s_up)[:-1])
    s_down = ''.join(list(s_down)[((size - 1) * 3) + size:])
    print(s_up + s_down)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
