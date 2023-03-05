n, m = map(int, input().strip().split())
pattern = 1
full_string = str()
for i in range(1, n+1):
    if i == (n//2)+1:
        print("WELCOME".center(m, "-"))
        full_string += "WELCOME".center(m, "-") + "\n"
        pattern -= 2
    elif i < (n//2)+1:
        print((".|."*pattern).center(m, "-"))
        full_string += (".|."*pattern).center(m, "-") + "\n"
        pattern += 2
    elif i > (n//2)+1:
        print((".|."*pattern).center(m, "-"))
        full_string += (".|."*pattern).center(m, "-") + "\n"
        pattern -= 2
