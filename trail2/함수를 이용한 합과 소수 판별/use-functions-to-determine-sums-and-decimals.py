a, b = map(int, input().split())

# Please write your code here.

def count(z):
    numbers = [int(x) for x in str(z)]  # 결과: [1, 2, 3]
    sum = 0
    for i in numbers:
        sum+=i
    if sum %2 == 0:
        return True
    else:
        return False   


def prime(y):
    if y == 0 or y == 1:
        return False
    for i in range(2,y):
        if y % i == 0:
            return False
    return True


def number(x):
    if prime(x) and count(x):
        return True
    else:
        return False


cnt = 0

for i in range(a,b+1):
    if number(i):
        cnt +=1
    else:
        continue
print(cnt)