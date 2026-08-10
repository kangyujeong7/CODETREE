a,b = map(int, input().split())

#피보나치인가?
# 리스트를 만들어서 계속 추가하고 
#출력하는 프로그램을 만들어야함

arr = []
arr.append(a)
arr.append(b)
for i in range(10):
    if (i >=2 ):
         x = arr[i-2] + arr[i-1]
         buffer = list(str(x))
         Y = int (buffer[-1])  #int(Y) = buffer[-1]이건 왜 안되
         arr.append(Y)
print(*arr,sep=" ")


