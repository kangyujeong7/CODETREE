N = int(input())

A = list(map(int, input().split()))
result=[]

for i in A:
    if i % 2 == 0:
        result.append(i)
result.reverse()
print(" ".join(map(str,result)))   
