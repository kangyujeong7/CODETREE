A, B = map(int, input().split())

# Please write your code here.
def swap(a,b):
    if a<b:
        b+=25
        a*=2
    else:
        a+=25
        b*=2
    return a,b


c,d = swap(A,B)
print(c,end=" ")
print(d)