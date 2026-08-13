N = int(input())

for i in range(N):
    elements = list(map(int,input().split()))
    store = [] 
    for j in range(elements[0],elements[1]+1):
        if j%2 == 0:
            store.append(j)
    total = sum(store)
    print(total)
    
    