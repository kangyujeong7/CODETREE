N = int(input())
result = []

for i in range(1,N+1):
    if i % 2== 0:
        result.append(i)
    elif i % 3 == 0:
        result.append(i)
    elif i % 5 == 0:
        result.append(i)
print(N- len(result))