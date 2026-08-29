n, m = map(int, input().split())

# Please write your code here.


def change(N,M):
    N,M = M, N
    return N,M


n, m = change(n,m)
print(n,m)
