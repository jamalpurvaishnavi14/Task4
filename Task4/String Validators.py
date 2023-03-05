alphnu=0
alpha=0
dig=0
upper=0
lower=0
s=input()
for x in s:
    if alphnu and alpha and dig and upper and lower >0:
        break
    if x.isalnum():
        alphnu += 1
    if x.isalpha():
        alpha +=1 
    if x.isdigit():
        dig += 1
    if x.islower():
        upper += 1
    if x.isupper():
        lower +=1
    
resultado=[alphnu > 0, alpha > 0, dig > 0, upper > 0, lower > 0]
for response in resultado:
    print(response)
