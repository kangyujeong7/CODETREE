n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


def change_element(e):
    arr[i] = (arr[i])//2
    

for i in range(0,n):
    if arr[i] % 2==0:
        change_element(i)

for i in arr:
    print(i,end=" ")
