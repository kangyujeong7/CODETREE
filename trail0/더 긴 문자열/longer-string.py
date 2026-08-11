N = input().split()

if len(N[0]) == len(N[1]):
    print('same')
else:
    if len(N[0]) > len(N[1]):
        print(N[0],end=" ")
        print(len(N[0]))
    else: 
        print(N[1],end=" ")
        print(len(N[1]))