n, m = map(int, input().split())


def Greatest_Common_Divisior(n,m):
    count = 1

    if n < m:
        N = n 
    else :
        N = m  
    for i in range(N):
        if n % count == 0 and m % count == 0:
            gcd = count
        count+=1
    print(gcd)


Greatest_Common_Divisior(n,m)   

# Please write your code here.