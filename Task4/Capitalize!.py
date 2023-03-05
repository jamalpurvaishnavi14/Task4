def solve(s):
    words = s.split(' ')
    result = []
    for i in words:
        result.append(i.capitalize())
    s = ' '.join(result)
    return(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
