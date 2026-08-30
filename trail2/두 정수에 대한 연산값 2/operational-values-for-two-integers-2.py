a, b = map(int, input().split())

# Please write your code here.
def modify(A,B):
    if A<B:
        A+=10
        B*=2
    else:
        B+=10
        A*=2
    return A,B



a,b = modify(a,b)
print(a,b)