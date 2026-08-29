y = int(input())

# Please write your code here.

def leap_year(t):
    if t % 4 == 0:
        if t % 100 == 0 and t%400!=0:
            return False
        else:
            return True
    elif t % 100 == 0 and t%400!=0:
        return False

    else: 
        return False


if  leap_year(y):
    print("true")
else:
    print("false")