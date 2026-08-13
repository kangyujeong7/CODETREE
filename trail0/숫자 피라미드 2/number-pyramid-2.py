N = int(input())
j = 1

for i in range(1,N+1):
    for _ in range(i):
        print(j,end=" ")
        j+=1

    print()
