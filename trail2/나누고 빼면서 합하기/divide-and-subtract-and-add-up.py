n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

total_M = []

def f(M):
    while M >1:
        total_M.append(M)
        if  M% 2 ==1:
            M-=1
        else:
            M//=2

f(m)
sum = A[0]
for i  in total_M:
    sum+=A[i-1]

print(sum)