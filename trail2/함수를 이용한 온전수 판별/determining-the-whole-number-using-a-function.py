a, b = map(int, input().split())

# Please write your code here.


def number(x):
    if x % 2 == 0:
        return False
    elif x%10 == 5:
        return False
    elif x % 3 == 0 and x%9!=0:
        return False
    else:
        return True


cnt = 0
for i in range(a,b+1):
    if number(i):
        cnt+=1
    else:
        cnt +=0
print(cnt)

    