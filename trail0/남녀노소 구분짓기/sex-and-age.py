SEX = int(input())
AGE = int(input())

if SEX == int(False):
    if AGE>=19:
        print("MAN")
    else:
        print("BOY")
else:
    if AGE>=19:
        print("WOMAN")
    else:
        print("GIRL")