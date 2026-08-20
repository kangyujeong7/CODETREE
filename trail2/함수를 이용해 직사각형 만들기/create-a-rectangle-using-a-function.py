
# def print_star(n,m):
#     for _ in range(n):
#         print("1"*m)

# row_num, col_num = tuple(map(int,input().split()))

# print_star(row_num,col_num)

n, m = map(int,input().split())

for _ in range(n):
    for _ in range(m):
        print("1",end="")
    print()
        