n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def change_element(N):
    for i in range(0,N):
        arr[i] = abs(arr[i])


change_element(n)

for num in arr:
    print(num,end=" ")