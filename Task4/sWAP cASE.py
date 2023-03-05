def swap_case(s):
    newTxt = ""
    for i in range(len(s)):
        if( s[i] == s[i].upper()):
            newTxt += (s[i].lower())
        else:
            newTxt += (s[i].upper())
    return newTxt
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
